# Mission Brief external behavior evaluation

This maintainer contract binds the executable Eval Pack in [`mission-brief-pack.json`](./mission-brief-pack.json) to the human-readable behavior in [`../EVALS.md`](../EVALS.md). It is not runtime instruction and must remain inaccessible to evaluation executors.

Select validation according to the shared [default policy](../EVALS.md#default-validation-policy). The matrix is a selectable case bank.

## Candidate and source identity

Each run must record the exact four-file Mission Brief runtime digest, Git revision when available, Eval Pack digest, executor and judge model identities, isolation result, and complete evidence aggregate. The runtime is `SKILL.md`, UI metadata, and the two conditionally loaded references; maintainer files remain outside it. A Git revision that does not include a dirty candidate is insufficient on its own; the runtime digest is authoritative for the evaluated bundle. The repository runner extends the platform judge packet with a complete final workspace-directory inventory and binds that extension into the recorded harness identity.

The historical regression source set in [`fixtures/mb-000-original-feedback-regression/`](./fixtures/mb-000-original-feedback-regression/) is authentically incomplete, so exact historical reproduction is `INCONCLUSIVE` until the missing originals are supplied. The executable baseline is explicitly a synthetic source-preservation case: it may compare behavior at the historical revision, but cannot close or stand in for the unavailable four-artifact conversation.

## Executable matrix

| EVALS scenario | Executable case |
|---|---|
| 1 explicit-only invocation | `l-20000001`, `l-20000002`, `l-20000003` |
| 2 small result | `c-10000001` |
| 3 implementation item | `c-10000002` |
| 4 settled write / consequential wait | `c-10000003`, `c-10000004` |
| 5 discussion is not contract | `c-10000005` |
| 6 authority conflict | `c-10000006` |
| 7 evidence proportionality | `c-10000007`, `c-10000008` |
| 8 experiential evidence | `c-10000009` |
| 9 proxy checks | `c-1000000a` |
| 10 result topology variants | `c-1000000b`, `c-1000000c`, `c-1000000d` |
| 11 Parent Mission seams | `c-1000000e` |
| 12 parent continuity variants | `c-1000000f`, `c-10000010` |
| 13 safely discoverable unknowns | `c-10000011` |
| 14 current contract | `c-10000012` |
| 15 output location and commission identity | `c-10000013`, `c-10000014` |
| 16 contract-only blind handoff | dynamic blind run `contract-only` |
| 17 final-plan fidelity | `c-10000015` |
| 18 detailed findings | `c-10000016` |
| 19 mixed authority | `c-10000017` |
| 20 temporary context | `c-10000018` |
| 21 known findings / safe discovery | `c-10000019` |
| 22 storage topology variants | `c-1000001a`, `c-1000001b`, `c-1000001c` |
| 23 simple Mission ceremony | `c-1000001d` |
| 24 traceability-aware blind handoff | dynamic blind run `traceability-aware` |
| 25 irrelevant bulk | `c-1000001e` |
| 12 explicit preservation choice still pending | `c-1000001f` |
| 26 coupled ambiguity and return / cancellation | `c-10000020`, `c-10000021`; optional Align availability comparison |
| Current authorization and compatibility amendments | `c-10000022`; fresh recovery in `h-40000003` |
| Reference instructions do not grant authority | `c-10000023` |
| Implicit alignment discovery with Brief still hidden | `l-20000004`, with Align staged |

Case `c-1000000f` retains an older `Mission 0` fixture title to exercise existing Brief input; current prompts use Parent Mission.

The static Pack contains 35 behavior cases, 4 Loader cases, and 45 turns. Three optional fresh-session blind handoffs examine contract recovery, traceability and amended authorization/compatibility. Select them when those handoff properties are in question; a full-coverage claim derives its cases from the frozen Pack.

The runtime's handoff-readiness check is an authoring criterion, not evidence that an independent reader was run. Real execution is evaluated separately with [frozen local tasks](mission-handoff-execution.json) and [the existing-harness chain entrypoint](scripts/run_mission_handoff_execution.py). The chain compares commissioning variants while keeping the executor and Review configuration fixed; it does not measure Review against a minimal-review control.

Ordinary behavior cases judge the resulting commission, source fidelity and handoff. Reference-read observations remain available for a specific progressive-disclosure or cost investigation; reading a different sufficient path is not by itself a failed outcome. Loader cases retain explicit invocation and reference assertions. File-count assertions remain where they represent a no-write boundary or an explicitly tested storage topology, rather than a general preference for a single file.

## Durable run shape

Run evidence lives at `evals/runs/mission-brief/<run-id>/` and includes the platform report, retained Eval Pack and Skill contract, per-case raw turns and filesystem manifests, a generated `run-contract.md`, and `evidence-manifest.json`. Comparative baseline evidence uses its own run ID and names the revision actually compared. The old `8adf782bf61e7051f9afe14d2e25166790e8bdc3` baseline belongs to the historical full-release protocol.

The dynamic blind runs must retain:

- the exact source Brief and any allowed durable sources;
- the new task or session identity;
- the blind prompt and raw final response;
- the hidden-authoring exclusions applied;
- a semantic grade for contract recovery, source-status recovery, known risks, optional routes, and implementation freedom.

For the traceability-aware handoff, confirmed findings remain Reference context unless adopted authority gives them binding effect. The reader must not invent a user decision for a representative sample left to execution. Route freedom permits a source candidate when current evidence supports it. The blind prompt also supplies a clearly hypothetical incompatible environment: the reader must change the route while preserving the contract, without treating that hypothesis as a new current fact or source advice as authority. Independence is established by fresh context and restricted inputs, not novelty of mechanism.

## Completion

Apply the shared validation policy and state the scope supported by the retained evidence. Selected-case checks do not imply full-suite coverage, and handoff recovery does not imply actual implementation. Full suites, independent Closure and cross-Skill coverage are available when a specific change calls for them.
