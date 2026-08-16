# mission-review v0 offline preflight

Date: 2026-08-16
Result: `PASSED` offline; behavioral model-run gate remains `CLOSED` pending explicit authorization.

## Frozen inputs

- Repository baseline: `bcdd50903b0120d2aea5e06157925a39bdc29df4`
- Mission contract: `docs/mission-briefs/mission-review-mvp.md`
- Mission contract SHA-256: `e564f5677c4d3c800d2629d5ec10141ad3d4b1fd06f074c64ad68e16aa90d723`
- Candidate runtime aggregate: `2bc5a2359c90071e8cfedc647ac993479e0346148c801c08beadd7e61f9f5acc`
- Maintainer eval contract SHA-256: `fcab38b66457f16da89897105ccf329679ac3bd56440899ab4cd63c8bf618b40`
- Raw synthetic case-packet aggregate: `bdd54dfbbb6ee361457f909b2e65e8061b9ee63e414ec478739d09f029dbcf01`
- `mr-001-standard-report-v2` fixture aggregate: `7133b6081a2c9b16a2be35ef48859b35771d70f465485d5e1fd3f1678d92c4bc`
- `mr-005-guide-journey` fixture aggregate: `d18a1969e70e72c1a59b7209a7a1d1c26cda4fb18bf471a17fc5768c0713dcde`

The aggregate algorithm hashes every regular file, sorted by path under the repository root, then hashes the resulting `shasum -a 256` lines.

## Runtime package

The candidate contains exactly two regular files and no symlinks:

| File | SHA-256 |
|---|---|
| `mission-review/SKILL.md` | `de1c5f55dad8091c76fead408feb7f5c61d75180890713bbd00d2e0272707cd4` |
| `mission-review/agents/openai.yaml` | `44d1e768cc568f072119dcd8e6f3cd7a7c4b5abe2a276660bc98fc1cd04a807e` |

Frontmatter and interface YAML parse successfully. The Skill name and directory agree. Manual invocation is expressed in both runtime surfaces:

- `disable-model-invocation: true`
- `policy.allow_implicit_invocation: false`

The default UI prompt explicitly invokes `$mission-review`.

## Attention and rule audit

`SKILL.md` is 78 lines and 779 English words. It has no bundled reference branch, script, asset, placeholder, trailing whitespace, or line longer than 240 characters.

The main path is one outcome-review sequence:

1. recover the adopted promise;
2. exercise the finished result;
3. judge material fulfillment;
4. write the Closure Review.

The output guidance requires legible information rather than fixed headings. The runtime text contains no fixed question count, clause taxonomy, scoring system, approval state machine, case-specific blacklist, or minimum finding quota.

Attention signals recorded for later comparison:

- `only`: 4
- `exactly`: 0
- `do not`: 3
- `must`: 0

The candidate positively assigns feasible validation to the reviewing Agent. A fresh child Agent is conditional evidence, not a mandatory approver. Human participation is limited to an explicitly contracted human decision or an experience an Agent cannot supply.

## Eval boundary

`evals/mission-review.md` contains nine maintainer scenarios. They grade external behavior and explicitly leave headings, wording, inspection order, check count, and child-Agent use free. Six synthetic executor packets live separately under `evals/cases/mission-review/` and contain no expected verdict or repair direction.

The scenarios cover manual invocation, contract authority, a real report-reading journey, faithful nonliteral delivery, Agent-owned experiential evidence, explicit human authority, unobtainable external evidence, review-versus-repair, and a recoverable chat-only contract.

The real `mr-001-standard-report-v2` fixture contains nine files. Its manifest names eight inputs and deliverables; all eight recorded file hashes independently match. The manifest itself is included in the frozen fixture aggregate.

The local `mr-005-guide-journey` fixture contains eight files. Its manifest names seven contract, guide, claim, request, project, script, and output files; all seven recorded hashes match. Running `npm run preview` from the sample project exits successfully and prints the existing generated page's `file://` URL. This fixture lets a fresh reviewer exercise a reader journey rather than merely discuss whether a human should do it.

Executor prompts must receive raw contract, artifacts, implementer evidence, and applicable authority only. Expected verdicts, suspected defects, intended fixes, and this preflight remain outside executor context.

## Existing Skill preservation

The released `mission-brief` runtime files have no worktree diff. Their SHA-256 values remain:

| File | SHA-256 |
|---|---|
| `SKILL.md` | `5972cc3b55e77025e8f36311ff1b150d5cd2d91c235b91e149571ce2bc61d667` |
| `agents/openai.yaml` | `2bc07b45b4e4935d06c103f54292359b50383dc1452eb9b1d0f9c1111194d465` |
| `references/mission-zero.md` | `60268a603b99805f00cce7b28483fa8f3ade78991abd79cbd6d0d3b2e30f21e4` |

No candidate or maintainer file has been installed into an Agent runtime directory.

## Validator note

The bundled `quick_validate.py` exits on `disable-model-invocation` because its allowed-key table predates the current user-invoked Skill mechanism. The same mechanism is required by the active `writing-for-agents` instructions and is used by the released, Loader-validated `mission-brief`.

This preflight therefore records the validator incompatibility rather than removing manual-invocation metadata. Independent YAML parsing, exact runtime shape checks, and the paired `openai.yaml` policy all pass. Loader behavior remains to be proven in a fresh run.

## Gate decision

The candidate is eligible for fresh behavioral testing under the frozen identities above. This preflight does not predict model behavior and does not authorize model calls, candidate edits, commits, installation, or synchronization.

Any runtime or eval change creates a new identity and requires a new offline preflight before behavioral evidence can be attributed to it.
