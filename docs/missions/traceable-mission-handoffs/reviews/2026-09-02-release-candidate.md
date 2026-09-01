# Release candidate evidence — independent review pending

This record freezes the evidence submitted to the final independent Mission Review. It is not release authority by itself. Global runtime synchronization remains prohibited until a new Codex task inspects this candidate and returns an evidence-supported `PASSED`.

## Frozen runtime

- Repository: `/Users/admin/Documents/Codex/MissionBrief`
- Branch at evidence closure: `codex/mission-brief-traceability-revision`
- Evidence-closure commit before this record: `2ab5bc9d81edf1e40421584d4ccbfe9db4f1098e`
- Mission Brief runtime files: `SKILL.md`, `agents/openai.yaml`, `references/mission-zero.md`
- Mission Brief runtime digest: `9f88759cb801a84890cf2a6f5d04dd8a6fca8fd17dcebe95d966742ecec7b236`
- The full candidate run recorded runtime revision `eb32289fd0e0469ef3113268cda577b6b26e8ca7`. The later commits through `2ab5bc9` change only blind-evaluation infrastructure; `git diff --quiet eb32289 -- SKILL.md agents/openai.yaml references/mission-zero.md` exits `0`.
- Mission Review runtime files remain exactly `mission-review/SKILL.md` and `mission-review/agents/openai.yaml`, with SHA-256 values `7efd502d167b0bfbe5c5451a7fa93f91aab59f53f1ea97bd67343033509c46ff` and `44d1e768cc568f072119dcd8e6f3cd7a7c4b5abe2a276660bc98fc1cd04a807e` respectively.

## Evidence coordinates

### Historical baseline

- Run: `/Users/admin/Documents/Codex/MissionBrief/evals/runs/mission-brief-baseline/20260901T091754Z-5b01d157`
- Candidate revision: `8adf782bf61e7051f9afe14d2e25166790e8bdc3`
- Candidate runtime digest: `62a57c13594d2c31eb3fca0cddc05427f25418e30b480623343923157e178eff`
- Eval Pack digest: `121531aad41290add92c2de371a45c40dc21e4c2fff131825e5caf7257d95869`
- Evidence aggregate: `ffcb9e1c61dff5b393d55a1257cd1ba3f7b38bfb96f9e33673c8eb7a3dd81d22`
- Result on the strongest available synthetic regression input: `PASSED`.
- Exact historical reproduction: `INCONCLUSIVE`. The authentic detailed proposal, first generated Brief, revised generated Brief, and exact conversion request are unavailable; `evals/fixtures/mb-000-original-feedback-regression/manifest.json` records that source gap. The authentic user feedback remains evidence that the original defect occurred, but the missing inputs were not reconstructed or mislabeled as originals.

### Full frozen-candidate evaluation

- Run: `/Users/admin/Documents/Codex/MissionBrief/evals/runs/mission-brief/20260901T165428Z-365cc4e5`
- Verdict: `PASSED`
- Candidate runtime digest: `9f88759cb801a84890cf2a6f5d04dd8a6fca8fd17dcebe95d966742ecec7b236`
- Eval Pack: `mission-brief-traceability` version `1.3.5`
- Eval Pack digest: `c5f5330d6510b5040079101c475a5618ea500ae04299d6e0aa049bb437f54259`
- Evidence aggregate: `ccbe5beecc91c12abf89cb85f4c77762014af9184ac1f0cfb9c7292f11cf3f0a`
- Coverage: 30 semantic behavior cases, three loader cases, and isolation; every case passed with no consequential uncertainty.

### Dynamic blind handoffs

- Run: `/Users/admin/Documents/Codex/MissionBrief/evals/runs/mission-brief-blind/20260901T173618Z-a2e490b4`
- Verdict: `PASSED`
- Source authoring run: `20260901T165428Z-365cc4e5`, case `c-10000016`
- Candidate runtime digest: `9f88759cb801a84890cf2a6f5d04dd8a6fca8fd17dcebe95d966742ecec7b236`
- Dynamic Eval Pack digest: `15d4fccfe3c4893d4e084b2bfd64a3d2e3409acc3b8eb6cb8357f10224162073`
- Harness identity: `ae62176c06176a582dfb9651d2097bf12d087e51fa532c49c3f517bb1dcd566a`
- Evidence aggregate: `fd2fa5606bc5b95f3d48939a8dfe92910d907c0606b7d546ce8395b2711d1ca2`
- Contract-only reader: all three semantic criteria passed; the trace records zero runtime reads, zero skill injections, and zero workspace changes.
- Traceability-aware reader: all three semantic criteria passed; it recovered both shared consumers, importer recreation and the distinct stale entry points, then selected a positive distribution allowlist rather than any preserved candidate mechanism. The trace again records zero runtime reads, zero skill injections, and zero workspace changes.

The upstream v1 Eval Pack schema normally couples private semantic rubrics to required Skill invocation. `evals/scripts/run_mission_brief_blind.py` therefore applies a narrow, hashed adapter for these two cases only: it preserves the platform parser, isolated runner, deterministic checks, semantic judge and evidence writer, while locally verifying that invocation and runtime-reference access are forbidden. The adapter source is included in the reported harness identity.

## Release gate

The following command returned `static: PASSED` and `release_evidence: PASSED`, verifying 26 fixture files, 49 maintained local links, exact evidence manifests, candidate identity binding, blind-source binding, runtime boundaries and the byte-preserved Mission Review migration:

```sh
python3 evals/scripts/verify_mission_brief_release.py \
  --candidate-run evals/runs/mission-brief/20260901T165428Z-365cc4e5 \
  --blind-run evals/runs/mission-brief-blind/20260901T173618Z-a2e490b4 \
  --baseline-run evals/runs/mission-brief-baseline/20260901T091754Z-5b01d157
```

The verified evidence aggregates were the three values recorded above. No installed-runtime claim is made at this stage.

## Independent decision requested

The independent reviewer must inspect the frozen runtime and durable evidence directly, treat this record and all prior verdicts as claims, and return `PASSED`, `FAILED`, or `INCONCLUSIVE`. It should specifically test whether the earlier failed audit's five decisive findings are now closed without disguising the historical source gap. Only `PASSED` authorizes synchronization to `/Users/admin/.agents/skills/mission-brief` and `/Users/admin/.agents/skills/mission-review`.
