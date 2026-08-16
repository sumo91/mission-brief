# mission-review v3 offline preflight

Date: 2026-08-16
Result: `PASSED`

No model was called during this preflight.

## Frozen identities

- Candidate bundle digest: `4b2ddf6da0cae0e53ef1eeca4729660c2ca2a8cd78be402967ab4498dd9849e8`
- Candidate runtime files: `SKILL.md`, `agents/openai.yaml`
- Repository HEAD at capture: `bcdd50903b0120d2aea5e06157925a39bdc29df4`
- Runner SHA-256: `6137c947625f9dc7c5f7231e78c8c6687d178a1ac5b8495f047acf67e7ee270f`
- Runner and imported harness aggregate: `227fc6aaf4f5539719c8d80e210559b81bfbc971199c6009b1e8d920086e4fdb`
- Codex CLI: `codex-cli 0.144.5`
- Executor model: `gpt-5.6-sol`
- Cases: `mr-001`, `mr-002`, `mr-004`, `mr-005`, `mr-006`, `mr-007`, `mr-008`, `mr-009`

## Case repair

The earlier `mr-004` packet contained only prose claiming that reproduction had succeeded. It could not validly test a Skill whose job is to inspect the finished result rather than trust the implementer's completion claim.

The replacement fixture provides an executable CLI, its adopted Mission, a non-authoritative implementer note, a retained PostgreSQL data extract and query transcript, and a six-file hash manifest. Independent checks reproduced stderr `export exp-42 stopped: permission denied`, exit status `17`, matching export/state/reason values in both PostgreSQL evidence files, and all manifest hashes. The expected verdict is not present in the executor workspace.

The semantic adjudicator concluded that the old candidate response was correct and the old case evidence was insufficient. The runtime Skill therefore remains unchanged.

## Runner closure

The runner now:

- grants `/opt/homebrew` read access only to `mr-005`, requires that exact grant to appear in the root managed profile, and rejects any unapproved path grant;
- allows only the frozen Codex shell and exactly one real non-symlink `codex-arg0*` control file beyond the declared case permissions;
- keeps source-repository overlap and observed source access as hard failures;
- labels the untracked candidate's repository revision only as `repository_head_at_capture`;
- accepts exactly the two observed web-search deprecation events and fails capture on any other or malformed executor error;
- retains the existing root thread, dispatch, injection, model, profile, no-mutation, auth-cleanup, private-session, and evidence-manifest gates.

An independent read-only runner review reproduced positive and adversarial permission checks and returned `PASSED` with no remaining finding.

## Run boundary

The stopped v1 diagnostic and admissible v2 capture remain frozen. The v3 run must create a new output directory, eight new root threads, and a complete new evidence manifest. Its runner can establish only capture integrity; semantic and release verdicts require a later independent review.
