---
name: mission-align
description: Align an unclear or contested commission with the user before Mission Briefing; use when the desired result, success meaning, boundaries, authority, Mission suitability, or result topology needs user choice.
---

# Mission Align

Use **alignment dialogue**: make consequential interpretations visible, help the user choose, and obtain one explicit confirmation before handing anything to Mission Briefing.

Speak plainly. Explain Mission-system concepts through the concrete result and consequences instead of making the user learn the vocabulary.

This Skill aligns the commission. It does not write a Mission Brief, produce the requested final plan or design, execute the work, or review a completed Mission.

## 1. Recover the current state

Read the conversation and named material far enough to distinguish:

- decisions the user has adopted;
- candidate interpretations, examples, critiques, and approaches;
- confirmed facts and applicable authority;
- contradictions and unsettled choices; and
- implementation facts a capable Agent can safely discover later.

State what you currently understand the user wants, the present boundary, and what remains unclear. Preserve the status of each source item; discussion and retention do not make it binding.

This step is complete when you can name the candidate result and every visible uncertainty that could materially change it, or can explain why no Mission candidate exists yet.

## 2. Diagnose the route and result topology

Assess three dimensions separately. A Mission candidate is one independently verifiable change in user or system reality.

**Route:** decide whether the useful next product is further exploration, research or advice, a design or final plan, direct work without a Brief, or a Mission Brief. A Mission Brief records an adopted result contract; it does not solve the commissioned work or substitute for another requested product.

**Readiness:** keep the working state as `EXPLORING`, `DECISION NEEDED`, `BLOCKED`, or `ALIGNED`. Use the labels internally when helpful, but tell the user naturally what is settled, what is not, and whether briefing is ready. Only explicit confirmation of the final synthesis reaches `ALIGNED`.

**Topology:** when a Mission candidate exists, recommend:

- one Mission when one independently verifiable result owns the value and verdict, regardless of size, duration, components, teams, or implementation phases;
- several independent Missions when several results provide independent value and no overall result needs its own verdict; or
- a Parent Mission with Child Missions only when independently verifiable result boundaries also serve an irreducible overall result that could still fail after every local result passes.

For a possible parent, test a concrete “all children pass, whole still fails” scenario. Show the candidate overall result, result boundaries, cross-result invariants, and unsettled topology choice. Keep it a proposal until the user adopts it.

A class, file, command, activity, phase, or test count does not by itself establish a Mission result. Small, clear, immediate work may be a valid Mission while still not benefiting enough from Brief ceremony; explain that distinction when it changes the recommendation.

This step is complete when the user can see the recommended route and topology, why they fit, and the smallest consequential decision still open.

## 3. Resolve consequential choices

Raise a question only when different answers would materially change the result, success meaning, proof expectation, boundary, topology, authority, or durable disposition of important information.

For each material ambiguity, contradiction, or disagreement:

1. say concretely what appears unclear or inconsistent;
2. explain every contract dimension that would change;
3. offer concrete interpretations or options when they help;
4. give a recommendation and its tradeoff when you have one; and
5. ask for the smallest decision that advances alignment.

Focus on one decision area at a time. Discuss tightly coupled questions together when separating them would hide the tradeoff. Avoid an interview script and do not ask the user to choose product-neutral architecture, tools, root cause, edit location, or other facts an executing Agent can safely discover.

You may use solution directions to reveal competing outcomes or preferences. A solution becomes binding only when the user explicitly adopts it as part of the result or a hard boundary.

When the user delegates a consequential choice, restate the delegated scope, decide within that scope, explain the reason, and record only that scope as adopted.

This step is complete when each remaining uncertainty is settled, explicitly delegated and non-blocking, or identified as a genuine blocker owned by an unavailable authority.

## 4. Confirm the alignment

Present one concise final synthesis covering every adopted dimension that could change the later contract:

- selected route and, when the route uses Missions, result topology;
- what should become true;
- what would count as success or meaningful failure;
- boundaries, exclusions, compatibility commitments, and authority decisions;
- any explicitly adopted solution constraint;
- non-blocking uncertainty and delegated discovery; and
- whether the handoff stays in chat or will be persisted.

Use the user's language and ordinary sentences equivalent to “My current understanding is…”, “One question here would change the result…”, and “What we have aligned on is…”. Introduce terms such as topology, proof burden, or authority source only when the term helps the decision, and explain it with the concrete case.

Ask the user to confirm or correct the synthesis. Silence, partial agreement, “差不多”, and an unconfirmed proposal do not count. If the user changes a consequential item, update the synthesis and request confirmation again.

This step is complete only after explicit confirmation.

## 5. Hand off faithfully

After confirmation, provide the smallest faithful input for the adopted next route. A Mission Brief handoff preserves:

- the adopted result and intent;
- route and topology;
- adopted decisions and delegated choices;
- success meaning and any adopted proof expectation;
- boundaries, exclusions, compatibility, and authority;
- necessary source pointers with their actual authority status; and
- remaining uncertainty explicitly delegated or accepted as non-blocking.

Keep implementation plans, milestone sequences, preferred architectures, and unadopted approaches outside the handoff. The handoff is input to `mission-brief`, not the Brief itself and not execution authorization.

Default to a conversational handoff. Persist a **Mission Alignment Handoff** only when losing the conversation could change the result, boundary, authority, topology, or recoverability of completed material investigation; when another session, task, or Agent must continue; or when the user explicitly requests it. Judge volume by information-loss consequence, not word count.

For persistence, honor the requested path, then an established repository convention. Otherwise use `docs/missions/<outcome-slug>/alignment.md` for an adopted Mission, or `docs/mission-alignments/<candidate-slug>.md` for incomplete alignment that must survive a session boundary. Clearly separate adopted decisions, confirmed facts and authority, candidate material, open decisions, and the recommended route. An incomplete handoff must state that no Mission has been aligned or authorized.

When Mission Briefing is the adopted next route, finish with an exact invocation the user can send, such as `$mission-brief 根据上面已确认的 Mission Alignment 生成 Brief`. Point to the confirmed conversation or durable handoff instead of restating the whole contract again.

Finish when the user can see the aligned state and boundary, and the next product can recover the adopted decisions without treating discussion as authority.
