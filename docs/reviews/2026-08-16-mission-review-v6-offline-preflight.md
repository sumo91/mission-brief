# mission-review v6 offline preflight

Date: 2026-08-16
Result: `PASSED`

No model was called during this preflight.

## Frozen identities

- Candidate bundle digest: `4b2ddf6da0cae0e53ef1eeca4729660c2ca2a8cd78be402967ab4498dd9849e8`
- Candidate runtime files: `SKILL.md`, `agents/openai.yaml`
- Repository HEAD at capture: `bcdd50903b0120d2aea5e06157925a39bdc29df4`
- Runner SHA-256: `f388d4af362ca89c0162cb41f8731830cc7e7917380b35c46a9a8ef5216cbcdf`
- Runner and imported harness aggregate: `75639ed40200f9b35d3f7fd12eda76732af8db0e32f81b987abc7903438ea9a4`
- Codex CLI: `codex-cli 0.144.5`
- Executor model: `gpt-5.6-sol`

Candidate, cases, fixtures, prompts, and behavior expectations remain unchanged.

## V5 disposition

V5 established working model transport and captured three passed cases plus a fourth substantive response. The replacement `mr-004` exercised the CLI and returned an evidence-grounded `PASSED` as intended. `mr-005` successfully ran Node/npm, completed the local guide journey, inspected the finished page, and returned `PASSED`, but npm created `.npm` logs and update-notifier state under the executor workspace. The frozen zero-mutation gate correctly failed capture and stopped the suite.

V5 remains `FAILED / NOT_GRADED`. Its four responses, workspace diff, 152-file evidence manifest, auth checks, and cleanup evidence are retained and cannot contribute to v6.

## Runner repair

Only `mr-005` now receives two shell-environment settings:

- `NPM_CONFIG_CACHE=<case disposable temp>/npm-cache`
- `NPM_CONFIG_UPDATE_NOTIFIER=false`

The cache is inside the case's existing exact temp write boundary. No new filesystem or network grant was added. The executor workspace is still compared byte-for-byte before and after review; the runner neither ignores nor deletes mutations before comparison. If npm does not honor the settings, the case fails closed again.

An independent read-only review parsed the resulting TOML, verified that the settings apply only to `mr-005`, reproduced a preview run without changing the sample project, and returned `PASSED` with no P1 or P2.

## Run boundary

V6 must create a new directory and eight new root threads. The trusted Codex client may use model transport, while each executor must independently prove the same restricted managed profile. Any capture failure stops the suite. Only a complete eight-case capture and later independent semantic grading may authorize release.
