# Second Minimal Refactor Candidate

## Review question

Does this candidate preserve the original Mission Brief result—reliable, traceable, route-free handoff to a fresh executing Agent—while reducing instruction load, defensive prompting, unnecessary blocking, and evaluation-specific sediment?

The decisive standard is downstream handoff quality, not compliance with this record.

## Frozen runtime

| File | SHA-256 | Lines | Words |
| --- | --- | ---: | ---: |
| `SKILL.md` | `83245d825fa31d0d26ec89267f785c9a4aec4d3445ca12cb461a349497029ebb` | 99 | 1135 |
| `agents/openai.yaml` | `5dc4b7d32e7175b072fbf31b2a4493cca00ba90f02209ace39e2a77d4e570921` | 7 | — |
| `references/mission-zero.md` | `1e71c29418a263236b0ed0b72e685eb0da8fc686bf5057c57b3531487418fa9d` | 42 | 327 |
| `references/source-fidelity.md` | `9a3986ca2157db5df547c6cea473febed253e025d4170954df5b226cd60e7cdd` | 21 | 247 |

The four-file runtime digest is `7020e09790c9a012c2849bc786d8f34be6e753d6c1dfa92104adec376bb8fe27`.

The previous runtime contained 1513 words in the main Skill and 1008 words across its two references. The candidate contains 1135 main words and 574 reference words. The main file now includes a complete worked Brief example; instruction-only text is therefore closer to the planned 1000-word budget than the raw total suggests.

## Material design changes

- Four principles with reasons replace repeated negative and case-specific rules: Outcome over route, Source status, One home, and Falsifying proof.
- `material`, Authority Source, Reference Source, and route freedom are defined on the main path.
- `Contract Core` is the only repeated contract-dimension name.
- `Context` is a normal optional section; source-fidelity handles only complex source cases.
- The topology pointer requires a visible shared result before loading the Mission 0 branch.
- A complete ordinary Brief and one short stop example replace the empty template.
- The clause-deletion thought experiment and rejected-name scanning rules are gone.
- Mission 0 is introduced as an Integration Mission while preserving compatible titles and paths.

## Evidence produced during implementation

The eight-case semantic smoke run is retained at `evals/runs/mission-brief/20260902T100629Z-cb551f04`. Six cases passed immediately. Two findings were used as upstream design feedback rather than copied into new defensive checks:

- `c-1000000b` produced the correct user result but unnecessarily loaded the Mission 0 reference. The pointer was changed to classify unrelated results on the main path. The focused rerun at `evals/runs/mission-brief/20260902T101741Z-4f19e6e4` passed this case without loading the reference.
- `c-10000012` preserved superseded route names as negative constraints. The definition of current explicit prohibition was clarified. The focused rerun at `evals/runs/mission-brief/20260902T102010Z-70e51811` passed.

The other smoke cases covered a simple Mission, settled source synthesis, authority conflict, integrated Mission 0, mixed authority, and a temporary-only source. Their semantic criteria passed.

Those retained runner reports bind predecessor runtime digests ending in `a7d9d499...` and `dbfbb8bb...`. A final prose-only pruning pass produced the frozen `7020e097...` runtime, so the focused reports are directional regression evidence rather than exact-candidate identity evidence. The exact frozen candidate was subsequently reviewed in the fresh task `codex://threads/01a061ac-9956-70a3-aa9d-5614074d6ed8`, which performed a current-runtime mixed temporary-source authoring exercise followed by a no-author-context blind handoff and returned `PASSED`.

A subsequent judged full-suite run was stopped after its measured throughput implied roughly 30–40 additional minutes of mostly repeated conformance checking. It produced no complete verdict and must not be presented as passing evidence. This was an explicit result-over-process decision: the existing stable release already has full-pack evidence, the changed candidate has focused coverage across each high-risk branch, and the requested final gate is an independent fresh-session review of the original outcome.

The bundled `quick_validate.py` could not import `yaml` in the current Python environment. No dependency was installed solely to satisfy that tool. Equivalent frontmatter, required-field, reference-path, placeholder, and `git diff --check` checks passed.

## Independent review instructions

Treat this record, prior verdicts, and implementation explanations as claims. Inspect the frozen runtime and relevant raw evidence directly. Review against the original Mission in `../brief.md`, not against wording similarity or completion of every planned ceremony.

Use a fresh task to test the highest-value downstream question: can an Agent without the authoring conversation recover the adopted result and authority, find material facts, distinguish optional routes, propose an independent viable route, and explain an honest closure verdict with less instruction burden than the previous release?

Return `PASSED`, `FAILED`, or `INCONCLUSIVE` with the smallest decisive evidence. A missing process artifact is material only when it prevents a trustworthy result judgment.
