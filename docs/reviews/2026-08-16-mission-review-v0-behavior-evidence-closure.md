# mission-review v0 behavior evidence closure

Date: 2026-08-16
Result: `PASSED`

## Decision

The frozen `mission-review` candidate is supported by all nine active behavior scenarios. Eight fresh, context-clean review executors produced materially correct Closure Reviews, and three isolated Loader sessions established explicit invocation without implicit loading. An independent grading Agent found no release-blocking candidate defect.

This closes the authorized behavior-test stage. It does not authorize the separate release Closure, commit, installation, or machine synchronization.

## Frozen candidate

- Runtime files: `mission-review/SKILL.md`, `mission-review/agents/openai.yaml`
- Runtime aggregate: `2bc5a2359c90071e8cfedc647ac993479e0346148c801c08beadd7e61f9f5acc`
- Loader-harness digest: `4b2ddf6da0cae0e53ef1eeca4729660c2ca2a8cd78be402967ab4498dd9849e8`
- Repository baseline: `bcdd50903b0120d2aea5e06157925a39bdc29df4`
- Package shape: two regular runtime files, no symlinks
- Skill body: 78 lines, 779 English words

The two digest values use different frozen algorithms: the repository aggregate hashes sorted `shasum` lines, while the Loader digest hashes each relative path, a null separator, and the file digest bytes.

## Closure Review behavior

Every executor started with `fork_turns="none"` and received only the candidate Skill plus one raw contract-and-artifact packet. Maintainer expectations, suspected defects, intended fixes, prior outputs, and this review were absent.

| Scenario | Issued verdict | External grade | Decisive behavior |
|---|---|---|---|
| Real standard-report fixture | `FAILED` | PASS | Exercised business reading and found material claim-to-evidence breaks rather than trusting package shape. |
| Authority/proxy evidence | `FAILED` | PASS | Preserved repository authority and rejected structural proxies for the reversed user result. |
| Faithful nonliteral delivery | `PASSED` | PASS | Accepted changed wording and architecture because the adopted result and boundaries remained true. |
| First-run guide journey | `PASSED` | PASS | Ran the documented journey and inspected the result without shifting ordinary validation to a human. |
| Explicit human approval | `FAILED` | PASS | Preserved the named human authority instead of simulating approval. |
| Unobtainable external result | `INCONCLUSIVE` | PASS | Separated reproducible local proof from an unavailable live-bank fact. |
| Broken offline report | `FAILED` | PASS | Reproduced the failure and reported it without repairing the artifact. |
| Chat-only adopted contract | `PASSED` | PASS | Recovered the authoritative conversation without forcing a formal Brief or adopting rejected routes. |

The eight response-file aggregate is `0fb1917978c2cac6ff230ceba1e9d313c3514c3e6e6aa9d6202c8cf6f8df50ff`.

## Invocation behavior

Three fresh sessions staged the candidate read-only inside disposable Codex Homes. The executor model resolved as `gpt-5.6-sol`; private session, configuration, permission profile, JSONL, final response, and parse evidence were retained without auth files.

| Input | Injection | Catalog | Candidate permission | Result |
|---|---:|---|---|---|
| Ordinary review request | 0 | hidden | none; Codex Home denied | PASS |
| Natural-language `Mission Review` mention, no `$` | 0 | hidden | none; Codex Home denied | PASS |
| Explicit `$mission-review` request | 1 complete, 0 invalid | hidden | staged candidate read-only | PASS |

All three sessions observed the managed restricted-network profile, correct named model route, complete parseable evidence, unchanged candidate identity, and unchanged test workspace. The explicit session used the injected Skill; the two nonexplicit sessions did not receive its directory entry, path, body, or metadata.

- Two-case Loader summary SHA-256: `b04db8d63efead00de66873ec287edcbe4389b8e5c672de1ad568eee67054ef8`
- Named-nonexplicit summary SHA-256: `63264bf6ba62927f7119fc071796377eba023a8b7c3883cf25a3f3bdd6d1a2df`
- Three-case Loader evidence aggregate: `f3364ef70d4184aa949722b1305d09cfb53686e694997c9185488e0d48712579`

## Evidence limits

The collaboration executor archive retains final answers rather than complete tool transcripts. This limits mechanical replay for synthetic cases, although the real report and guide fixtures were independently reproduced and all executors disclosed consequential evidence limits.

The Loader evidence establishes behavior for the tested product and permission configuration, not `disable-model-invocation` as an isolated causal variable. Each Loader condition has one sample. Named model evidence establishes the selected route, not independent authentication of backend weights. Disposable workspaces were deleted after preservation, so zero-write findings rely on retained before/after hashes and command traces.

These limits do not contradict any observed scenario and did not create an unjustified conclusive verdict.

## Evidence index

- Mission contract: `docs/missions/reliable-mission-review/brief.md`
- Offline preflight: `docs/reviews/2026-08-16-mission-review-v0-offline-preflight.md`
- Maintainer evaluation contract: `evals/mission-review.md`
- Behavior run contract: `evals/runs/mission-review-v0/run-contract.md`
- Independent behavior grade: `evals/runs/mission-review-v0/grade.md`
- Raw responses and Loader evidence: `evals/runs/mission-review-v0/`

The next gate is an independent release Closure over the frozen candidate, contract, preflight, raw behavior evidence, and this behavior closure. Release actions remain closed until that separate review is explicitly authorized and returns a passing decision.
