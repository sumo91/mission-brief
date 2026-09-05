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
import mission_brief_eval.judge as harness_judge_module  # noqa: E402
from mission_brief_eval.trace import session_turn_context, session_skill_evidence, runtime_reads  # noqa: E402
from mission_brief_eval.candidate import identify, bundle_digest  # noqa: E402
from mission_brief_eval.runner import HarnessRunner  # noqa: E402


_PLATFORM_BUILD_JUDGE_PACKET = harness_runner_module.build_judge_packet
_PLATFORM_HARNESS_IDENTITY = harness_runner_module.harness_identity
_PLATFORM_CONFIG = harness_runner_module.write_isolated_config
_PLATFORM_SETTINGS = harness_runner_module._execution_settings
_PLATFORM_ADAPTER = harness_runner_module.CodexAdapter
_PLATFORM_STAGE = harness_runner_module.stage
_PLATFORM_ESTABLISH = harness_runner_module.establish
_PLATFORM_CASE = HarnessRunner._run_case
REASONING_EFFORT: str | None = None
COMPANION = None
CASE_EVIDENCE: Path | None = None


def configure_evaluation(effort: str | None, companion: Path | None = None, companion_pack: Path | None = None) -> None:
    global REASONING_EFFORT, COMPANION
    REASONING_EFFORT = effort
    if bool(companion) != bool(companion_pack):
        raise ValueError("--companion and --companion-pack must be supplied together")
    COMPANION = None
    if companion is not None:
        contract = load_eval_pack(companion_pack.resolve()).skill_contract
        COMPANION = (companion.resolve(), contract, identify(companion.resolve(), contract))


def isolated_config_with_effort(**kwargs: object) -> Path:
    path = _PLATFORM_CONFIG(**kwargs)
    if REASONING_EFFORT:
        path.write_text(
            f'model_reasoning_effort = {json.dumps(REASONING_EFFORT)}\n'
            + path.read_text(encoding="utf-8"), encoding="utf-8"
        )
    if COMPANION and (kwargs["isolated_home"] / "skills" / COMPANION[1].skill_name).is_dir():
        runtime = (kwargs["isolated_home"] / "skills" / COMPANION[1].skill_name).resolve()
        marker = "\n[permissions.eval-executor.network]"
        config = path.read_text(encoding="utf-8")
        if config.count(marker) != 1:
            raise RuntimeError("unexpected isolated config boundary")
        path.write_text(config.replace(marker, f'\n{json.dumps(str(runtime))} = "read"\n{marker}'), encoding="utf-8")
    return path


def execution_settings_with_effort(config: RunConfig) -> dict[str, object]:
    return {**_PLATFORM_SETTINGS(config), "requested_reasoning_effort": REASONING_EFFORT,
            "companion": asdict(COMPANION[2]) if COMPANION else None}


def stage_discoverable(candidate, isolated_home, contract):
    # Native skill symlinks keep runtime outside the denied credential/session tree.
    isolated_home = isolated_home.resolve()
    runtime = _PLATFORM_STAGE(candidate, isolated_home.parent / "runtime", contract)
    link = isolated_home / "skills" / contract.skill_name
    link.parent.mkdir(parents=True, exist_ok=True)
    link.symlink_to(runtime, target_is_directory=True)
    return runtime


def establish_with_runtime(**kwargs):
    result = _PLATFORM_ESTABLISH(**kwargs)
    runtime = kwargs["isolated_home"].parent / "runtime"
    if runtime.is_dir():
        with kwargs["profile_path"].open("a", encoding="utf-8") as stream:
            stream.write(f'\n(allow file-read* (subpath {json.dumps(str(runtime))}))\n')
    return result


def stage_with_companion(candidate, isolated_home, contract):
    runtime = stage_discoverable(candidate, isolated_home, contract)
    if COMPANION:
        source, companion_contract, identity = COMPANION
        if companion_contract.skill_name == contract.skill_name:
            raise ValueError("companion must be a distinct Skill")
        staged = stage_discoverable(source, isolated_home, companion_contract)
        if bundle_digest(staged) != identity.digest:
            raise RuntimeError("companion changed after selection")
        if CASE_EVIDENCE:
            shutil.copytree(staged, CASE_EVIDENCE / "retained-companion-bundle")
    return runtime


def run_case_with_companion(self, case, output, *args, **kwargs):
    global CASE_EVIDENCE
    CASE_EVIDENCE = output / "cases" / (case.opaque_id if case else "i-0e519dab")
    CASE_EVIDENCE.mkdir(parents=True, exist_ok=True)
    try:
        return _PLATFORM_CASE(self, case, output, *args, **kwargs)
    finally:
        CASE_EVIDENCE = None


class ObservedAdapter(_PLATFORM_ADAPTER):
    def execute(self, prompt: str, *, turn_index: int, judge: bool = False):
        execution = super().execute(prompt, turn_index=turn_index, judge=judge)
        context = session_turn_context(self.isolated_home) or {}
        if REASONING_EFFORT and context.get("effort") != REASONING_EFFORT:
            execution.uncertainty.append(
                f"Reasoning effort mismatch: requested {REASONING_EFFORT}, observed {context.get('effort')!r}."
            )
            execution.returncode = execution.returncode or 1
        if COMPANION and not judge:
            _, contract, identity = COMPANION
            runtime = (self.isolated_home / "skills" / contract.skill_name).resolve()
            observed = bundle_digest(runtime)
            observation = {
                "identity": asdict(identity), "observed_digest": observed,
                "invocation": session_skill_evidence(self.isolated_home, runtime, contract.skill_name),
                "reads": runtime_reads(execution.events, runtime_bundle=runtime, observable_targets=("SKILL.md",)),
            }
            (CASE_EVIDENCE / f"turn-{turn_index + 1}.companion.json").write_text(
                json.dumps(observation, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            if observed != identity.digest:
                execution.uncertainty.append("Companion runtime identity changed during execution.")
                execution.returncode = execution.returncode or 1
        return execution


def build_judge_packet_with_directories(**kwargs: object) -> dict[str, object]:
    packet = _PLATFORM_BUILD_JUDGE_PACKET(**kwargs)
    workspace = Path(kwargs["executor_workspace"])
    packet["workspace_directories"] = sorted(
        path.relative_to(workspace).as_posix()
        for path in workspace.rglob("*")
        if path.is_dir()
    )
    if CASE_EVIDENCE:
        packet["execution_events"] = recorded_tool_events(CASE_EVIDENCE)
        packet["runtime_context"] = {
            "companion_skill": COMPANION[1].skill_name if COMPANION else None,
            "companion_observations": [
                {"turn": path.name, "reads": (value := json.loads(path.read_text(encoding="utf-8")))["reads"],
                 "injection_count": value["invocation"]["injection_count"],
                 "catalog_present": value["invocation"]["catalog_present"]}
                for path in sorted(CASE_EVIDENCE.glob("turn-*.companion.json"))
            ],
        }
    return packet


def recorded_tool_events(evidence: Path) -> dict[str, list[dict[str, object]]]:
    """CLI stdout omits some code-mode calls; private sessions retain their output."""
    recorded = {}
    types = {"function_call", "function_call_output", "custom_tool_call", "custom_tool_call_output"}
    for path in sorted((evidence / "codex-sessions").rglob("*.jsonl")):
        events = []
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            value = json.loads(line)
            payload = value.get("payload", {})
            if value.get("type") == "response_item" and payload.get("type") in types:
                events.append({"line": number, "timestamp": value.get("timestamp"), "payload": payload})
        recorded[path.relative_to(evidence).as_posix()] = events
    return recorded


def repository_extended_harness_identity() -> str:
    digest = hashlib.sha256()
    digest.update(_PLATFORM_HARNESS_IDENTITY().encode("utf-8"))
    digest.update(b"\0mission-brief-runner-extension\0")
    digest.update(Path(__file__).read_bytes())
    return digest.hexdigest()


harness_runner_module.build_judge_packet = build_judge_packet_with_directories
harness_runner_module.harness_identity = repository_extended_harness_identity
harness_runner_module._execution_settings = execution_settings_with_effort
harness_runner_module.write_isolated_config = isolated_config_with_effort
harness_judge_module.write_isolated_config = isolated_config_with_effort
harness_runner_module.CodexAdapter = ObservedAdapter
harness_judge_module.CodexAdapter = ObservedAdapter
harness_runner_module.stage = stage_with_companion
harness_runner_module.establish = establish_with_runtime
HarnessRunner._run_case = run_case_with_companion


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
        "--suite", choices=("behavior", "loader", "isolation", "all"), required=True,
        help="Choose the validation scope explicitly; use --case-id for targeted cases."
    )
    value.add_argument("--model", required=True)
    value.add_argument("--judge-model")
    value.add_argument("--reasoning-effort", choices=("low", "medium", "high", "xhigh", "max", "ultra"))
    value.add_argument("--companion", type=Path)
    value.add_argument("--companion-pack", type=Path)
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
    configure_evaluation(args.reasoning_effort, args.companion, args.companion_pack)
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
