#!/usr/bin/env python3
"""Run with python3 evals/scripts/test_eval_adaptation.py; no model calls."""
import json
from copy import deepcopy
import tempfile
import tomllib
from pathlib import Path

from run_mission_brief_behavior import (
    configure_evaluation, derived_subset_pack, evidence_manifest,
    isolated_config_with_effort, load_eval_pack, stage_discoverable, recorded_tool_events, REPOSITORY,
)
from run_mission_review_behavior import capture_summary_conditions, make_tree_removable
from verify_mission_brief_release import (
    VerificationError, require_passed, require_candidate_identity, verify_evidence_manifest,
    combine_candidate_reports, apply_semantic_adjudication, sha256,
)


def rejected(function, *args):
    try:
        function(*args)
    except (VerificationError, ValueError, SystemExit):
        return
    raise AssertionError(f"{function.__name__} accepted invalid evidence")


def main():
    passed = {"case_id": "mr-004", "thread_id": "fresh-1", "capture_status": "PASSED"}
    assert all(capture_summary_conditions(["mr-004"], [passed]).values())
    assert not all(capture_summary_conditions(["mr-001", "mr-004"], [passed]).values())
    assert not all(capture_summary_conditions(["mr-004", "mr-004"], [passed, passed]).values())
    assert not all(capture_summary_conditions([], []).values())
    report = {"verdict": "PASSED", "candidate": {"digest": "frozen"},
              "cases": [{"opaque_id": "one", "verdict": "PASSED"}]}
    require_passed(report, {"one"}, "test")
    rejected(require_passed, report, {"one", "missing"}, "test")
    rejected(require_passed, report, set(), "test")
    rejected(require_passed, {**report, "cases": [{"opaque_id": "one", "verdict": "NOT_GRADED"}]}, {"one"}, "test")
    require_candidate_identity(report, "frozen", "test")
    rejected(require_candidate_identity, report, "changed", "test")
    current = {"skill_contract": {}, "cases": [
        {"opaque_id": name, "fixture_files": {"input": name}, "rubric": ["same meaning"]}
        for name in ("one", "two")
    ]}

    def group(index):
        case = current["cases"][index]
        pack = {"identity": {"digest": case["opaque_id"]}, "skill_contract": {}, "cases": [case]}
        result = {"verdict": "PASSED", "candidate": {"digest": "frozen"},
                  "eval_pack": {"digest": case["opaque_id"]}, "harness_identity": "same",
                  "harness_version": "1", "codex_cli_version": "1", "executor_model": "model", "semantic_judge_model": "model",
                  "execution_settings": {"requested_executor_model": "model", "requested_judge_model": "model",
                      "requested_reasoning_effort": "medium", "adapter_flags": ["--json"], "approval_policy": "never",
                      "executor_network": "denied", "filesystem_profile": "isolated", "shell_environment": "isolated",
                      "timeout_seconds": 900, "semantic_judging": True},
                  "cases": [{"opaque_id": name, "verdict": "PASSED"}
                            for name in (case["opaque_id"], "i-0e519dab")]}
        return Path(case["opaque_id"]), result, pack

    first, second = group(0), group(1)
    merged, sources = combine_candidate_reports([first, second], current, "frozen")
    assert len(merged["cases"]) == 3 and set(sources) == {"one", "two"}
    rejected(combine_candidate_reports, [first], current, "frozen")
    rejected(combine_candidate_reports, [first, second, first], current, "frozen")
    rejected(combine_candidate_reports, [first, second], current, "different")
    changed = deepcopy(second)
    changed[2]["cases"][0]["fixture_files"]["input"] = "changed"
    rejected(combine_candidate_reports, [first, changed], current, "frozen")
    changed = deepcopy(second)
    changed[1]["harness_identity"] = "different"
    rejected(combine_candidate_reports, [first, changed], current, "frozen")
    changed = deepcopy(second)
    changed[1]["verdict"] = "FAILED"
    rejected(combine_candidate_reports, [first, changed], current, "frozen")
    for field in ("executor_model", "codex_cli_version", "harness_identity", "execution_settings"):
        incomplete = deepcopy([first, second])
        for _, result, _ in incomplete:
            result.pop(field)
        rejected(combine_candidate_reports, incomplete, current, "frozen")
    incomplete = deepcopy([first, second])
    for _, result, _ in incomplete:
        result["execution_settings"].pop("requested_reasoning_effort")
    rejected(combine_candidate_reports, incomplete, current, "frozen")
    updated_pack = deepcopy(current)
    updated_pack["cases"][0]["fixture_files"]["input"] = "corrected input"
    replacement = deepcopy(first)
    replacement = (Path("replacement"), replacement[1], replacement[2])
    replacement[2]["cases"][0] = updated_pack["cases"][0]
    obsolete = deepcopy(first)
    obsolete[1]["verdict"] = obsolete[1]["cases"][0]["verdict"] = "FAILED"
    reused, sources = combine_candidate_reports([obsolete, second, replacement], updated_pack, "frozen", True)
    assert reused["verdict"] == "PASSED" and sources["one"] == "replacement/report.json"
    assert obsolete[1]["verdict"] == "FAILED"
    rejected(combine_candidate_reports, [obsolete, second], updated_pack, "frozen", True)
    rejected(combine_candidate_reports, [first, second, first], current, "frozen", True)
    rejected(combine_candidate_reports, [obsolete, second], current, "frozen", True)
    obsolete[1]["consequential_uncertainty"] = ["thread reused"]
    rejected(combine_candidate_reports, [obsolete, second, replacement], updated_pack, "frozen", True)
    with tempfile.TemporaryDirectory() as name:
        root = Path(name)
        subset = derived_subset_pack(REPOSITORY / "evals/mission-align-pack.json", root, ["a-1000000d"])
        assert [c.opaque_id for c in load_eval_pack(subset).cases] == ["a-1000000d"]
        rejected(derived_subset_pack, REPOSITORY / "evals/mission-align-pack.json", root, ["missing"])
        configure_evaluation("medium")
        path = isolated_config_with_effort(isolated_home=root, workspace=root / "workspace",
            runtime_bundle=None, temp_dir=root / "tmp", model="gpt-6-astra")
        config = tomllib.loads(path.read_text())
        assert config["model_reasoning_effort"] == "medium"
        assert config["approval_policy"] == "never"
        assert config["permissions"]["eval-executor"]["network"]["enabled"] is False
        isolated = root / "isolated/codex-home"
        isolated.mkdir(parents=True)
        contract = load_eval_pack(REPOSITORY / "evals/mission-align-pack.json").skill_contract
        staged = stage_discoverable(REPOSITORY / "mission-align", isolated, contract)
        assert not staged.is_relative_to(isolated)
        assert (isolated / "skills/mission-align").resolve() == staged
        assert (staged / "SKILL.md").read_bytes() == (REPOSITORY / "mission-align/SKILL.md").read_bytes()
        make_tree_removable(root)
        sessions = root / "codex-sessions"
        sessions.mkdir()
        (sessions / "root.jsonl").write_text("\n".join(json.dumps(value) for value in [
            {"type": "response_item", "payload": {"type": "message", "role": "developer", "content": "not tool evidence"}},
            {"type": "response_item", "timestamp": "now", "payload": {"type": "custom_tool_call_output", "output": "observed CSV row"}},
        ]) + "\n")
        events = recorded_tool_events(root)["codex-sessions/root.jsonl"]
        assert len(events) == 1 and events[0]["line"] == 2
        assert events[0]["payload"]["output"] == "observed CSV row"
        (root / "evidence-manifest.json").write_text(json.dumps(evidence_manifest(root)))
        verify_evidence_manifest(root)
        path.write_text("tampered")
        rejected(verify_evidence_manifest, root)
        run = root / "adjudicated-run"
        run.mkdir()
        original = {"verdict": "FAILED", "candidate": {"digest": "frozen"}, "cases": [{
            "opaque_id": "one", "suite": "behavior", "verdict": "FAILED",
            "semantic_findings": [{"criterion": "same meaning", "verdict": "FAILED"}],
            "turns": [{"verdict": "PASSED", "deterministic_findings": [{"verdict": "PASSED"}]}]}]}
        (run / "report.json").write_text(json.dumps(original))
        (run / "evidence-manifest.json").write_text(json.dumps(evidence_manifest(run)))
        review = root / "review.md"
        review.write_text("Independent review of the actual artifact against the original criterion.")
        decision = {"run_root": str(run), "report_sha256": sha256(run / "report.json"),
            "candidate_digest": "frozen", "evidence_aggregate_sha256": verify_evidence_manifest(run),
            "reviewer_context": "fresh-review", "review_evidence_files": {str(review): sha256(review)},
            "case_id": "one", "independent_verdict": "PASSED",
            "criteria": [{"criterion": "same meaning", "verdict": "PASSED", "reason": "actual artifact"}]}
        decision_path = root / "decision.json"
        decision_path.write_text(json.dumps(decision))
        accepted, receipt = apply_semantic_adjudication(run, original, current, decision_path)
        assert accepted["verdict"] == "PASSED" and original["verdict"] == "FAILED"
        assert receipt["original_verdict"] == "FAILED"
        rejected(apply_semantic_adjudication, run, accepted, current, decision_path)
        for field, value in (("report_sha256", "changed"), ("candidate_digest", "changed"),
                             ("criteria", []), ("reviewer_context", "")):
            decision_path.write_text(json.dumps({**decision, field: value}))
            rejected(apply_semantic_adjudication, run, original, current, decision_path)
        decision_path.write_text(json.dumps(decision))
        broken = deepcopy(original)
        broken["cases"][0]["turns"][0]["deterministic_findings"][0]["verdict"] = "FAILED"
        rejected(apply_semantic_adjudication, run, broken, current, decision_path)
        rejected(apply_semantic_adjudication, run,
                 {**original, "consequential_uncertainty": ["executor thread reused across cases"]},
                 current, decision_path)
        review.write_text("changed")
        rejected(apply_semantic_adjudication, run, original, current, decision_path)
    configure_evaluation(None)
    print("PASS: subset capture, missing/ungraded cases, candidate identity, effort config and evidence tampering")


if __name__ == "__main__":
    main()
