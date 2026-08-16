# Mission Review v6 live final release Closure

Date: 2026-08-16
Verdict: `PASSED`
Release blockers: `P1 = 0`, `P2 = 0`

## Authorization

The frozen `mission-review` candidate is supported by a complete fresh behavior capture, correct external semantic grading, and the retained explicit-invocation Loader evidence. For the exact identities recorded below:

- release: `AUTHORIZED`
- release commit: `AUTHORIZED`
- installation: `AUTHORIZED`
- machine synchronization: `AUTHORIZED`

These authorizations apply only to the frozen candidate with digest `4b2ddf6da0cae0e53ef1eeca4729660c2ca2a8cd78be402967ab4498dd9849e8`. They do not authorize unrelated workspace changes.

## Frozen identities and package boundary

Independent recomputation matched the v6 preflight:

- candidate digest: `4b2ddf6da0cae0e53ef1eeca4729660c2ca2a8cd78be402967ab4498dd9849e8`
- runner SHA-256: `f388d4af362ca89c0162cb41f8731830cc7e7917380b35c46a9a8ef5216cbcdf`
- runner/harness aggregate: `75639ed40200f9b35d3f7fd12eda76732af8db0e32f81b987abc7903438ea9a4`
- Codex CLI SHA-256: `5e29ab10ca1171be158f7335dd6bd8ce1aaf9af1556939db36a5ee338be6f5f2` (`codex-cli 0.144.5`)
- repository HEAD at capture: `bcdd50903b0120d2aea5e06157925a39bdc29df4`

The complete runtime package is exactly two regular files and contains no symlink:

- `mission-review/SKILL.md` — SHA-256 `de1c5f55dad8091c76fead408feb7f5c61d75180890713bbd00d2e0272707cd4`
- `mission-review/agents/openai.yaml` — SHA-256 `44d1e768cc568f072119dcd8e6f3cd7a7c4b5abe2a276660bc98fc1cd04a807e`

`docs/`, `evals/`, cases, fixtures, run archives, grades, diagnostics, manifests, and Closure Reviews are repository evidence, not runtime. They must not be installed or machine-synchronized as part of the Skill.

## Fresh v6 evidence audit

`evals/runs/mission-review-v6/` is a single self-contained run over the complete selected set `mr-001`, `mr-002`, `mr-004`, `mr-005`, `mr-006`, `mr-007`, `mr-008`, and `mr-009`.

Independent hashing found 258 files covered by `evidence-manifest.json`, excluding the manifest itself. The actual relative-path map matched all 258 recorded file hashes, and recomputing the frozen path-plus-file-digest algorithm produced the recorded aggregate:

`2933f2572151654f5aadd49c8b5185c38d79ed85aad1e14cc5ac7907e73c822d`

The suite summary is `capture_status: PASSED`, all eight cases are capture-passed, and the eight root thread IDs are nonempty and unique. For every case I independently checked the preserved result, private root session, dispatch file, profile evidence, injection evidence, before/after manifests, mutation diffs, and cleanup record:

- the dispatch and user-prompt bytes match their preflight SHA-256 identities;
- exactly one dispatch appears in the root session bound to the stdout thread;
- the requested and root-session model are `gpt-5.6-sol`;
- the observed root profile is managed, filesystem-restricted, and network-restricted;
- repository grants, source-repository accesses, source mentions, unexpected grants, and invalid injections are empty;
- each case has one complete `mission-review` injection, a hidden catalog, and no invalid injection;
- runtime and workspace before/after identities match, with empty mutation diffs;
- executor returns are zero, structured finals exist, and the only executor error items are the two exact retained web-search deprecation messages allowed by the frozen runner;
- no case reports an artifact, retains an auth file, or collides with the source auth-file digest;
- all eight disposable roots are absent after cleanup.

The mr-005-only npm controls are present in `[shell_environment_policy.set]`: its cache points under the case temp directory and the update notifier is disabled. The case retains only its required `/opt/homebrew` read grant; the other seven cases receive neither that grant nor the npm controls. Network and source-repository boundaries remain closed.

## Independent semantic Closure

I graded the preserved raw packet or fixture, root response, command JSONL, and retained outputs rather than accepting the summary's deliberately ungraded behavior field.

| Case | Issued verdict | External grade | Independent basis |
|---|---|---|---|
| `mr-001` | `FAILED` | PASS | Both report packages index only eight visual assets while material evidence references contain 53 and 52 uses of unindexed frames. The four unknown paths in each package and missing required validation evidence materially defeat traceability. |
| `mr-002` | `FAILED` | PASS | The delivered search promotes and labels a superseded draft as current while obscuring the authoritative policy; schema/link proxy checks cannot satisfy the operator outcome. |
| `mr-004` | `PASSED` | PASS | The preserved command trace shows `export exp-42 stopped: permission denied` with captured status 17. The PostgreSQL extract and query agree on the stopped export, and all six fixture-manifest hashes recompute exactly. |
| `mr-005` | `PASSED` | PASS | The raw trace follows `cd sample-site` and `npm run preview`, receives a file URL, opens the completed HTML, and identifies `sample-site/dist/index.html` without network or global package installation. |
| `mr-006` | `FAILED` | PASS | No named legal-owner approval exists; the executor preserves the explicit human authority rather than substituting an Agent opinion. |
| `mr-007` | `INCONCLUSIVE` | PASS | Local claims cannot establish the unavailable live-bank acceptance and exactly-once settlement; the response invents neither success nor failure and asks for correlated production evidence. |
| `mr-008` | `FAILED` | PASS | A loopback-hosted cited image is blank without the server, directly contradicting offline visibility; the response reports the material defect without repairing the report. |
| `mr-009` | `INCONCLUSIVE` | PASS | The packet asserts success but supplies no executable export, timing, terminal-failure, or PostgreSQL evidence. The response correctly withholds closure while refusing to turn rejected Kafka/worker/reviewer ideas into requirements. |

External semantic result: `8/8 PASS`. The verdict sequence is `F, F, P, P, F, I, F, I` for `mr-001`, `mr-002`, `mr-004`, `mr-005`, `mr-006`, `mr-007`, `mr-008`, and `mr-009` respectively.

## Explicit-invocation evidence

The v0 Loader archive is relevant because it exercises the same candidate digest `4b2ddf6da0cae0e53ef1eeca4729660c2ca2a8cd78be402967ab4498dd9849e8`. Its frozen three-case evidence aggregate is `f3364ef70d4184aa949722b1305d09cfb53686e694997c9185488e0d48712579`; the two retained summaries still hash to `b04db8d63efead00de66873ec287edcbe4389b8e5c672de1ad568eee67054ef8` and `63264bf6ba62927f7119fc071796377eba023a8b7c3883cf25a3f3bdd6d1a2df`.

I re-opened the three raw private sessions, per-case results, profiles, and injection records:

- ordinary nonexplicit request: zero injections, no catalog entry, isolated Codex Home denied;
- natural-language `Mission Review` mention without `$`: zero injections, no catalog entry, isolated Codex Home denied;
- explicit `$mission-review` request: exactly one complete injection, no invalid injection, candidate staged read-only.

All three have distinct complete threads, `gpt-5.6-sol`, restricted network, unchanged runtime digest, unchanged workspace, and no retained auth file. Current candidate bytes are unchanged from those Loader identities. The manual-invocation controls are also unchanged: `disable-model-invocation: true` remains in `SKILL.md`, while `allow_implicit_invocation: false` and the explicit `$mission-review` default prompt remain in `agents/openai.yaml`.

## Evidence separation

The v3 transport failure, v4 transport failure, and v5 workspace-mutation failure remain diagnostics only. They are not combined with the release evidence. Their retained root thread IDs do not overlap any of the eight v6 threads, and no v3/v4/v5 run path or old thread ID appears in the v6 archive. V6 independently starts and completes all eight cases and seals only its own files in its own 258-file manifest.

## Final decision

No release-blocking candidate defect or evidence-integrity gap remains. The exact two-file candidate identified above is `PASSED` and is authorized for release, release commit, installation, and machine synchronization. Installation and synchronization must use only those two runtime files; repository evidence under `docs/` and `evals/` must remain outside the installed Skill.
