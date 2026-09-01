#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
from dataclasses import asdict
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
REPOSITORY = SCRIPT_DIR.parents[1]
sys.path.insert(0, str(SCRIPT_DIR))

from run_mission_brief_behavior import (  # noqa: E402
    HARNESS_SOURCE,
    evidence_manifest,
    write_run_contract,
)

sys.path.insert(0, str(HARNESS_SOURCE))

from mission_brief_eval.candidate import identify  # noqa: E402
from mission_brief_eval.eval_pack import (  # noqa: E402
    _effective_content,
    _parse_case,
    _parse_skill_contract,
    digest_value,
)
from mission_brief_eval.models import (  # noqa: E402
    EvalPack,
    EvalPackIdentity,
    RunConfig,
    Verdict,
)
import mission_brief_eval.runner as harness_runner_module  # noqa: E402
from mission_brief_eval.runner import HarnessRunner  # noqa: E402


DEFAULT_OUTPUT = REPOSITORY / "evals" / "runs" / "mission-brief-blind"
SOURCE_CASE = "c-10000016"
BLIND_CASES = ("h-40000001", "h-40000002")


_REPOSITORY_EXTENDED_HARNESS_IDENTITY = harness_runner_module.harness_identity


def blind_extended_harness_identity() -> str:
    digest = hashlib.sha256()
    digest.update(_REPOSITORY_EXTENDED_HARNESS_IDENTITY().encode("utf-8"))
    digest.update(b"\0mission-brief-blind-runner-extension\0")
    digest.update(Path(__file__).read_bytes())
    return digest.hexdigest()


harness_runner_module.harness_identity = blind_extended_harness_identity


class BlindHarnessRunner(HarnessRunner):
    """Run the platform harness with one narrow, locally verified pack exception.

    The upstream v1 pack schema couples semantic rubrics to required Skill
    invocation. Blind handoff evaluation needs the inverse: the staged Skill must
    remain unread while a private semantic rubric grades the fresh reader's output.
    All execution, isolation, deterministic findings, judging, and evidence writing
    still use the platform runner unchanged.
    """

    def __init__(self, config: RunConfig) -> None:
        verify_blind_pack_integrity(config.eval_pack)
        self.config = config
        self.candidate_identity = identify(
            config.candidate, config.eval_pack.skill_contract
        )


def read_json(path: Path) -> dict[str, object]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise SystemExit(f"expected a JSON object: {path}")
    return value


def resolve_report(value: Path) -> Path:
    resolved = value.expanduser().resolve()
    report = resolved / "report.json" if resolved.is_dir() else resolved
    if not report.is_file():
        raise SystemExit(f"source report not found: {report}")
    return report


def source_artifact(report_path: Path) -> tuple[dict[str, object], Path, Path]:
    report = read_json(report_path)
    cases = report.get("cases")
    if not isinstance(cases, list):
        raise SystemExit("source report has no cases")
    matching = [item for item in cases if isinstance(item, dict) and item.get("opaque_id") == SOURCE_CASE]
    if len(matching) != 1:
        raise SystemExit(f"source report must contain exactly one {SOURCE_CASE} result")
    case = matching[0]
    if case.get("verdict") != "PASSED":
        raise SystemExit(f"source case {SOURCE_CASE} did not pass")
    turns = case.get("turns")
    if not isinstance(turns, list) or len(turns) != 1 or not isinstance(turns[0], dict):
        raise SystemExit(f"source case {SOURCE_CASE} has an unexpected turn shape")
    artifacts = turns[0].get("artifact_changes")
    if not isinstance(artifacts, list) or len(artifacts) != 1 or not isinstance(artifacts[0], str):
        raise SystemExit(f"source case {SOURCE_CASE} must produce exactly one artifact")
    workspace = report_path.parent / "cases" / SOURCE_CASE / "workspace-final"
    brief = (workspace / artifacts[0]).resolve()
    proposal = (workspace / "proposal.md").resolve()
    for path in (brief, proposal):
        try:
            path.relative_to(workspace.resolve())
        except ValueError as exc:
            raise SystemExit(f"source path escapes retained workspace: {path}") from exc
        if not path.is_file() or path.is_symlink():
            raise SystemExit(f"retained source file is unavailable: {path}")
    return report, brief, proposal


def dynamic_pack(brief: str, proposal: str) -> dict[str, object]:
    contract = {
        "skill_name": "mission-brief",
        "display_name": "Mission Brief",
        "explicit_invocation": "$mission-brief",
        "conditional_runtime_reference": "references/mission-zero.md",
        "runtime_reference_finding_name": "mission-zero-reference",
        "runtime_reference_roots": ["references"],
        "runtime_reference_suffixes": [".md"],
        "runtime_metadata_files": ["agents/openai.yaml"],
        "artifact_path_prefixes": ["docs/missions", "docs/mission-briefs"],
        "artifact_path_suffixes": [".md"],
        "protected_project_files": [],
        "protected_candidate_files": [],
        "global_installation_roots": [".agents/skills", ".codex/skills"],
        "semantic_judge_policy": (
            "Judge the blind reader's recovery from only the visible packet. Do not reward exact wording. "
            "Do not use inaccessible authoring context or the staged Skill as evidence. A viable route must "
            "satisfy the recovered contract without silently turning a Reference Source suggestion into authority."
        ),
    }
    return {
        "schema_version": "1.0",
        "pack_id": "mission-brief-dynamic-blind",
        "pack_version": "1.0.0",
        "display_name": "Mission Brief Dynamic Blind Handoffs",
        "platform_contract": "skill-eval-pack-v1",
        "capability_requirements": ["local-files", "local-process"],
        "skill_contract": contract,
        "cases": [
            {
                "id": "h-40000001",
                "suite": "behavior",
                "turns": [
                    {
                        "prompt": (
                            "你是没有参与编写过程的执行 Agent。只阅读 brief.md；你看不到原对话和详细方案。"
                            "说明你恢复出的结果、实质失败、证据义务、边界、目标位置和授权，并列出任何因来源不可见而必须保留的不确定性。"
                            "不要修改工作区，也不要调用任何技能。"
                        ),
                        "assertions": {
                            "artifact_count": 0,
                            "runtime_reference": "forbidden",
                            "skill_invocation": "forbidden",
                        },
                    }
                ],
                "fixtures": [{"path": "brief.md", "content": brief}],
                "rubric": [
                    "The fresh reader accurately recovers the outcome, meaningful failure, proof obligations, boundaries, target, and authority from the Brief alone.",
                    "The reader does not invent missing proposal details or silently promote an unavailable source into contract content.",
                    "Any source-dependent uncertainty is explicit without making the otherwise recoverable contract unusable.",
                ],
            },
            {
                "id": "h-40000002",
                "suite": "behavior",
                "turns": [
                    {
                        "prompt": (
                            "你是没有参与编写过程的执行 Agent。阅读 brief.md 和 proposal.md。说明恢复出的合同、来源状态、"
                            "已确认依赖与风险，以及哪些建议仍非绑定；然后提出一条可行实现路线。该路线的控制机制必须实质区别于"
                            "proposal.md 中列出的候选机制，不能只是换词、换序或从候选项中挑一个。不要修改工作区，也不要调用任何技能。"
                        ),
                        "assertions": {
                            "artifact_count": 0,
                            "runtime_reference": "forbidden",
                            "skill_invocation": "forbidden",
                        },
                    }
                ],
                "fixtures": [
                    {"path": "brief.md", "content": brief},
                    {"path": "proposal.md", "content": proposal},
                ],
                "rubric": [
                    "The reader distinguishes adopted decisions and confirmed findings from candidate approaches and advisory investigation order.",
                    "The reader recovers both shared consumers, importer recreation behavior, and the distinct stale entry points as material context.",
                    "The proposed route satisfies the contract while using a controlling mechanism materially different from registry tombstones, moving the shared script, leaving consumers unchanged as a strategy, or adding a permanent repository-wide import simulator.",
                ],
            },
        ],
    }


def load_blind_pack(path: Path) -> EvalPack:
    """Load the generated blind pack while preserving the platform's identities.

    Parsing delegates to the platform's field validators. The local exception is
    limited to allowing forbidden invocation plus a rubric on behavior cases.
    """

    source = path.expanduser().resolve()
    raw = read_json(source)
    expected_keys = {
        "schema_version",
        "pack_id",
        "pack_version",
        "display_name",
        "platform_contract",
        "capability_requirements",
        "skill_contract",
        "cases",
    }
    if set(raw) != expected_keys:
        raise SystemExit("dynamic blind pack has an unexpected top-level shape")
    if raw["schema_version"] != "1.0" or raw["platform_contract"] != "skill-eval-pack-v1":
        raise SystemExit("dynamic blind pack uses an unsupported platform contract")
    capabilities_raw = raw["capability_requirements"]
    if not isinstance(capabilities_raw, list) or set(capabilities_raw) != {
        "local-files",
        "local-process",
    }:
        raise SystemExit("dynamic blind pack must request the complete local capability profile")
    capabilities = tuple(sorted(capabilities_raw))
    skill_contract = _parse_skill_contract(raw["skill_contract"])
    cases_raw = raw["cases"]
    if not isinstance(cases_raw, list):
        raise SystemExit("dynamic blind pack cases are unavailable")
    cases = tuple(
        _parse_case(item, index=index, pack_root=source.parent)[0]
        for index, item in enumerate(cases_raw)
    )
    effective = _effective_content(
        schema_version=str(raw["schema_version"]),
        pack_id=str(raw["pack_id"]),
        pack_version=str(raw["pack_version"]),
        display_name=str(raw["display_name"]),
        capabilities=capabilities,
        skill_contract=skill_contract,
        cases=cases,
    )
    identity = EvalPackIdentity(
        source=str(source),
        digest=digest_value(effective),
        pack_id=str(raw["pack_id"]),
        pack_version=str(raw["pack_version"]),
        schema_version=str(raw["schema_version"]),
        display_name=str(raw["display_name"]),
        capability_requirements=capabilities,
        source_files=(source.name,),
    )
    pack = EvalPack(
        identity=identity,
        skill_contract=skill_contract,
        cases=cases,
        source_paths=(source,),
    )
    verify_blind_pack_integrity(pack)
    return pack


def verify_blind_pack_integrity(pack: EvalPack) -> None:
    source = Path(pack.identity.source).resolve()
    if pack.source_paths != (source,) or not source.is_file() or source.is_symlink():
        raise SystemExit("dynamic blind pack source is unavailable or ambiguous")
    reparsed = read_json(source)
    expected_ids = tuple(case.opaque_id for case in pack.cases)
    if expected_ids != BLIND_CASES:
        raise SystemExit(f"dynamic blind pack must contain exactly {BLIND_CASES}")
    if len(pack.cases) != 2:
        raise SystemExit("dynamic blind pack must contain exactly two cases")
    for case in pack.cases:
        if case.suite != "behavior" or not case.rubric or len(case.turns) != 1:
            raise SystemExit("each blind case must be a one-turn semantic behavior case")
        turn = case.turns[0]
        if (
            turn.expected_invocation != "forbidden"
            or turn.expected_reference is not False
            or turn.expected_artifact_count != 0
            or pack.skill_contract.explicit_invocation in turn.prompt
        ):
            raise SystemExit(
                "each blind case must forbid Skill invocation and runtime reads, and produce no artifact"
            )
    effective = _effective_content(
        schema_version=pack.identity.schema_version,
        pack_id=pack.identity.pack_id,
        pack_version=pack.identity.pack_version,
        display_name=pack.identity.display_name,
        capabilities=pack.identity.capability_requirements,
        skill_contract=pack.skill_contract,
        cases=pack.cases,
    )
    if digest_value(effective) != pack.identity.digest:
        raise SystemExit("dynamic blind pack was mutated after validation")
    source_contract = _parse_skill_contract(reparsed.get("skill_contract"))
    source_cases_raw = reparsed.get("cases")
    if not isinstance(source_cases_raw, list):
        raise SystemExit("dynamic blind pack source cases are unavailable")
    source_cases = tuple(
        _parse_case(item, index=index, pack_root=source.parent)[0]
        for index, item in enumerate(source_cases_raw)
    )
    source_capabilities_raw = reparsed.get("capability_requirements")
    if not isinstance(source_capabilities_raw, list):
        raise SystemExit("dynamic blind pack source capabilities are unavailable")
    source_effective = _effective_content(
        schema_version=str(reparsed.get("schema_version")),
        pack_id=str(reparsed.get("pack_id")),
        pack_version=str(reparsed.get("pack_version")),
        display_name=str(reparsed.get("display_name")),
        capabilities=tuple(sorted(source_capabilities_raw)),
        skill_contract=source_contract,
        cases=source_cases,
    )
    if (
        source_contract != pack.skill_contract
        or source_cases != pack.cases
        or digest_value(source_effective) != pack.identity.digest
    ):
        raise SystemExit("dynamic blind pack source changed after validation")


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser(description="Run two fresh-session Mission Brief blind handoffs.")
    value.add_argument("--source-run", type=Path, required=True)
    value.add_argument("--candidate", type=Path, default=REPOSITORY)
    value.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    value.add_argument("--model", required=True)
    value.add_argument("--judge-model")
    value.add_argument("--codex-bin", type=Path)
    value.add_argument("--timeout", type=int, default=900)
    return value


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    report_path = resolve_report(args.source_run)
    source_report, brief_path, proposal_path = source_artifact(report_path)
    source_candidate = source_report.get("candidate")
    if not isinstance(source_candidate, dict) or not isinstance(source_candidate.get("digest"), str):
        raise SystemExit("source report has no candidate digest")

    output_dir = args.output_dir.expanduser().resolve()
    contract_dir = output_dir / "source-contracts" / report_path.parent.name
    contract_dir.mkdir(parents=True, exist_ok=True)
    pack_path = contract_dir / "dynamic-blind-pack.json"
    pack_path.write_text(
        json.dumps(
            dynamic_pack(
                brief_path.read_text(encoding="utf-8"),
                proposal_path.read_text(encoding="utf-8"),
            ),
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    pack = load_blind_pack(pack_path)
    candidate = args.candidate.expanduser().resolve()
    selected = identify(candidate, pack.skill_contract)
    if selected.digest != source_candidate["digest"]:
        raise SystemExit(
            "candidate drift: source run used "
            f"{source_candidate['digest']}, selected candidate is {selected.digest}"
        )
    codex_bin = (
        args.codex_bin.expanduser().resolve()
        if args.codex_bin
        else Path(shutil.which("codex") or "").resolve()
    )
    if not codex_bin.is_file():
        raise SystemExit("codex executable not found; pass --codex-bin")
    config = RunConfig(
        candidate=candidate,
        eval_pack=pack,
        output_dir=output_dir,
        codex_bin=codex_bin,
        model=args.model,
        judge_model=args.judge_model or args.model,
        judge=True,
        keep_workspaces=True,
        timeout_seconds=args.timeout,
    )
    report = BlindHarnessRunner(config).run("behavior")
    run_dir = output_dir / report.run_id
    write_run_contract(run_dir, report)
    source_binding = {
        "source_report": str(report_path),
        "source_run_id": source_report.get("run_id"),
        "source_case": SOURCE_CASE,
        "candidate_digest": selected.digest,
        "brief_source_path": str(brief_path),
        "proposal_source_path": str(proposal_path),
    }
    (run_dir / "blind-source-binding.json").write_text(
        json.dumps(source_binding, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    manifest = evidence_manifest(run_dir)
    (run_dir / "evidence-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "report": str(run_dir / "report.json"),
                "run_contract": str(run_dir / "run-contract.md"),
                "evidence_manifest": str(run_dir / "evidence-manifest.json"),
                "verdict": report.verdict.value,
                "candidate": asdict(report.candidate),
                "eval_pack": asdict(report.eval_pack),
                "evidence_aggregate": manifest["aggregate_sha256"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    if report.verdict == Verdict.PASSED:
        return 0
    if report.verdict == Verdict.FAILED:
        return 1
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
