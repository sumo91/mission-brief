# Mission Align Skill Specification

Status: confirmed on 2026-09-02; amended by the user-approved [Astra adaptation](mission-skills-astra-adaptation.md) and [simplification implementation](mission-skills-simplification-plan.md) on 2026-09-05. Current rules below count explicit original decisions as adoption and preserve user-requested confirmation.

## 1. Purpose

`mission-align` is an optional pre-commissioning Skill for the Mission system. It helps the user and Agent reach one explicitly confirmed understanding of:

- what the user actually wants to become true;
- which ambiguities, contradictions, disagreements, or authority questions materially change that result;
- whether the work should enter the Mission system and whether a Mission Brief is useful now;
- whether the result is one Mission, several independent Missions, or a Parent Mission with Child Missions; and
- which decisions and boundaries have been adopted for handoff to `mission-brief`.

It owns exploratory alignment. `mission-brief` continues to own the normative result contract.

## 2. User problem

The current `mission-brief` correctly stops when a consequential choice would change the contract, but its normal path is convergent: find the smallest missing decision, settle it, and write one Brief. Some commissions need a prior divergent phase in which the Agent helps the user discover what the disagreement really is, compare interpretations, and decide what should be commissioned.

Without a distinct alignment phase, the system can:

- turn an unclear wish into a falsely precise contract;
- ask the user for facts an executing Agent should discover;
- silently choose among conflicting interpretations;
- use a Mission Brief where the user actually needs research, advice, design, or direct work;
- split work by size, components, or phases instead of result topology; or
- claim alignment while a consequential interpretation or requested confirmation remains unsettled.

## 3. Adopted product decisions

The following decisions are already confirmed:

1. The Skill is named `mission-align` and is presented to users as **Mission Align / 任务对齐**.
2. Users may invoke it manually. `mission-brief` may also reach it when consequential ambiguity requires more than one small clarification.
3. Its scope is balanced: it may discuss solution directions to expose different goals and tradeoffs, but it binds a solution only when the user explicitly adopts that solution as part of the result or boundary.
4. It surfaces material ambiguity, contradiction, disagreement, authority conflict, and obvious unanswered questions instead of silently resolving them.
5. It helps unclear goals become concrete, but does not claim privileged access to the user's “true desire.” The Agent proposes interpretations; the user adopts one.
6. It distinguishes user decisions from safely discoverable facts. Product-neutral implementation, root cause, edit location, tools, and other safe execution-time discoveries remain delegated.
7. It always communicates the current alignment state and task boundary in plain language.
8. `ALIGNED` requires all consequential decisions to be explicitly adopted or settled within delegation. Original user instructions count as adoption of the decisions they settle; a synthesis adding no consequential interpretation needs no repeat confirmation. New choices, authority conflicts and user-requested confirmation remain pending. Complete amendments may adopt the unaffected remainder; hints, tentative suggestions and silence do not settle an open choice.
9. The default handoff is in the current conversation. A durable handoff is created only for material-volume risk, cross-session or cross-Agent continuity, or an explicit user request.
10. It judges Mission suitability and result topology. Already explicit route and topology decisions remain adopted; a new consequential proposal needs adoption or an applicable delegation.

## 4. Invocation and discovery

`mission-align` must be model-invoked rather than user-only because another Skill needs to reach it. Its `agents/openai.yaml` therefore keeps `allow_implicit_invocation: true`, while Mission Brief and Mission Review keep that policy `false`. Manual `$mission-align` invocation remains available.

Confirmed model-facing description:

```yaml
description: Align an unclear or contested Mission commission before briefing.
```

The description should not cause ordinary implementation requests to enter alignment automatically. Autonomous invocation is appropriate when:

- `mission-brief` encounters several coupled consequential decisions;
- the user states a symptom, artifact, activity, or solution but no stable observable result;
- different plausible interpretations imply different outcomes, success meanings, boundaries, authority, or topology;
- the user asks to explore what they really want before commissioning work; or
- the user explicitly invokes `$mission-align`.

`mission-brief` retains a lightweight direct path:

- a settled commission proceeds directly to briefing;
- one bounded missing decision may be asked and settled locally;
- deeper exploration routes to `mission-align` when it is available;
- if `mission-align` is unavailable, `mission-brief` keeps its present safe behavior: write nothing and request the smallest decision that can settle the contract.

`mission-brief` remains explicitly invoked. If that invocation routed into alignment, resume the already-authorized Brief after adoption without requesting the same invocation again. For an alignment-only request, return the handoff and an exact next invocation such as `$mission-brief 根据上面已确认的 Mission Alignment 生成 Brief`. Resume neither cancelled work nor a product the user has not authorized.

## 5. Operating model

Use an adaptive alignment dialogue. Its order and depth follow actual gaps; no fixed questionnaire, per-question checklist, or repeated summary is required.

### 5.1 Recover result, route and topology

Distinguish adopted decisions, confirmed facts and applicable authority, candidate interpretations, consequential open choices, and safely discoverable implementation facts. Explain the candidate result and material uncertainty in ordinary language.

Choose the useful next product: exploration, research or advice, a design or final plan, direct work, or Mission Briefing. An alignment-only request ends with a handoff; any already-authorized next product belongs to the original request's next phase. A small task can be a valid Mission while adding little value from a Brief.

One independently verifiable result remains one Mission regardless of component count, phases or work volume. Several independently valuable results need separate Missions unless an adopted irreducible overall result needs its own verdict. Parent Mission requires a concrete case where all local results pass but the whole still fails; make its result boundaries and cross-result invariants visible. New consequential topology remains a proposal until adopted or decided within delegation.

Optional readiness labels are `EXPLORING`, `DECISION NEEDED`, `BLOCKED`, and `ALIGNED`; user-facing wording should explain what is settled and what is missing.

### 5.2 Resolve only consequential choices

Ask when alternatives change the result, success meaning, proof expectation, boundary, topology, authority, or preservation of material information. Explain the actual consequence; offer options or a recommendation when they help. Discuss coupled choices together when separating them hides the tradeoff. Root cause, tools, edit location and product-neutral architecture remain execution choices when safely discoverable.

State the scope of a delegation and choose within it. Continue proportionate, authorized investigation that does not depend on a pending answer; dependent work waits. An unavailable external authority remains a real blocker rather than a choice the Agent may waive.

### 5.3 Adopt and hand off once

Use one concise synthesis as the handoff. It preserves the result and intent, selected route and topology, success and adopted proof expectations, boundaries and compatibility, authority and delegated choices, adopted solution constraints, necessary source pointers and their status, and non-blocking uncertainty. Include only material dimensions; unadopted implementation routes stay outside the handoff.

The user's explicit original instructions adopt the decisions they settle. If the synthesis adds no new consequential interpretation, hand it off directly. Ask for a new consequential choice or authority conflict, or when the user explicitly requested a summary for confirmation. A complete amendment can adopt the revised synthesis and its unaffected remainder. Tentative suggestions, silence and partial agreement cannot settle an open choice or authorize a change.

Reuse the synthesis itself, adding only necessary persistence or source pointers. Persistence follows section 7. For an already-invoked Brief, return to that request and complete the authorized Brief without a duplicate invocation. For alignment-only work, provide the handoff and an exact next invocation when useful. Existing execution authority survives; handoff creates none and cancelled work stays cancelled.

Alignment is complete when all consequential decisions are adopted within applicable authority and the next product can recover them without treating discussion as authority. Otherwise identify the remaining choice or blocker and who can resolve it.

## 6. Plain-language interaction contract

User-facing conversation should favor sentences such as:

- “我目前理解你真正想改变的是……”
- “这里有两种理解，它们会导致不同的成功标准。”
- “如果选 A，意味着……；如果选 B，意味着……”
- “我的建议是……，因为……”
- “目前已经对齐的是……，还没有决定的是……”
- “这件事适合写 Mission Brief，但现在还差一个会改变边界的决定。”

Terms such as result topology, commission boundary, proof burden, authority source, and cross-result invariant remain internal unless the term itself helps the user decide. When used, explain it with a concrete example in the same reply.

Plain language must preserve precision. It does not permit hiding uncertainty, omitting consequences, or replacing an explicit decision with a friendly-sounding assumption.

## 7. Handoff persistence

The default handoff remains in the current conversation.

Persist a `Mission Alignment Handoff` only when at least one condition holds:

- losing the conversation could change the result, success meaning, boundary, authority, topology, or recoverability of completed material investigation;
- the alignment must survive a different session, task, Agent, or delayed continuation; or
- the user explicitly requests a durable artifact.

Material volume is judged by information-loss consequence, not word count.

When persistence is required, honor a user-requested path, then an established repository convention. Fallback locations are:

- `docs/missions/<outcome-slug>/alignment.md` after the Mission has been explicitly adopted; or
- `docs/mission-alignments/<candidate-slug>.md` when alignment is still incomplete but must survive a session boundary.

A persisted handoff clearly separates:

- current status;
- adopted decisions;
- confirmed facts and applicable authority;
- candidate interpretations or approaches;
- open decisions and blockers; and
- the recommended next route.

Persistence never promotes candidates or discussion into authority. An incomplete handoff must visibly state that no Mission has yet been aligned or authorized.

## 8. Boundaries and non-goals

`mission-align` does not:

- write or silently substitute a Mission Brief;
- create a final design, implementation plan, milestone plan, or execution record;
- execute the requested Mission;
- review a completed Mission;
- force every request into the Mission system;
- make a parent Mission from size, complexity, or organization structure;
- require users to decide safely discoverable implementation facts;
- claim certainty about unstated user intent; or
- create a durable artifact by default.

It may recommend a separate research, design, planning, review, or execution product. Alignment-only work stops at handoff; the original request resumes any already-authorized next product after alignment.

Adopting a route does not expand execution authority. The original request and any later explicit authorization continue to determine whether another product may be created or work may begin.

## 9. Confirmed repository and runtime changes

The first implementation should remain small and self-contained:

```text
mission-align/
├── SKILL.md
└── agents/
    └── openai.yaml
```

No scripts, assets, or separate references are required initially. Split a topology or persistence reference only if the finished `SKILL.md` becomes difficult to follow or behavioral evaluation shows that branch-specific detail distracts from the main dialogue loop.

Additional repository changes:

1. Update the root `mission-brief` Skill with a narrow routing rule for deeper ambiguity and an unavailable-skill fallback.
2. Add `Mission Alignment` and, if retained as a canonical term, `Mission Alignment Handoff` to `CONTEXT.md`.
3. Update `README.md` with the three-Skill lifecycle and invocation behavior.
4. Add maintainer-only behavioral scenarios for `mission-align` and for the `mission-brief` routing seam.
5. Update installation and synchronization instructions for the optional runtime package.

`mission-align/agents/openai.yaml` should use:

```yaml
interface:
  display_name: "Mission Align"
  short_description: "Clarify and confirm a Mission before briefing"
  default_prompt: "Use $mission-align to clarify this request and confirm its Mission boundary before briefing."
policy:
  allow_implicit_invocation: true
```

## 10. Behavioral evaluation contract

The initial evaluation set should include at least these scenarios:

1. **Clear single Mission:** hands off a compact synthesis directly from explicit decisions without repeat confirmation, new product questions or topology ceremony.
2. **Unclear desired result:** explores the user-visible change instead of turning an artifact or activity into the outcome.
3. **Conflicting interpretations:** explains the consequence of each interpretation and obtains a user choice.
4. **Discoverable implementation facts:** leaves root cause, edit location, architecture, and tools to execution.
5. **Different requested product:** recommends research, design, advice, planning, or direct work when a Brief is not the next useful product.
6. **Brief optional:** explains why a low-risk immediate change may not justify contract overhead.
7. **Complex single result:** keeps one Mission despite many components and proof categories.
8. **Unrelated results:** recommends independent Missions and does not manufacture Parent Mission.
9. **Pending integration result:** exposes a candidate Parent Mission, result boundaries, and seam invariants for adoption.
10. **Delegated decision:** records only the scope the user explicitly delegated.
11. **Authority conflict:** identifies the unavailable decision-maker and remains blocked.
12. **User-requested confirmation:** waits when the user explicitly requested a summary for confirmation; silence or partial agreement does not settle that pending decision.
13. **Correction after synthesis:** accepts an explicit amendment and the adopted remainder; asks only about new consequential ambiguity or conflict. Tentative suggestions do not change the contract.
14. **Conversational handoff:** creates no file by default.
15. **Durable handoff:** persists material mixed-status information without promoting candidates into authority.
16. **Mission Brief seam:** deeper ambiguity reaches `mission-align`; a settled commission and one small bounded question stay in `mission-brief`.
17. **Unavailable optional Skill:** `mission-brief` safely falls back to its present clarification gate.
18. **Return by original scope:** an already-invoked Brief resumes after adoption; alignment-only gives the next invocation; cancelled work stays cancelled.
19. **Plain language:** the user can understand the current state, choice, consequence, and boundary without Mission-system vocabulary.

A release candidate fails when it:

- declares alignment with a new consequential choice, authority conflict or user-requested confirmation still unresolved;
- writes a Mission Brief before alignment or beyond the original authorization, or starts uncommissioned implementation;
- silently chooses a consequential interpretation;
- asks the user for safely discoverable implementation facts;
- recommends topology from size or organization structure;
- loses adopted decisions or material authority in handoff;
- turns candidate approaches into binding requirements; or
- creates persistence ceremony for an ordinary small alignment.

Natural wording, different numbers of dialogue turns, and defensible alternative option framing are allowed when the same adopted result and boundaries are preserved.

## 11. Completion criteria for implementation

Implementation is complete when:

1. the new Skill and UI metadata validate structurally;
2. manual invocation works and model invocation is discoverable from `mission-brief`;
3. direct, routed, and unavailable-Skill paths preserve the intended boundaries;
4. behavioral scenarios cover route, readiness, topology, explicit confirmation, plain language, and persistence;
5. the runtime package contains only files needed during alignment; and
6. a fresh explicit `mission-brief` invocation can recover the confirmed commission from the handoff without importing unadopted discussion or an implementation route.

## 12. Confirmed implementation baseline

The user confirmed the full behavior and responsibility boundary, model-invoked discovery policy, fallback persistence locations, and minimal runtime structure before implementation began.
