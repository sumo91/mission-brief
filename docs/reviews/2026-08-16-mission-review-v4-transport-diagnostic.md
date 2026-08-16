# mission-review v4 transport diagnostic

Date: 2026-08-16
Result: `FAILED CAPTURE — NOT RELEASE EVIDENCE`

The fail-fast v4 runner created one fresh root thread, `01a00b05-7fd4-7c02-965d-d786b32ad594`, then stopped automatically.

The Codex model stream disconnected before completion. HTTPS fallback failed DNS lookup, the process exited non-zero, and no structured final response existed. The runner correctly treated the previously unseen transport event as an unknown executor error and wrote `capture_status: FAILED`, an incomplete-suite summary, and a path-addressed evidence manifest. No semantic verdict is available.

The repeated failure under the default outer command sandbox identifies the remaining run condition: the trusted Codex client needs model-transport network access. The executor's shell and tools remain governed separately by the recorded managed profile with restricted network and credential-stripped environment. A later run must request the outer transport exception rather than weakening the executor profile or allowlisting the DNS failure.

V4 also repeated the arg0 lifecycle observation. The private root session retained exactly one read grant under the denied isolated Codex Home at `tmp/arg0/codex-arg0*`; the ephemeral target was not suitable for post-execution filesystem-type validation. Because this grant is emitted by the trusted control plane inside an executor-denied directory, the stable evidence boundary is its unique lexical parent and name in the root session profile. The executor cannot create or alter that private entry.

The v4 directory remains frozen. Its response count is one, its behavior verdict is `NOT_GRADED`, and it must not be joined to any later suite.
