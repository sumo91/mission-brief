---
name: mission-align
description: Align an unclear or contested Mission commission before briefing.
---

# Mission Align

Use **alignment dialogue**: make consequential interpretations visible and settle the result and its boundaries before handing off.

Speak plainly. Explain Mission-system concepts through the concrete result and consequences instead of making the user learn the vocabulary.

This Skill owns alignment. After alignment, return to any still-authorized original request; writing its Brief, plan, or implementation belongs to that next phase. An alignment-only request ends with the handoff.

## Recover the commission

Use the conversation and named material to distinguish adopted decisions, confirmed facts and applicable authority, candidate interpretations and approaches, and consequential open choices. Preserve each source's status: discussion and retention do not make it binding. Leave safely discoverable implementation facts to execution.

Assess three dimensions separately. A Mission candidate is one independently verifiable change in user or system reality.

**Route:** decide whether the useful next product is further exploration, research or advice, a design or final plan, direct work without a Brief, or a Mission Brief. A Mission Brief records an adopted result contract; it does not solve the commissioned work or substitute for another requested product.

**Readiness:** use `EXPLORING`, `DECISION NEEDED`, `BLOCKED`, or `ALIGNED` internally when helpful. Explain naturally what is settled and what remains. `ALIGNED` means the current result and consequential boundaries have been explicitly adopted or decided within an explicit delegation.

**Topology:** when a Mission candidate exists, recommend:

- one Mission when one independently verifiable result owns the value and verdict, regardless of size, duration, components, teams, or implementation phases;
- several independent Missions when several results provide independent value and no overall result needs its own verdict; or
- a Parent Mission with Child Missions only when independently verifiable result boundaries also serve an irreducible overall result that could still fail after every local result passes.

For a possible Parent Mission, test a concrete “all children pass, whole still fails” scenario. Make the overall result, result boundaries, cross-result invariants, and unsettled topology choice visible. Keep new topology a proposal until adopted.

A class, file, command, activity, phase, or test count does not by itself establish a Mission result. Small, clear, immediate work may be a valid Mission while still not benefiting enough from Brief ceremony; explain that distinction when it changes the recommendation.

## Resolve consequential choices

Raise a question only when different answers would materially change the result, success meaning, proof expectation, boundary, topology, authority, or durable disposition of important information.

Make the uncertainty and its consequence concrete, then ask for the smallest decision that advances alignment. Offer options and a reasoned recommendation when useful. Let the current gap determine the dialogue; discuss coupled questions together when separating them would hide the tradeoff. Product-neutral architecture, tools, root cause, and edit location remain execution choices when safely discoverable.

You may use solution directions to reveal competing outcomes or preferences. A solution becomes binding only when the user explicitly adopts it as part of the result or a hard boundary.

When the user delegates a consequential choice, restate the delegated scope, decide within that scope, explain the reason, and record only that scope as adopted.

While a decision is pending, continue proportionate, already-authorized reading or fact checks that do not depend on it. Use asynchronous questions when available; ordinary dialogue also works. A required answer remains pending regardless of elapsed time, and the dependent contract or disputed work waits.

## Complete the handoff

Use one concise synthesis as the handoff. Preserve the adopted result and intent, route and topology, success meaning and adopted proof expectation, boundaries and compatibility, authority and delegated choices, any adopted solution constraint, necessary source pointers with their status, and non-blocking uncertainty. State whether it remains in chat or is persisted. Include only what could affect the next product; unadopted routes and implementation plans stay outside the handoff.

The user's explicit instructions and scoped delegation adopt the decisions they already settle. When the synthesis preserves those decisions and adds no new consequential interpretation, hand it off directly. Request a decision for a new consequential interpretation, an unsettled choice outside delegation, or an authority conflict. If the user requests a summary for confirmation first, honor that boundary. Delegation cannot replace a required external decision.

An unambiguous “change X; the rest is correct” adopts the amended synthesis when its meaning is complete. Preserve unaffected decisions and ask only about a new consequential ambiguity or conflict. Tentative suggestions, silence, and partial agreement do not settle an open choice or authorize a change.

After adoption, hand off the synthesis itself, adding only necessary source or persistence pointers. It preserves existing authorization without creating additional authority.

Default to a conversational handoff. Persist a **Mission Alignment Handoff** only when losing the conversation could change the result, boundary, authority, topology, or recoverability of completed material investigation; when another session, task, or Agent must continue; or when the user explicitly requests it. Judge volume by information-loss consequence, not word count.

For persistence, honor the requested path, then an established repository convention. Otherwise use `docs/missions/<outcome-slug>/alignment.md` for an adopted Mission, or `docs/mission-alignments/<candidate-slug>.md` for incomplete alignment that must survive a session boundary. Clearly separate adopted decisions, confirmed facts and authority, candidate material, open decisions, and the recommended route. An incomplete handoff must state that no Mission has been aligned or authorized.

When an already-invoked `mission-brief` entered alignment, return the adopted decisions to that request and complete its authorized Brief without asking the user to invoke it again. For alignment-only requests, provide an exact next invocation when useful, such as `$mission-brief 根据上面已确认的 Mission Alignment 生成 Brief`. Point to the handoff instead of repeating it. Resume only a request that has not been cancelled or replaced.

Finish when no consequential interpretation has been silently chosen, the current synthesis is adopted within applicable authority, and the next product can recover it without treating discussion as authority. If a choice cannot be settled, identify the blocker and who can resolve it.
