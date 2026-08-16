# mission-review v1 auditable runner preflight

Date: 2026-08-16
Result: `PASSED`

No model was called during this preflight.

## Frozen scope

- Candidate digest: `4b2ddf6da0cae0e53ef1eeca4729660c2ca2a8cd78be402967ab4498dd9849e8`
- Candidate runtime files: `SKILL.md`, `agents/openai.yaml`
- Candidate source aggregate: `2bc5a2359c90071e8cfedc647ac993479e0346148c801c08beadd7e61f9f5acc`
- Runner: `evals/scripts/run_mission_review_behavior.py`
- Runner SHA-256: `7a3b4c500033438e8f4de1057131a526c50a3901686d2be29072d1be4cce42ac`
- Imported runner/harness aggregate: `5373f88ece117e522fdf36eb499b76135a4f93200b249e9b7a40ba535812393c`
- Codex CLI: `codex-cli 0.144.5`
- Requested model: `gpt-5.6-sol`
- Cases: `mr-001`, `mr-002`, `mr-004`, `mr-005`, `mr-006`, `mr-007`, `mr-008`, `mr-009`

## Closed findings

Independent static review confirmed that the runner now fails capture when any root permission grants source-repository access, any recorded command accesses the source repository, or any private session contains the repository source path.

Each stdout thread ID must bind to exactly one private `session_meta.id`. That root session must contain the exact dispatch once, the requested model, the managed restricted-network profile, and one complete root-only candidate injection. Child sessions cannot satisfy these root checks by aggregation.

The suite requires all eight cases and eight unique thread IDs. Candidate runtime and executor workspace identities are recorded before and after execution, with diffs and full input/final snapshots. Raw and parsed JSONL, stdout, stderr, private sessions, Codex outputs, configuration, profile, dispatch, access events, and invocation evidence are retained.

No auth file may enter retained evidence or share a full-file digest with retained evidence. The disposable root must be removed and its removal verified. Runner, imported harness, schema, CLI binary/version, flags, argv, candidate, inputs, and dispatch hashes are frozen. The completed run writes a path-addressed SHA-256 evidence manifest.

The first live diagnostic exposed two runner-only defects before a complete suite existed: cleanup could not remove read-only staged directories, and a parsed `//` token was overclassified as repository access. The replacement restores owner-write only on real nodes inside the disposable tree, skips symlinks, then removes and verifies the root. Command access now requires a path located within the repository, while permission grants still reject any readable ancestor that would expose it. The stopped diagnostic is preserved as `mission-review-v1` and cannot be joined to this fresh run.

## Verdict boundary

`capture_status: PASSED` means only that execution and evidence preservation met the frozen integrity conditions. The runner always leaves `behavior_verdict: NOT_GRADED`.

No semantic or release `PASSED` can originate from this runner. A separate reviewer must judge the frozen responses against the raw contracts and artifacts after evidence capture is complete.
