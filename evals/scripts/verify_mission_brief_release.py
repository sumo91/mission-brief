#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, Iterable


REPOSITORY = Path(__file__).resolve().parents[2]
HARNESS_SOURCE = Path(
    os.environ.get(
        "MISSION_BRIEF_HARNESS_SRC",
        "/Users/admin/Documents/Codex/SkillEvalTestPlatform/src",
    )
).expanduser().resolve()
sys.path.insert(0, str(HARNESS_SOURCE))

from mission_brief_eval.candidate import identify, runtime_files  # noqa: E402
from mission_brief_eval.eval_pack import load_eval_pack  # noqa: E402


BASELINE_REVISION = "8adf782bf61e7051f9afe14d2e25166790e8bdc3"
MAIN_PACK = REPOSITORY / "evals" / "mission-brief-pack.json"
EXPECTED_RUNTIME_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    "references/parent-child.md",
    "references/source-fidelity.md",
]
SOURCE_FIDELITY_REQUIRED = {
    "c-10000016",
    "c-10000017",
    "c-10000018",
    "c-1000001e",
}
SOURCE_FIDELITY_FORBIDDEN = {"c-10000001", "c-1000001d"}
EXPECTED_STATIC_CASES = {
    *(f"c-100000{value:02x}" for value in range(1, 31)),
    "l-20000001",
    "l-20000002",
    "l-20000003",
}
EXPECTED_BLIND_CASES = {"h-40000001", "h-40000002"}
REQUIRED_TRACEABILITY_FINDINGS = {
    "Confirmed findings remain non-binding Reference context unless a cited adopted decision or applicable Authority Source gives them a binding effect; copying them into the Brief does not itself make them contract requirements.",
    "The reader does not invent a user decision or authorization gate for choosing the representative supported consumer when the Brief leaves that sample selection to execution.",
}
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


class VerificationError(RuntimeError):
    pass


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def json_object(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise VerificationError(f"expected JSON object: {path}")
    return value


def fixture_entries(value: Any) -> Iterable[dict[str, str]]:
    if isinstance(value, dict):
        if isinstance(value.get("path"), str) and isinstance(value.get("sha256"), str):
            yield value
        for item in value.values():
            yield from fixture_entries(item)
    elif isinstance(value, list):
        for item in value:
            yield from fixture_entries(item)


def verify_fixture_manifests() -> int:
    checked = 0
    for manifest_path in sorted((REPOSITORY / "evals" / "fixtures").glob("*/manifest.json")):
        manifest = json_object(manifest_path)
        for item in fixture_entries(manifest):
            target = (manifest_path.parent / item["path"]).resolve()
            try:
                target.relative_to(manifest_path.parent.resolve())
            except ValueError as exc:
                raise VerificationError(f"fixture manifest path escapes its case: {target}") from exc
            if not target.is_file() or target.is_symlink():
                raise VerificationError(f"fixture manifest target missing or unsafe: {target}")
            actual = sha256(target)
            if actual != item["sha256"]:
                raise VerificationError(
                    f"fixture hash mismatch: {target} expected {item['sha256']} got {actual}"
                )
            checked += 1
    return checked


def verify_links() -> int:
    checked = 0
    roots = [
        path
        for path in REPOSITORY.rglob("*.md")
        if ".git" not in path.parts and "evals/runs" not in path.as_posix()
    ]
    for source in sorted(roots):
        text = source.read_text(encoding="utf-8")
        for raw in LINK.findall(text):
            value = raw.strip().strip("<>").split("#", 1)[0]
            if not value or value.startswith(("http://", "https://", "mailto:")):
                continue
            value = re.sub(r":\d+$", "", value)
            target = Path(value) if value.startswith("/") else source.parent / value
            if not target.resolve().exists():
                raise VerificationError(f"broken local link in {source}: {raw}")
            checked += 1
    return checked


def verify_frontmatter() -> None:
    for relative, expected_name in (("SKILL.md", "mission-brief"), ("mission-review/SKILL.md", "mission-review")):
        text = (REPOSITORY / relative).read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
        if match is None:
            raise VerificationError(f"invalid frontmatter boundary: {relative}")
        fields: dict[str, str] = {}
        for line in match.group(1).splitlines():
            key, separator, value = line.partition(":")
            if not separator:
                raise VerificationError(f"unsupported frontmatter line in {relative}: {line}")
            fields[key.strip()] = value.strip().strip('"').strip("'")
        if fields.get("name") != expected_name:
            raise VerificationError(f"wrong Skill name in {relative}")
        if not fields.get("description"):
            raise VerificationError(f"missing Skill description in {relative}")
        if fields.get("disable-model-invocation") != "true":
            raise VerificationError(f"{relative} must keep explicit-only invocation")


def verify_runtime_boundary() -> tuple[str, str]:
    pack = load_eval_pack(MAIN_PACK)
    selected = identify(REPOSITORY, pack.skill_contract)
    if selected.runtime_files != EXPECTED_RUNTIME_FILES:
        raise VerificationError(
            f"Mission Brief runtime boundary drifted: {selected.runtime_files}"
        )
    review = [
        path.relative_to(REPOSITORY / "mission-review").as_posix()
        for path in sorted((REPOSITORY / "mission-review").rglob("*"))
        if path.is_file() and not path.is_symlink()
    ]
    if review != ["SKILL.md", "agents/openai.yaml"]:
        raise VerificationError(f"Mission Review runtime boundary drifted: {review}")
    metadata = (REPOSITORY / "agents" / "openai.yaml").read_text(encoding="utf-8")
    review_metadata = (REPOSITORY / "mission-review" / "agents" / "openai.yaml").read_text(
        encoding="utf-8"
    )
    if "allow_implicit_invocation: false" not in metadata or "allow_implicit_invocation: false" not in review_metadata:
        raise VerificationError("UI metadata must keep both Skills explicit-only")
    return selected.digest, selected.git_revision or "unavailable"


def verify_migration() -> None:
    old = REPOSITORY / "docs" / "mission-briefs" / "mission-review-mvp.md"
    new = REPOSITORY / "docs" / "missions" / "reliable-mission-review" / "brief.md"
    if old.exists() or not new.is_file():
        raise VerificationError("Mission Review contract migration is incomplete")
    baseline = subprocess.run(
        ["git", "show", f"{BASELINE_REVISION}:docs/mission-briefs/mission-review-mvp.md"],
        cwd=REPOSITORY,
        capture_output=True,
        check=False,
    )
    if baseline.returncode != 0:
        raise VerificationError("cannot recover migrated baseline contract")
    if new.read_bytes() != baseline.stdout:
        raise VerificationError("migrated Mission Review contract is not byte-for-byte preserved")


def resolve_run(value: Path) -> Path:
    resolved = value.expanduser().resolve()
    run = resolved if resolved.is_dir() else resolved.parent
    if not (run / "report.json").is_file():
        raise VerificationError(f"run report is unavailable: {value}")
    return run


def verify_evidence_manifest(run: Path) -> str:
    recorded = json_object(run / "evidence-manifest.json")
    files: dict[str, str] = {}
    for path in sorted(run.rglob("*")):
        if not path.is_file() or path.is_symlink():
            continue
        relative = path.relative_to(run).as_posix()
        if relative == "evidence-manifest.json":
            continue
        files[relative] = sha256(path)
    if recorded.get("files") != files:
        raise VerificationError(f"evidence file manifest drifted: {run}")
    aggregate = hashlib.sha256()
    for relative, digest in sorted(files.items()):
        aggregate.update(relative.encode("utf-8"))
        aggregate.update(b"\0")
        aggregate.update(bytes.fromhex(digest))
    actual = aggregate.hexdigest()
    if recorded.get("aggregate_sha256") != actual:
        raise VerificationError(f"evidence aggregate mismatch: {run}")
    return actual


def report_cases(report: dict[str, Any]) -> dict[str, dict[str, Any]]:
    values = report.get("cases")
    if not isinstance(values, list):
        raise VerificationError("report cases are unavailable")
    result = {
        item["opaque_id"]: item
        for item in values
        if isinstance(item, dict) and isinstance(item.get("opaque_id"), str)
    }
    if len(result) != len(values):
        raise VerificationError("report case identities are duplicated or invalid")
    return result


def require_passed(report: dict[str, Any], expected: set[str], label: str) -> None:
    if report.get("verdict") != "PASSED":
        raise VerificationError(f"{label} aggregate verdict is not PASSED")
    cases = report_cases(report)
    missing = expected - cases.keys()
    if missing:
        raise VerificationError(f"{label} is missing cases: {sorted(missing)}")
    failed = {case_id: cases[case_id].get("verdict") for case_id in expected if cases[case_id].get("verdict") != "PASSED"}
    if failed:
        raise VerificationError(f"{label} has non-passing cases: {failed}")


def verify_blind_semantics(report: dict[str, Any], run: Path) -> None:
    pack = json_object(run / "eval-pack.json")
    raw_cases = pack.get("cases")
    if not isinstance(raw_cases, list):
        raise VerificationError("blind Eval Pack cases are unavailable")
    rubrics: dict[str, set[str]] = {}
    for item in raw_cases:
        if not isinstance(item, dict):
            raise VerificationError("blind Eval Pack has an invalid case")
        case_id = item.get("opaque_id", item.get("id"))
        if not isinstance(case_id, str):
            raise VerificationError("blind Eval Pack has an invalid case")
        values = item.get("rubric")
        if not isinstance(values, list) or not values or not all(isinstance(value, str) for value in values):
            raise VerificationError(f"blind rubric is unavailable: {case_id}")
        criteria = set(values)
        if len(criteria) != len(values):
            raise VerificationError(f"blind rubric has duplicate criteria: {case_id}")
        rubrics[case_id] = criteria
    if set(rubrics) != EXPECTED_BLIND_CASES:
        raise VerificationError("blind Eval Pack case set drifted")
    if not REQUIRED_TRACEABILITY_FINDINGS <= rubrics["h-40000002"]:
        raise VerificationError("traceability blind rubric is missing required semantic findings")

    for case_id, case in report_cases(report).items():
        findings = case.get("semantic_findings")
        if not isinstance(findings, list):
            raise VerificationError(f"blind semantic findings are unavailable: {case_id}")
        by_criterion: dict[str, str] = {}
        for finding in findings:
            if not isinstance(finding, dict) or not isinstance(finding.get("criterion"), str):
                raise VerificationError(f"blind semantic finding is invalid: {case_id}")
            criterion = finding["criterion"]
            if criterion in by_criterion:
                raise VerificationError(f"blind semantic finding is duplicated: {case_id}")
            by_criterion[criterion] = finding.get("verdict")
        if set(by_criterion) != rubrics[case_id]:
            raise VerificationError(f"blind semantic findings do not match the rubric: {case_id}")
        failed = {
            criterion: verdict
            for criterion, verdict in by_criterion.items()
            if verdict != "PASSED"
        }
        if failed:
            raise VerificationError(f"blind semantic findings did not pass: {case_id}: {failed}")


def verify_progressive_disclosure(report: dict[str, Any]) -> None:
    cases = report_cases(report)
    reads_by_case: dict[str, set[str]] = {}
    for case_id, case in cases.items():
        turns = case.get("turns")
        if not isinstance(turns, list):
            raise VerificationError(f"candidate case has no turns: {case_id}")
        reads: set[str] = set()
        for turn in turns:
            if not isinstance(turn, dict) or not isinstance(turn.get("runtime_files_read"), list):
                raise VerificationError(f"candidate case has invalid runtime read evidence: {case_id}")
            reads.update(
                value for value in turn["runtime_files_read"] if isinstance(value, str)
            )
            events = turn.get("access_events")
            if not isinstance(events, list):
                raise VerificationError(f"candidate case has invalid access evidence: {case_id}")
            for event in events:
                if not isinstance(event, dict) or event.get("exit_code") != 0:
                    continue
                accesses = event.get("path_accesses")
                if not isinstance(accesses, list):
                    continue
                for access in accesses:
                    if not isinstance(access, dict) or not isinstance(access.get("path"), str):
                        continue
                    path = access["path"]
                    marker = "/skills/mission-brief/references/"
                    if marker in path and path.endswith(".md"):
                        reads.add("references/" + path.rsplit("/", 1)[-1])
        reads_by_case[case_id] = reads

    source_reference = "references/source-fidelity.md"
    missing = {
        case_id
        for case_id in SOURCE_FIDELITY_REQUIRED
        if source_reference not in reads_by_case.get(case_id, set())
    }
    if missing:
        raise VerificationError(
            f"source-fidelity reference was not loaded for required cases: {sorted(missing)}"
        )

    unexpected = {
        case_id: sorted(
            value
            for value in reads_by_case.get(case_id, set())
            if value.startswith("references/")
        )
        for case_id in SOURCE_FIDELITY_FORBIDDEN
        if any(
            value.startswith("references/")
            for value in reads_by_case.get(case_id, set())
        )
    }
    if unexpected:
        raise VerificationError(
            f"simple cases loaded conditional references: {unexpected}"
        )


def verify_release_runs(
    candidate_run_value: Path,
    blind_run_value: Path,
    baseline_run_value: Path,
    candidate_digest: str,
) -> tuple[dict[str, str], str]:
    candidate_run = resolve_run(candidate_run_value)
    blind_run = resolve_run(blind_run_value)
    baseline_run = resolve_run(baseline_run_value)
    aggregates = {
        "candidate": verify_evidence_manifest(candidate_run),
        "blind": verify_evidence_manifest(blind_run),
        "baseline": verify_evidence_manifest(baseline_run),
    }
    candidate = json_object(candidate_run / "report.json")
    blind = json_object(blind_run / "report.json")
    baseline = json_object(baseline_run / "report.json")
    require_passed(candidate, EXPECTED_STATIC_CASES | {"i-0e519dab"}, "candidate run")
    verify_progressive_disclosure(candidate)
    require_passed(blind, EXPECTED_BLIND_CASES, "blind run")
    verify_blind_semantics(blind, blind_run)
    for label, report in (("candidate", candidate), ("blind", blind)):
        identity = report.get("candidate")
        if not isinstance(identity, dict) or identity.get("digest") != candidate_digest:
            raise VerificationError(f"{label} run candidate digest does not match frozen candidate")
    baseline_identity = baseline.get("candidate")
    if not isinstance(baseline_identity, dict) or baseline_identity.get("git_revision") != BASELINE_REVISION:
        raise VerificationError("baseline run is not bound to the required historical revision")
    baseline_cases = report_cases(baseline)
    if set(baseline_cases) != {"b-30000001"}:
        raise VerificationError("baseline run does not contain the synthetic preservation case")
    if baseline_cases["b-30000001"].get("verdict") != "PASSED":
        raise VerificationError("synthetic preservation baseline did not pass")
    baseline_pack = baseline.get("eval_pack")
    if not isinstance(baseline_pack, dict) or baseline_pack.get("pack_id") != "mission-brief-synthetic-preservation-baseline":
        raise VerificationError("baseline evidence is not labeled as synthetic preservation")
    source_manifest = json_object(
        REPOSITORY / "evals" / "fixtures" / "mb-000-original-feedback-regression" / "manifest.json"
    )
    if source_manifest.get("provenance_status") != "incomplete-authentic-source-set" or not source_manifest.get(
        "missing_authentic_inputs"
    ):
        raise VerificationError("historical source gap is not recorded honestly")
    binding = json_object(blind_run / "blind-source-binding.json")
    if binding.get("source_run_id") != candidate.get("run_id") or binding.get("candidate_digest") != candidate_digest:
        raise VerificationError("blind evidence is not bound to the candidate authoring run")
    return aggregates, "INCONCLUSIVE"


def verify_installed_runtime(root: Path) -> None:
    installed = root.expanduser().resolve()
    for relative in EXPECTED_RUNTIME_FILES:
        source = REPOSITORY / relative
        target = installed / relative
        if not target.is_file() or not source.is_file() or source.read_bytes() != target.read_bytes():
            raise VerificationError(f"installed runtime mismatch: {target}")
    actual = [
        path.relative_to(installed).as_posix()
        for path in sorted(installed.rglob("*"))
        if path.is_file() and not path.is_symlink()
    ]
    if actual != EXPECTED_RUNTIME_FILES:
        raise VerificationError(f"installed runtime contains unexpected files: {actual}")


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser(description="Verify Mission Brief static and durable release evidence.")
    value.add_argument("--candidate-run", type=Path)
    value.add_argument("--blind-run", type=Path)
    value.add_argument("--baseline-run", type=Path)
    value.add_argument("--installed-runtime", type=Path)
    return value


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    provided = [args.candidate_run, args.blind_run, args.baseline_run]
    if any(provided) and not all(provided):
        raise SystemExit("candidate, blind, and baseline runs must be supplied together")
    verify_frontmatter()
    fixture_count = verify_fixture_manifests()
    link_count = verify_links()
    verify_migration()
    candidate_digest, revision = verify_runtime_boundary()
    result: dict[str, Any] = {
        "static": "PASSED",
        "candidate_digest": candidate_digest,
        "git_revision": revision,
        "runtime_files": EXPECTED_RUNTIME_FILES,
        "fixture_files_verified": fixture_count,
        "local_links_verified": link_count,
    }
    if all(provided):
        aggregates, historical_reproduction = verify_release_runs(
            args.candidate_run,
            args.blind_run,
            args.baseline_run,
            candidate_digest,
        )
        result["release_evidence"] = "PASSED"
        result["evidence_aggregates"] = aggregates
        result["historical_reproduction"] = historical_reproduction
    if args.installed_runtime:
        verify_installed_runtime(args.installed_runtime)
        result["installed_runtime"] = "PASSED"
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except VerificationError as exc:
        print(f"FAILED: {exc}", file=sys.stderr)
        raise SystemExit(1)
