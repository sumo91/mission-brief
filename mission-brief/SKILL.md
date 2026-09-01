---
name: mission-brief
description: Create one stable, traceable result contract for a capable fresh agent without replacing a final plan or losing material handoff context.
disable-model-invocation: true
---

# Mission Brief

Use **mission command**: specify the destination, proof, and hard boundaries—not the route. Compress an adopted commission into one stable Brief for a fresh capable agent.

A Mission Brief is a result contract, not a final plan, design review, decision recommendation, or implementation plan. This Skill authors only the Mission Brief; do not create one of those other products inside a `$mission-brief` invocation or silently substitute the Brief for it. When the request asks for another product, explain the boundary and ask whether to freeze the adopted commission as a Brief, produce the other product separately, or do both before writing anything.

A class, file, component, command, phase, or test-count request does not by itself define either a Mission or a product-routing choice. First ask for the observable user or system result, or place the implementation item beneath an existing Mission.

Write one Brief only when the commission is settled. When a consequential user choice or authority conflict would change the contract, write nothing; show what remains undecided and request the smallest decision that can settle it.

## 1. Locate the commission and its sources

Ground the commission in the conversation and named artifacts. Locate the target, adopted user decisions, applicable repository or governance authority, and material source information. Inspect the workspace only far enough to judge the contract boundary and find the sources needed for a durable handoff.

A source may mix adopted decisions, confirmed facts, candidate approaches, critiques, and superseded material. Preserve each item's actual status. Retaining or linking a source does not make all of it binding.

Treat source information as **material** when losing it could change the result, verdict, proof, boundary, target, or authority, or erase a known dependency, concrete risk mechanism, compatibility fact, or costly investigation that a fresh Agent would otherwise need to repeat.

Distinguish safely discoverable unknowns from completed investigation. Leave an unknown root cause, implementation location, internal structure, tool, or architecture to the executing Agent when it can be discovered safely. Do not discard an already confirmed material fact merely because another Agent could rediscover it.

If the user requested a different product, or material information exists only in a transient source and cannot be preserved within the authorized handoff, stop after explaining the smallest disposition decision still needed.

## 2. Choose the result

First decide from the visible commission whether it explicitly concerns an adopted or pending overall result that may fail after local results pass, or a child explicitly tied to a Mission 0. If and only if that condition is true, read [`references/mission-zero.md`](references/mission-zero.md) before deciding or writing. Never open it preemptively for source inspection, ordinary single-result work, or several unrelated results.

Choose one **result**: a coherent change in user or system reality that has independent value and can receive an honest verdict. Files, components, activities, phases, and test counts are execution work unless they define that observable change.

- If no observable result is stated, ask what should become true for the user or system, or place the request under an existing Mission.
- If one result owns the destination and verdict, continue with it regardless of size or complexity.
- If several results can be accepted independently, ask which one to commission unless the user has stated or is considering an overall result that could still fail after every local result passes.
  In that case, make the candidate integration topology explicit. Do not write the parent Brief until the user adopts it.

Do not open the Mission 0 reference or manufacture a candidate parent merely because several unrelated results were grouped together or the user requested a parent label. First establish that a genuine overall result is stated or under consideration.

A parent label or a large scope does not establish an integrated result. Read the Mission 0 reference for a later child explicitly tied to an approved parent as well.

This step is complete when one commission boundary is selected or the user can see the smallest topology decision still needed.

## 3. Settle the contract

Collect the adopted user decisions and applicable external authority that determine the result. Include binding content only when it follows from them, preserves their minimum necessary meaning, defines task-appropriate proof, or points to a necessary located Authority Source.

Paraphrase faithfully. Preserve who or what acts on what, the direction of important relationships, confirmed scope and granularity, and the original proof burden.

Discussion, examples, critiques, risk hypotheses, and proposed solutions remain non-binding until adopted. They may remain useful in a labeled Reference Source; preservation never promotes them into requirements, authorization, or a mandatory route.

Keep repository contracts, compatibility commitments, and governance decisions in force. When they conflict with the requested commission and no authorized supersession exists, expose the conflict before writing.

Treat current implementation as a fact to change when the Mission requires it, not as authority over the Mission.

Ask for a user decision only when different answers would materially change the outcome, success meaning, proof, boundary, topology, authority, or durable disposition of otherwise transient material information. Display any proposed synthesis that needs adoption in concrete language. When stopping for that decision, state in the main response every materially changed contract dimension; do not give one representative consequence or leave the rest only in an uncertainty field or audit record. For an unresolved approval, review, or gate, explicitly say whether adopting it would change who authorizes execution and what evidence must prove that the gate occurred.

Delegate product-neutral architecture, tools, implementation choices, safely discoverable unknowns, and facts already available in a durable located source.

The contract is settled when a fresh Agent can identify the result, meaningful failure, proof obligations, hard boundaries, target, and granted authority without inventing product policy.

## 4. Write, compress, and preserve traceability

Use this core structure:

```markdown
# Mission Brief: <observable result>

## Outcome
<What becomes possible or true at the user or system boundary.>

## Success
<The minimum falsifiable facts that distinguish success from a plausible but wrong result.>

## Evidence Required
<The task-appropriate evidence needed for an honest verdict.>

## Boundaries
<The hard limits that change valid execution.>
```

Add a section only when it carries binding content or necessary handoff information:

- `Intent`: an adopted purpose that adds meaning beyond `Outcome`.
- `Non-goals`: confirmed adjacent exclusions that change valid execution.
- `Context`: necessary target facts and durable pointers, labeled as Authority Sources or Reference Sources according to their actual status.
- `Execution Authority`: a commission-specific grant or restriction that changes ambient authority.

Keep `Success` about facts that must hold and `Evidence Required` about how to challenge them. Evidence must address the promised result rather than substitute convenient proxy checks.

When a claim spans a population, numeric domain, state space, or compatibility surface, require evidence that challenges representative classes and relevant boundaries unless the supported domain can be exercised exhaustively.

For claims about reading, judgment, or use, have the executing Agent exercise the finished result under realistic conditions and record concrete success, failure, and uncertainty. Structural and automated checks support the behaviors they actually exercise.

Use the least costly evidence capable of falsifying each claim, increasing strength with consequence, irreversibility, cross-system reach, or genuinely subjective judgment. The eventual evidence must support an honest `PASSED`, `FAILED`, or `INCONCLUSIVE`.

Human participation is reserved only when the contracted claim itself depends on a human decision or experience an Agent cannot genuinely supply, not when the Agent is merely uncertain or routine validation is difficult. Otherwise the Agent continues feasible validation and reports `INCONCLUSIVE` if a decisive fact remains unavailable.

Preserve an externally fixed mechanism when changing it would alter user-facing behavior, compatibility, collaboration, or governance. Otherwise describe the observable result and leave the route open.

Treat an explicitly named already-working platform, mode, consumer, or interaction as a compatibility baseline when the user contrasts it with the failure or says it must remain unchanged. Preserve that baseline in `Success` or `Boundaries` and require proportionate regression evidence; do not discard it as background merely because it is not the broken path.

Before finalizing, give each material source item one honest disposition: express its adopted effect in the Brief; preserve it in a durable labeled source; expose it as a consequential unsettled decision; or omit it because it is irrelevant, rejected, superseded, or safely discoverable without erasing completed investigation. Do not emit an inventory unless it helps the handoff.

When a durable pointer is sufficient for material non-binding content, name each retained category and its status in the pointer, such as candidate approaches or an advisory investigation order. Do not copy the individual routes or steps merely to make that coverage visible.

When compressing a confirmed causal finding, preserve the actor or trigger, the affected object, the mechanism or relationship, and the material consequence needed to understand the risk. A category label or partial paraphrase is not enough when it erases why the failure recurs.

When necessary material exists only in a temporary path, attachment, or source conversation, preserve the minimum necessary content in `Context` or an established durable repository record. Create a separate context record only when the user requested a Mission Package or repository convention calls for one; otherwise request the smallest disposition decision that prevents silent loss.

For a Mission 0, do not use the parent `Context` as a substitute home for confirmed child-local contracts. Follow the Mission 0 reference and keep the parent unwritten until their durable disposition is explicitly settled. While that disposition blocks writing, do not emit a candidate parent, parent-section outline, or other draft-like substitute for the unwritten Brief; identify the blocked commission and ask only for the smallest disposition decision.

State the current contract, not implementation phases, ownership plans, commands, counts, hashes, completed checks, rejected alternatives, or generic safety prose. Rejected or superseded material may shape the synthesis, but do not mention it by name or through generic historical disclaimers; retain an identity only when current compatibility, prohibition, or authority depends on it.

Keep unadopted candidate approaches in a labeled durable source. Do not copy or paraphrase them into `Boundaries`, `Non-goals`, or a negative requirements list merely to say that they remain optional.

Before saving, compare the Brief against every source item classified as candidate, rejected, or superseded. If a specific route name or identifying paraphrase still appears in `Boundaries`, `Non-goals`, or another contract clause only to disclaim, defer, or contrast it, remove it and rely on the labeled durable pointer plus one generic statement that the route remains open. Keep that identity only when the current contract truly depends on a compatibility obligation, explicit prohibition, or authority boundary attached to it.

Do not add `Context` merely to cite the current user conversation, an empty workspace, the absence of a repository convention, or an implementation fact already delegated for safe discovery.

Mission Brief owns the commission. Authority Sources own applicable decisions and contracts; Reference Sources own useful non-binding context; working plans own route, progress, discoveries, and intermediate evidence; Closure Reviews own actual evidence, counterevidence, verdict, and uncertainty.

Those records may evolve without silently redefining the Brief.

Delete any clause whose removal would not change the result, verdict, proof, hard boundaries, authority, approved topology, necessary target location, or ability to recover material handoff context.

## 5. Save and hand off

Return the Brief inline when requested or when writes are unavailable. Otherwise honor a requested path, then an established repository convention, then use `docs/missions/<outcome-slug>/brief.md` at the relevant repository or package documentation boundary.

Update an existing file only for the same commission; give a distinct result a distinct directory. Do not encode phases, owners, status, dates, or revision numbers in the Mission directory name.

Mission 0 is the parent role of the same `brief.md` artifact, not a global `mission-0.md` file type. Within one documentation boundary, store commissioned children under `children/<child-outcome-slug>/brief.md`, link each parent Result Boundary to its child, and link each child back to its Parent Mission. Across package boundaries, keep each Brief at the boundary that owns its result and use explicit bidirectional links instead of forcing physical nesting.

In saved artifacts, write repository-relative links that resolve from the containing document. Never persist a scratch-workspace, temporary-directory, or evaluation-run absolute path as a source, parent, or child link.

Do not create empty child directories or mandatory companion files. Produce the commission, not its implementation or progress record. Revise the Brief later only when the contract itself changes.

Finish with a **blind handoff** check. Without the source conversation, a capable fresh Agent must be able to:

- recover the outcome, meaningful failure, proof obligations, boundaries, target, and authority;
- locate necessary durable context and distinguish Authority Sources from Reference Sources;
- recover material known dependencies and risks without treating optional approaches as commands; and
- choose a viable route not copied from the authoring context.

Compare the handoff with the material content of named sources, not merely with the Brief in isolation. Require coverage and traceability, not sentence-by-sentence reconstruction.
