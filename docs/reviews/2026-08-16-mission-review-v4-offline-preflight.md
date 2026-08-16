# mission-review v4 offline preflight

Date: 2026-08-16
Result: `PASSED`

No model was called during this preflight.

## Frozen identities

- Candidate bundle digest: `4b2ddf6da0cae0e53ef1eeca4729660c2ca2a8cd78be402967ab4498dd9849e8`
- Candidate runtime files: `SKILL.md`, `agents/openai.yaml`
- Repository HEAD at capture: `bcdd50903b0120d2aea5e06157925a39bdc29df4`
- Runner SHA-256: `fe26e5764ea3da3694283a7d021b4c450049e94494064b479b41d5c9887a4b95`
- Runner and imported harness aggregate: `b2b57ec7c2c9f5f69e1e51de6504890ff32d4186678b4fe9e9d2dc7d3832b161`
- Codex CLI: `codex-cli 0.144.5`
- Executor model: `gpt-5.6-sol`

The candidate, cases, prompts, fixtures, and declared permissions are unchanged from the passed v3 offline preflight.

## Diagnostic disposition

The v3 live attempt is retained separately as a partial diagnostic and cannot contribute a response to v4. Its first model stream disconnected before a final response and then failed DNS during HTTPS fallback. The unknown error correctly failed capture. The operator interrupted the runner after it had begun staging the next case; no second response was retained.

The diagnostic also established that the Codex client may remove its temporary arg0 control file before post-execution profile inspection. The frozen v4 runner still requires exactly one permission entry with the exact isolated arg0 parent and `codex-arg0*` name. If the entry still exists on disk it must be a regular non-symlink file; disappearance after execution is accepted. Directories, symlinks, malformed paths, unexpected grants, and multiple arg0 entries fail the boundary.

The runner now stops automatically after any failed case capture and writes an incomplete-suite failure summary and manifest. It cannot continue spending or accidentally present a partial suite as complete.

An independent read-only review reproduced the positive and adversarial boundary cases, verified v3 auth and temporary-root cleanup, and returned `PASSED` with no remaining finding.

## Run boundary

V4 must use a new output directory and eight new root threads. Only `capture_status: PASSED`, a complete eight-case set, eight unique root threads, and a valid evidence manifest allow later independent semantic grading. The capture runner itself cannot issue a behavior or release verdict.
