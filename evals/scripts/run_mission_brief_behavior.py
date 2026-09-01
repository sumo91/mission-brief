#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys
from dataclasses import asdict
from pathlib import Path


REPOSITORY = Path(__file__).resolve().parents[2]
HARNESS_SOURCE = Path(
    os.environ.get(
        "MISSION_BRIEF_HARNESS_SRC",
        "/Users/admin/Documents/Codex/SkillEvalTestPlatform/src",
    )
).expanduser().resolve()
sys.path.insert(0, str(HARNESS_SOURCE))

from mission_brief_eval.eval_pack import load_eval_pack  # noqa: E402
from mission_brief_eval.models import RunConfig, Verdict  # noqa: E402
import mission_brief_eval.runner as harness_runner_module  # noqa: E402
from mission_brief_eval.runner import HarnessRunner  # noqa: E402


_PLATFORM_BUILD_JUDGE_PACKET = harness_runner_module.build_judge_packet
_PLATFORM_HARNESS_IDENTITY = harness_runner_module.harness_identity


def build_judge_packet_with_directories(**kwargs: object) -> dict[str, object]:
    packet = _PLATFORM_BUILD_JUDGE_PACKET(**kwargs)
    workspace = Path(kwargs["executor_workspace"])
    packet["workspace_directories"] = sorted(
        path.relative_to(workspace).as_posix()
        for path in workspace.rglob("*")
        if path.is_dir()
    )
    return packet


def repository_extended_harness_identity() -> str:
    digest = hashlib.sha256()
    digest.update(_PLATFORM_HARNESS_IDENTITY().encode("utf-8"))
    digest.update(b"\0mission-brief-runner-extension\0")
    digest.update(Path(__file__).read_bytes())
    return digest.hexdigest()


harness_runner_module.build_judge_packet = build_judge_packet_with_directories
harness_runner_module.harness_identity = repository_extended_harness_identity


DEFAULT_PACK = REPOSITORY / "evals" / "mission-brief-pack.json"
DEFAULT_OUTPUT = REPOSITORY / "evals" / "runs" / "mission-brief"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def evidence_manifest(run_dir: Path) -> dict[str, object]:
    files: dict[str, str] = {}
    for path in sorted(run_dir.rglob("*")):
        if not path.is_file() or path.is_symlink():
            continue
        relative = path.relative_to(run_dir).as_posix()
        if relative == "evidence-manifest.json":
            continue
        files[relative] = sha256(path)
    aggregate = hashlib.sha256()
    for relative, digest in sorted(files.items()):
        aggregate.update(relative.encode("utf-8"))
        aggregate.update(b"\0")
        aggregate.update(bytes.fromhex(digest))
    return {
        "algorithm": "SHA-256 over each relative path and file digest; evidence-manifest.json excluded",
        "file_count": len(files),
        "aggregate_sha256": aggregate.hexdigest(),
        "files": files,
    }


def derived_subset_pack(
    source: Path, output_dir: Path, case_ids: list[str]
) -> Path:
    raw = json.loads(source.read_text(encoding="utf-8"))
    cases = raw.get("cases")
    if not isinstance(cases, list):
        raise SystemExit("Eval Pack cases are unavailable")
    selected_ids = set(case_ids)
    available = {
        item.get("id")
        for item in cases
        if isinstance(item, dict) and isinstance(item.get("id"), str)
    }
    missing = selected_ids - available
    if missing:
        raise SystemExit(f"unknown case IDs: {sorted(missing)}")
    selected = [item for item in cases if item.get("id") in selected_ids]
    for case in selected:
        fixtures = case.get("fixtures")
        if not isinstance(fixtures, list):
            continue
        for index, fixture in enumerate(fixtures):
            if not isinstance(fixture, dict) or "source" not in fixture:
                continue
            fixture_source = (source.parent / fixture["source"]).resolve()
            try:
                fixture_source.relative_to(source.parent.resolve())
            except ValueError as exc:
                raise SystemExit(f"fixture escapes Eval Pack: {fixture_source}") from exc
            fixtures[index] = {
                "path": fixture["path"],
                "content": fixture_source.read_text(encoding="utf-8"),
            }
    raw["pack_id"] = f"{raw['pack_id']}-subset"
    raw["display_name"] = f"{raw['display_name']} subset"
    raw["cases"] = selected
    encoded = json.dumps(raw, ensure_ascii=False, indent=2) + "\n"
    digest = hashlib.sha256(encoded.encode("utf-8")).hexdigest()[:16]
    destination = output_dir / "_derived-packs" / f"{digest}.json"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(encoded, encoding="utf-8")
    return destination


def write_run_contract(run_dir: Path, report: object) -> None:
    candidate = report.candidate
    eval_pack = report.eval_pack
    lines = [
        "# Mission Brief behavior run contract",
        "",
        f"- Run ID: `{report.run_id}`",
        f"- Suite: `{report.suite}`",
        f"- Verdict: `{report.verdict.value}`",
        f"- Candidate source: `{candidate.source}`",
        f"- Candidate runtime digest: `{candidate.digest}`",
        f"- Candidate Git revision: `{candidate.git_revision or 'unavailable'}`",
        f"- Candidate runtime files: `{', '.join(candidate.runtime_files)}`",
        f"- Eval Pack: `{eval_pack.pack_id}` `{eval_pack.pack_version}`",
        f"- Eval Pack digest: `{eval_pack.digest}`",
        f"- Harness identity: `{report.harness_identity}`",
        f"- Case-set identity: `{report.case_set_identity}`",
        f"- Run-contract identity: `{report.run_contract_identity}`",
        f"- Executor model: `{report.executor_model}`",
        f"- Semantic judge model: `{report.semantic_judge_model}`",
        f"- Codex CLI: `{report.codex_cli_version}`",
        "",
        "Every case used a fresh isolated Codex home and workspace. Executors could read only the staged runtime bundle and visible case fixtures; the Eval Pack, rubrics, maintainer files, installed global Skills, and prior outputs were forbidden. Raw turns, manifests, diffs, resolved model observations, deterministic findings, semantic grades, and uncertainty are retained beside this contract.",
        "",
    ]
    (run_dir / "run-contract.md").write_text("\n".join(lines), encoding="utf-8")


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser(
        description="Run the repository Mission Brief Eval Pack with durable evidence."
    )
    value.add_argument("--candidate", type=Path, default=REPOSITORY)
    value.add_argument("--eval-pack", type=Path, default=DEFAULT_PACK)
    value.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    value.add_argument(
        "--suite", choices=("behavior", "loader", "isolation", "all"), default="all"
    )
    value.add_argument("--model", required=True)
    value.add_argument("--judge-model")
    value.add_argument("--codex-bin", type=Path)
    value.add_argument("--timeout", type=int, default=900)
    value.add_argument(
        "--case-id",
        action="append",
        default=[],
        help="Run only the selected case ID; repeat for an iteration subset.",
    )
    value.add_argument("--no-judge", action="store_true")
    value.add_argument(
        "--discard-workspaces",
        action="store_true",
        help="Do not retain final workspaces and staged runtime bundles in evidence.",
    )
    return value


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    codex_bin = (
        args.codex_bin.expanduser().resolve()
        if args.codex_bin
        else Path(shutil.which("codex") or "").resolve()
    )
    if not codex_bin.is_file():
        raise SystemExit("codex executable not found; pass --codex-bin")

    pack = load_eval_pack(args.eval_pack.expanduser().resolve())
    if args.case_id:
        subset_path = derived_subset_pack(
            Path(pack.identity.source), args.output_dir.expanduser().resolve(), args.case_id
        )
        pack = load_eval_pack(subset_path)
    config = RunConfig(
        candidate=args.candidate.expanduser().resolve(),
        eval_pack=pack,
        output_dir=args.output_dir.expanduser().resolve(),
        codex_bin=codex_bin,
        model=args.model,
        judge_model=args.judge_model or args.model,
        judge=not args.no_judge,
        keep_workspaces=not args.discard_workspaces,
        timeout_seconds=args.timeout,
    )
    report = HarnessRunner(config).run(args.suite)
    run_dir = config.output_dir / report.run_id
    write_run_contract(run_dir, report)
    manifest = evidence_manifest(run_dir)
    (run_dir / "evidence-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    summary = {
        "report": str(run_dir / "report.json"),
        "run_contract": str(run_dir / "run-contract.md"),
        "evidence_manifest": str(run_dir / "evidence-manifest.json"),
        "verdict": report.verdict.value,
        "candidate": asdict(report.candidate),
        "eval_pack": asdict(report.eval_pack),
        "evidence_aggregate": manifest["aggregate_sha256"],
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if report.verdict == Verdict.PASSED:
        return 0
    if report.verdict == Verdict.FAILED:
        return 1
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
