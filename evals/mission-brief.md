# Mission Brief external behavior evaluation

This maintainer contract binds the executable Eval Pack in [`mission-brief-pack.json`](./mission-brief-pack.json) to the human-readable behavior in [`../EVALS.md`](../EVALS.md). It is not runtime instruction and must remain inaccessible to evaluation executors.

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
| 11 parent seams | `c-1000000e` |
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

The static Pack contains 30 behavior cases, 3 Loader cases, and 35 turns. The release run adds two fresh-session blind handoffs derived from frozen candidate outputs.

Progressive disclosure is part of the observable runtime contract. Simple cases `c-10000001` and `c-1000001d` must not read either conditional reference. Mixed durable source cases `c-10000016`, `c-10000017`, and `c-1000001e`, plus transient source case `c-10000018`, must read `references/source-fidelity.md`. Because the upstream `runtime_files_read` field records only the single reference named by its v1 Skill contract, the release verifier also derives successful reference reads from retained `access_events`. Parent-child routing remains governed separately by its case assertions.

## Durable run shape

Run evidence lives at `evals/runs/mission-brief/<run-id>/` and includes the platform report, retained Eval Pack and Skill contract, per-case raw turns and filesystem manifests, a generated `run-contract.md`, and `evidence-manifest.json`. Baseline evidence uses a separate run ID bound to `8adf782bf61e7051f9afe14d2e25166790e8bdc3`.

The two dynamic blind runs must retain:

- the exact source Brief and any allowed durable sources;
- the new task or session identity;
- the blind prompt and raw final response;
- the hidden-authoring exclusions applied;
- a semantic grade for contract recovery, source-status recovery, known risks, optional routes, and implementation freedom.

For the traceability-aware handoff, confirmed findings must remain non-binding Reference context unless a cited adopted decision or applicable Authority Source gives them binding effect. The reader must not invent a user decision for a representative sample that the contract leaves to execution. An implementation route passes the independence check only when its controlling mechanism differs materially from the candidate mechanisms preserved in the source. Rewording, reordering, or choosing one of the named candidate routes is not independent.

## Release gate

An independent Closure may return `PASSED` only when all 33 static cases and both dynamic blind cases have durable evidence against one frozen candidate, the suite has no unresolved release-blocking finding, the authentic-source gap is either closed or explicitly makes the historical claim `INCONCLUSIVE`, and no decisive proof depends on `/tmp` or the authoring conversation.
