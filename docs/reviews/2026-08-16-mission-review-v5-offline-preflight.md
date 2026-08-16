# mission-review v5 offline preflight

Date: 2026-08-16
Result: `PASSED`

No model was called during this preflight.

## Frozen identities

- Candidate bundle digest: `4b2ddf6da0cae0e53ef1eeca4729660c2ca2a8cd78be402967ab4498dd9849e8`
- Candidate runtime files: `SKILL.md`, `agents/openai.yaml`
- Repository HEAD at capture: `bcdd50903b0120d2aea5e06157925a39bdc29df4`
- Runner SHA-256: `5c3d8bce66a338b12515ffbe296e4b7ec6ecdd994b7a1f831b599ffaed522a10`
- Runner and imported harness aggregate: `6b20d2b95dd4a007dbef3463b7d48cf5b64c8f48c487dfbfb869d1e79e2c9bfc`
- Codex CLI: `codex-cli 0.144.5`
- Executor model: `gpt-5.6-sol`

Candidate, cases, fixtures, dispatch prompts, and declared executor permissions remain unchanged.

## Trusted-control-plane boundary

V3 and v4 both showed the same model-transport DNS failure under the outer default command sandbox. The v4 fail-fast runner preserved a one-case `FAILED / NOT_GRADED` suite, complete summary and manifest, no auth material, and no disposable root. Its 42-file manifest and aggregate were independently reproduced.

V5 may run the trusted Codex CLI outside that outer network restriction. This exception exists only so the client can reach the model service. The executor session must still prove a credential-stripped managed permission profile with restricted network, exact workspace/runtime permissions, no source-repository grant or access, and no unexpected case grant.

The root private session must contain exactly one Codex arg0 read entry whose lexical parent is the executor-denied isolated Home's `tmp/arg0`, whose resolved parent matches that directory, and whose name begins `codex-arg0`. The evidence boundary no longer relies on the temporary target's post-execution filesystem type. The executor cannot modify the private Home or root session; multiple, traversal, or unrelated entries still fail.

An independent read-only review accepted this boundary, reproduced the adversarial shape checks, and found no remaining P1 or P2.

## Run boundary

V5 must create a fresh output directory and eight fresh root threads. The runner stops after any failed case. Only a complete eight-case capture with eight unique threads and a valid evidence manifest may proceed to independent semantic grading; no earlier response may be spliced in.
