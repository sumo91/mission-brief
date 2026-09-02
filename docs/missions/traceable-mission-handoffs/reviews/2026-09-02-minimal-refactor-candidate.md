# Minimal refactor release candidate — independent review pending

This record freezes the minimalist Mission Brief candidate submitted for a new independent review. It does not authorize installation. The global runtime remains on the preceding release until the reviewer returns `PASSED` and the installed-runtime gate is rerun.

## Runtime result

- Candidate revision: `9ec1352bb2ed8428238e51009aa0fb3120f7821f`
- Candidate digest: `6c0aba47c2460b303c90304b53b607581fd6d37b41091d1e4893f2424bda21b8`
- Runtime files: `SKILL.md`, `agents/openai.yaml`, `references/mission-zero.md`, and `references/source-fidelity.md`
- Core Skill: 113 lines and 1,513 words
- Mission 0 reference: 52 lines and 498 words
- Source-fidelity reference: 43 lines and 510 words
- Instruction total: 208 lines and 2,521 words

The installed preceding release contains 2,174 words in `SKILL.md` and 777 words in its Mission 0 reference, or 2,951 instruction words total. The candidate therefore reduces always-loaded Skill text by about 30% and total instruction text by about 15%, while moving conditional topology and source-preservation detail behind explicit routing.

## Behavior evidence

The complete candidate run is `evals/runs/mission-brief-minimal/20260902T064747Z-17333756`.

- Eval Pack: `mission-brief-traceability` 1.7.0
- Executor: `gpt-5.6-sol`
- Semantic judge: `gpt-5.4`
- Verdict: 34 of 34 cases `PASSED`
- Evidence aggregate: `734e7045f59a8f2d01fae975c9255e3348f9a270df43142f505be7fd7eac225f`

The release verifier combines structured runtime-read fields with successful path-access events. That evidence shows ordinary cases `c-10000001` and `c-1000001d` opened no reference, the four mixed-source cases opened `references/source-fidelity.md`, and applicable topology cases opened `references/mission-zero.md`.

The dynamic blind run is `evals/runs/mission-brief-minimal-blind/20260902T073922Z-d60d7ccf`.

- Blind pack: `mission-brief-dynamic-blind` 1.1.0
- Verdict: 2 of 2 cases `PASSED`
- Evidence aggregate: `e73cec0e787aefdd200e250840affe41053185520f0825a4faeb293fbeb00dec`
- The traceability-aware reader kept confirmed findings non-binding, did not invent a user authorization gate for representative sample selection, recovered material dependencies and risks, and selected a materially different implementation route.

The synthetic source-preservation baseline remains `evals/runs/mission-brief-synthetic-baseline/20260901T233204Z-e287a235`, with aggregate `86d4f59c6ca5a7eb34e3183683a0e9c95be53b6ef9500022bc3b50dff579d996`. It is labeled synthetic. Exact reproduction of the unavailable historical source exchange remains `INCONCLUSIVE`.

All failed and inconclusive development runs remain under ignored `evals/runs/` paths. They were not deleted or relabeled. They exposed, among other issues, false blind passes, revision-history residue, candidate-route leakage, unsettled authority, an archive-relocation judging error, and one interrupted loader session. Targeted cross-model reruns were used to distinguish instruction gaps from execution variance before the final complete run.

## Eval-contract changes

Eval Pack changes through 1.7.0 made synthetic inputs self-contained and clarified archive relocation. Rubrics were not weakened: the retained artifact must still preserve the completed investigation, while a user-facing absolute link that becomes stale only because the harness relocates the workspace after execution is not treated as evidence loss. The blind verifier now checks every retained rubric and semantic finding rather than trusting only the aggregate verdict.

## Release gate

This command returned `static: PASSED` and `release_evidence: PASSED`:

```sh
python3 evals/scripts/verify_mission_brief_release.py \
  --candidate-run evals/runs/mission-brief-minimal/20260902T064747Z-17333756 \
  --blind-run evals/runs/mission-brief-minimal-blind/20260902T073922Z-d60d7ccf \
  --baseline-run evals/runs/mission-brief-synthetic-baseline/20260901T233204Z-e287a235
```

It verified 26 fixture files, 56 maintained local links, the three evidence aggregates, candidate identity, blind-source binding, exact blind semantic findings, runtime boundaries, progressive disclosure, and the byte-preserved Mission Review migration. It reported `historical_reproduction: INCONCLUSIVE`.

## Independent gate

The read-only reviewer is task `codex://threads/01a05f48-edca-71b0-9269-a3b5aa42cb6e`. It was asked to recheck every prior blocking finding, inspect the 1.4 through 1.7 Eval Pack changes for weakened standards, reproduce the release verifier, and return an explicit `PASSED` or `FAILED`. Installation is prohibited until that result is recorded.
