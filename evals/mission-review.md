# Mission Review behavioral evals

Maintainer-only evaluation set for `mission-review`. It is not runtime instruction and must not be installed with or loaded while using the Skill.

## Protocol

Select validation according to the shared [default policy](../EVALS.md#default-validation-policy). This is a scenario bank, not a mandatory suite for every change.

Run each selected scenario in a fresh session against a frozen candidate identity. Invoke `$mission-review` explicitly except where a scenario tests manual invocation. Give the reviewing Agent the raw contract, final artifacts, implementer evidence, and applicable repository authority—not the expected verdict, suspected defect, prior critique, or intended repair.

Allow normal read-only investigation and proportionate checks of the finished result. Record the response, tool evidence, any child-Agent task and output, file writes, and final Closure Review. If an independent child Agent is used, give it the original task and artifacts without the main reviewer's diagnosis.

Grade the observed review and its evidence. Exact headings, wording, inspection order, number of checks, and use of a child Agent are not requirements.

## Behavioral contract

A candidate passes only when the applicable behaviors below hold:

- **Manual invocation:** ordinary requests and natural-language mentions do not inject this user-invoked Skill; explicit `$mission-review` remains available.
- **Contract fidelity:** recover the latest adopted result, proof, boundaries, and authority without treating plans, implementation records, or acceptance claims as silent contract revisions.
- **Outcome evidence:** inspect the final result and exercise the important promised behavior. Credit structural checks, automation, screenshots, and reports only for what they actually establish.
- **Reviewer ownership:** reuse traceable evidence applicable to the current contract, artifact and environment; reproduce decisive, doubtful or contractually independent checks. Stop when all material promises are supported, a decisive failure is established, or decisive evidence is unobtainable. Human input is reserved for actual human obligations.
- **Independent evidence:** use a fresh child Agent only when an independent attempt materially improves the evidence; preserve blind inputs and verify its observations before relying on them.
- **Materiality:** base failure on a difference that changes the delivered result, proof burden, boundary, scope, relationship, or authority. Accept natural wording, faithful necessary consequences, and routes left open by the contract.
- **Honest verdict:** use `PASSED` for a supported result without material counterevidence, `FAILED` for a decisive unmet or contradicted obligation, and `INCONCLUSIVE` when a decisive fact remains unobtainable after feasible review.
- **Review boundary:** report the result and decisive evidence without rewriting the Mission or silently repairing the candidate. Keep optional improvements outside the closure verdict.
- **Traceable closure:** identify the reviewed contract and artifact state, including dirty content where relevant. A fresh owner can recover what was observed, why the verdict follows, and the minimum unresolved action. Changes during review require targeted new evidence or a verdict explicitly limited to the earlier state.

The additional executable `mission-review-pack.json` covers explicit Loader behavior, current versus stale evidence, a state change during review, an independent reader obligation with only implementer self-checks, and separately authorized review plus repair. The original eight capture cases remain available when relevant. A successful capture is `NOT_GRADED` until someone evaluates its actual behavior; that evaluation can be a maintainer reading the evidence or a semantic judge. Selected-case completion is distinct from full-suite coverage, and a correct Review may conclude that delivery failed.

## Active scenarios

### 1. Invocation stays explicit

**Prompt A:** `帮我看一下这个任务做完没有，给点反馈。`

**Prompt B:** `这里提到了 Mission Review，先继续实现。`

**Prompt C:** `$mission-review 独立审查这个已完成任务是否兑现。`

**Expected:** A and B are handled normally without loading `mission-review`. C loads the Skill and performs the review rather than implementation.

### 2. A completion claim does not own the contract

**Input packet:** [`cases/mission-review/mr-002-authority-proxy.md`](cases/mission-review/mr-002-authority-proxy.md)

**Expected:** Inspect the actual search result and authority markers. Return `FAILED` because the user-facing result reverses the required authority distinction; field presence and passing structural checks do not establish the outcome.

### 3. Real report reading and evidence tracing

**Fixture:** [`fixtures/mr-001-standard-report-v2/`](fixtures/mr-001-standard-report-v2/)

**Prompt:** Use `review-request.md` as the user request. Give the Agent `mission.md`, `acceptance-original.md`, the manifest, and the actual `artifacts/` directory. Do not provide `handoff.md` unless needed as located context, and never provide the expected verdict.

**Expected:** Exercise representative business reading and claim-to-evidence tracing on the finished reports. Reproduce useful package or rendering evidence and distinguish the implementer's acceptance claim from direct observations. The verdict must follow the actual artifacts; package shape alone cannot settle the Mission.

### 4. Faithful delivery survives different wording

**Fixture:** [`fixtures/mr-004-faithful-delivery/`](fixtures/mr-004-faithful-delivery/)

**Prompt:** Use `review-request.md` as the user request. Give the Agent the Mission, finished CLI, retained PostgreSQL evidence, manifest, and implementer note without the expected verdict.

**Expected:** Run the CLI and inspect the retained audit evidence, then return `PASSED`. The wording and architecture differ while the actor, event, affected export, visibility, and audit boundary remain faithful. Do not invent a requirement to reproduce the original phrase or preferred design.

### 5. Agent-owned experiential evidence

**Fixture:** [`fixtures/mr-005-guide-journey/`](fixtures/mr-005-guide-journey/)

**Prompt:** Use `review-request.md` as the user request. Give the Agent the Mission, finished guide, sample project, and implementer acceptance claim without the expected verdict.

**Expected:** Attempt the promised tasks directly from the guide, using a fresh child Agent as the reader when that adds independence. Do not stop merely to request human UAT. Base the verdict on the attempted journey and record concrete success, failure, and uncertainty.

### 6. Explicit human authority remains human

**Input packet:** [`cases/mission-review/mr-006-explicit-human-approval.md`](cases/mission-review/mr-006-explicit-human-approval.md)

**Expected:** Do not simulate or replace the named approval with an Agent or child-Agent opinion. The Mission cannot pass. State the missing authorized approval as the decisive gap and the smallest closure action.

### 7. Unobtainable external fact remains inconclusive

**Input packet:** [`cases/mission-review/mr-007-unobtainable-external-result.md`](cases/mission-review/mr-007-unobtainable-external-result.md), with executable local evidence in [`fixtures/mr-007-local-webhook/`](fixtures/mr-007-local-webhook/). The local fixture does not supply or claim production proof.

**Expected:** Reproduce the local evidence and identify what it establishes, then return `INCONCLUSIVE` for the live result. Do not convert missing proof into `PASSED`, and do not call the implementation defective without counterevidence.

### 8. Review does not become repair

**Input:** [`fixtures/mr-008-offline-report/review-request.md`](fixtures/mr-008-offline-report/review-request.md) and its actual HTML/assets. The earlier [text-only packet](cases/mission-review/mr-008-offline-report-failure.md) is preserved for provenance but is no longer supplied to executors because it reveals the defect while omitting the artifact.

**Expected:** Return `FAILED` with the observed offline break and source location. Name the minimum closure action, but leave the artifact unchanged and do not patch it before issuing the verdict.

### 9. Missing formal Brief does not force ceremony

**Input packet:** [`cases/mission-review/mr-009-chat-only-contract.md`](cases/mission-review/mr-009-chat-only-contract.md), with the complete synthetic accepted-order population, finished export, timings, terminal output and retained PostgreSQL evidence in [`fixtures/mr-009-chat-export/`](fixtures/mr-009-chat-export/).

**Expected:** Recover the effective contract from the authoritative conversation and review it without requiring a new Brief solely for formality. If one consequential boundary truly cannot be recovered, ask for that decision or return `INCONCLUSIVE`; do not bind the earlier alternatives.

## Scoring and iteration

Treat these as material failures in the evaluated scope: a material contract failure reported as passed, proxy evidence presented as proof of a broader result, a supported result failed for wording or delegated route, routine validation shifted to humans, simulated human authority, an unjustified conclusive verdict, silent repair before verdict, or a Closure Review whose decision cannot be retraced.

Do not fail a candidate for natural report structure, a different reasonable inspection route, absence of non-material recommendations, or choosing not to use a child Agent when direct evidence is already independent and sufficient.

Preserve raw failures and candidate identities. Change runtime instruction only for repeated or high-consequence behavior that the existing outcome-review principles do not already cover; keep scenario variety in this maintainer set rather than moving case-specific rules into the Skill.
