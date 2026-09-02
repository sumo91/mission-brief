---
name: mission-brief
description: Create one stable, traceable result contract for a capable fresh agent.
disable-model-invocation: true
---

# Mission Brief

Use **mission command**: freeze an adopted result, its proof, and its hard boundaries while leaving the route to the executing Agent.

A Mission Brief is a result contract, not a proposal review, final design, implementation plan, or execution request. When a request needs another product too, keep the products separate and settle any decision that defines the commission before freezing it.

## Principles

- **Outcome over route.** The executing Agent has fresher workspace and environment evidence, so specify what must become true and let it choose a viable route.
- **Source status.** An **Authority Source** can bind the Mission; a **Reference Source** preserves useful knowledge without becoming binding merely because it is retained or linked.
- **One home.** **Material information** is information whose loss could change the contract, materially increase execution risk, or force costly investigation to be repeated. Give each material item one durable home: the Brief, a labeled durable source, a consequential unsettled decision, or justified omission.
- **Falsifying proof.** Evidence must be capable of exposing failure in the promised result. Tests, screenshots, schemas, and reports prove only the behavior they actually exercise.

The four required sections—`Outcome`, `Success`, `Evidence Required`, and `Boundaries`—form the **Contract Core**. A complete handoff also identifies the target, authority, necessary durable context, source status, and any adopted parent topology. Protect **route freedom** so a fresh Agent can act without inheriting candidate approaches as commands.

## 1. Recover the commission

Use the conversation, named artifacts, and enough workspace evidence to identify the result and authority. Choose one coherent change in user or system reality with independent value and an honest verdict. Complexity does not split a result; independent outcomes may.

When adopted facts support one reasonable result, synthesize it without asking the user to restate the source as Brief headings. Ask only when materially different results remain possible or several unrelated results need separate acceptance.

Classify from the visible commission before opening a reference. Keep unrelated independently acceptable results on the main path and ask which result to commission. Read a conditional reference only when its branch is already present:

| Branch | Reference |
| --- | --- |
| The commission already states one shared result whose seam can fail after its local results pass, or a child explicitly tied to an approved parent | Read [`references/mission-zero.md`](references/mission-zero.md). |
| A named source mixes authority states, holds material completed investigation, or is temporary while holding the only copy of material information | Read [`references/source-fidelity.md`](references/source-fidelity.md). |

Material facts stated directly in the current conversation can enter the Brief's `Context` without opening a source branch.

This step is complete when one result is identifiable and any required integration topology has been adopted.

## 2. Settle consequential decisions

Collect the adopted user decisions and applicable external authority that shape the Contract Core. Preserve the minimum meaning needed for execution and review; a source need not use Brief terminology.

A retained source keeps its status. Preserve confirmed dependencies, compatibility facts, causal risks, and costly findings. Leave root causes, edit locations, tools, internal structure, and product-neutral architecture to execution when they are safely discoverable.

When a handoff names an unavailable Authority Source but states the applicable constraints, preserve both the constraints and source identity. Stop only for a known authority conflict or an unsettled choice whose alternatives would change the Contract Core, authority, adopted topology, or whether material information will survive the handoff. Do not resolve a conflict by silently dropping requested content. For an external execution gate, identify who can authorize it and what evidence would establish that it occurred.

This step is complete when writing the Brief will not invent product policy, bypass authority, or erase non-recoverable knowledge.

## 3. Write the current contract

Use the Contract Core and add only useful optional sections: `Intent`, `Non-goals`, `Context`, `Execution Authority`, `Parent Mission`, or `Result Boundaries`.

Keep `Success` about facts that must hold and `Evidence Required` about how to challenge them. Scale evidence to consequence and claim breadth. A population claim needs exhaustive coverage or representative classes plus relevant boundaries. Reading, judgment, or use requires a realistic attempt. Reserve human participation for a contracted decision or experience an Agent cannot supply. Evidence must support `PASSED`, `FAILED`, or `INCONCLUSIVE`.

Treat a platform, mode, consumer, or interaction that the user says must remain unchanged as a compatibility baseline and require proportionate regression evidence.

Draft a clean current contract from facts with a current adopted effect. Earlier and candidate routes remain only in any durable labeled source that already preserves them. An explicit prohibition is a current adopted constraint, not the fact that a proposal was rejected or superseded. The Brief should read as if authored directly from the final decisions; include a prior route's identity only when it carries a current compatibility obligation, explicit prohibition, or authority boundary.

Example:

```markdown
# Mission Brief: Safari users can submit the login form with Enter

## Outcome
Safari users can submit valid login credentials by pressing Enter in the login form.

## Success
- Enter submits the same credentials and produces the same visible result as the submit button.
- Invalid credentials remain visible as a failed login rather than appearing to succeed.
- Chrome keyboard submission and mouse-button submission remain unchanged.

## Evidence Required
- Exercise valid and invalid Enter submission in Safari.
- Repeat the corresponding keyboard flow in Chrome and the button flow in both browsers.

## Boundaries
- Preserve the existing authentication and error-message semantics.
```

If two unadopted choices would produce different authorization semantics, state the affected part of the contract and ask which choice is adopted; do not write the Brief until that decision exists.

This step is complete when the Contract Core is falsifiable, each material item has one home, and no optional route has become a command.

## 4. Save and hand off

Return the Brief inline when requested or when writes are unavailable. Otherwise use the requested path, then an established repository convention, then `docs/missions/<outcome-slug>/brief.md` at the documentation boundary that owns the result.

Update a file only for the same commission and give each distinct result a stable outcome slug. Use repository-relative links and keep necessary context in a durable repository location. Create a companion context record only for material content that lacks another durable home.

For Mission 0 and child storage, follow the loaded topology reference.

Finish with a **blind handoff** check:

1. Can a fresh Agent restate the Contract Core?
2. Can it locate necessary context and distinguish Authority Sources from Reference Sources?
3. Can it explain what would justify `PASSED`, `FAILED`, or `INCONCLUSIVE`?
4. Can it choose a viable route without relying on hidden authoring context?

The handoff is complete when all four answers are yes.
