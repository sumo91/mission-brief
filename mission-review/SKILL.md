---
name: mission-review
description: Review a completed Mission against its adopted result contract and produce an evidence-grounded closure verdict.
---

# Mission Review

Use **outcome review**: test the delivered result, not whether the implementation or report resembles the words used to commission it.

Review a completed Mission from its adopted contract, finished artifacts, and available evidence. Keep optional improvements outside failure conditions. Preserve the verdict before entering any separately authorized repair phase; a review-only request leaves the work and contract unchanged.

## 1. Recover the promise

Locate the Mission Brief or the latest authorized contract that serves the same purpose. Read applicable repository authority, labeled context sources, and only enough implementation record to find the result and its evidence.

Recover:

- the outcome that should now be true for a user or system;
- plausible failures that the contract distinguishes from success;
- required proof and hard boundaries;
- any commission-specific authority or explicit human decision.

Treat Authority Sources, Reference Sources, plans, progress logs, implementation choices, acceptance claims, and earlier proposals according to their actual status. They may preserve context or point to evidence; retention, linkage, or package membership does not silently redefine the Mission.

Preserve meaning rather than sentence form. A wording difference matters only when it changes the promised result, proof burden, boundary, scope, relationship, or authority.

When no reliable contract can be recovered, request the smallest missing decision if it is available from the user. Otherwise review what can be established and keep the verdict `INCONCLUSIVE` rather than inventing policy.

This step is complete when the promised result and the facts that would materially falsify it can be stated without relying on the implementation's own completion claim.

## 2. Exercise the finished result

Identify the contract and artifact state being reviewed, using a commit, relevant file digest, deployment identity, or observable state appropriate to the claim. HEAD alone does not identify uncommitted changes. If the result changes during review, identify affected claims and recheck them; qualify a verdict that covers only the earlier state.

Inspect actual deliverables. Reuse traceable evidence when its coverage, artifact state, and relevant environment still apply; reproduce decisive or doubtful parts and any explicitly required independent checks. Perform the least costly additional checks capable of falsifying remaining meaningful claims. An implementer assertion is a lead, not reproduced evidence.

Credit each check only for the behavior it exercises. File presence, schema shape, passing automation, screenshots, and implementer summaries can support a verdict, but none proves a broader user or system result by association.

For a claim about reading, judgment, or use, attempt the promised task on the finished result under representative conditions. Record what succeeds, fails, or remains uncertain.

The reviewing Agent owns every check it can genuinely perform. Reserve human participation for an explicitly contracted human decision or an experience an Agent cannot supply.

Use an existing fresh review context or a fresh child Agent when independence materially improves the evidence, such as a reader task or a review after participating in implementation. A new Agent inheriting the implementation history is not a blind attempt. If independence is unavailable, disclose that limit and judge whether the contract requires it.

Give it the original contract, finished artifact, and task without the expected verdict or suspected defect. Treat its observations as evidence to verify, not as an approval that replaces the main reviewer's judgment.

Stop when proportionate evidence supports all material obligations, a decisive failure establishes `FAILED`, or a remaining decisive fact is unobtainable. Extend checks only for new changes, counterevidence, or unresolved material doubt.

## 3. Judge material fulfillment

Compare the observed result with the adopted promise. Ask whether the disputed difference gives the user a substantive reason to say the promised result was not delivered.

Accept faithful necessary consequences, natural wording, and choices the contract left to execution.

Keep preferences, polish opportunities, speculative risks, and stronger future standards outside the verdict unless they expose a present contract failure.

Use the verdicts consistently:

- `PASSED`: the required result is supported by proportionate evidence and no material counterevidence remains.
- `FAILED`: a material promised result, proof obligation, boundary, or authority condition is contradicted or unmet.
- `INCONCLUSIVE`: feasible review cannot establish or refute a decisive claim with trustworthy evidence.

A passing result may still have non-blocking improvements. A failed result needs a decisive gap, not a quota of findings. Evidence that was merely asserted but could not be reproduced remains identified as such.

## 4. Write the Closure Review

Lead with `PASSED`, `FAILED`, or `INCONCLUSIVE` and the decisive reason. Make the observed result and supporting or contrary evidence easy to find.

Include material gaps and unresolved uncertainty only when they affect the verdict. For a failed or inconclusive review, name the smallest action that could close it.

Distinguish direct observation, reproduced evidence, implementer claim, and reviewer inference when that distinction affects confidence.

Cite the reviewed state and concrete artifact paths, commands, outputs, or interactions closely enough for another Agent to retrace the decision. A later repaired result requires its own verification; it cannot retroactively pass the original delivery.

Choose headings that fit the repository rather than filling a fixed form. Do not manufacture recommendations after `PASSED` or design a repair unless the user separately commissions it.

Return the review inline when requested or when writes are unavailable. Otherwise honor a requested path, then an established repository convention. When the Mission lives at `docs/missions/<mission-slug>/brief.md`, place the review under that Mission's `reviews/` directory with a concise distinct filename; otherwise use `docs/closure-reviews/<mission-slug>.md` at the relevant documentation boundary.

Finish when a fresh owner can see what was promised, what was actually observed, why the verdict follows, and what—if anything—still prevents closure.
