# Mission 0

Read this reference when several results can be accepted independently and the user has also adopted, or is considering, an overall result that may still fail after all local results pass.

It also applies to a later child tied to an approved Mission 0.

## Make the topology explicit

Before writing a parent Brief, show a compact result map:

```text
Candidate Mission 0: <the overall result that local success does not prove>

Result boundaries:
- <independently acceptable result>
- <independently acceptable result>

Cross-result invariants:
- <what must remain true through their connection>

Unsettled boundaries:
- <decision still needed, if any>
```

Treat the map as a proposal until the user adopts its overall result, displayed result boundaries, and cross-result invariants as one parent commission. When that packaging has not been adopted, stop after the map and ask whether to commission it while leaving each result boundary for a later independent Mission.

The map records result topology, not implementation order, ownership, milestones, or child contracts.

A requested parent label does not replace an integrated result the user actually values.

Topology adoption does not settle missing scope, authority, success meaning, or proof. Resolve those parent-level decisions under the main Skill before writing.

## Write the parent contract

Mission 0 owns the irreducible integration outcome, cross-result invariants, seam evidence, program-wide boundaries, and concise result boundaries.

Use `# Mission 0: <integration outcome>` as the parent title. The distinct title makes the parent role visible to humans while the filename remains the uniform `brief.md` used by every Mission contract.

Add this section after `Boundaries`:

```markdown
## Result Boundaries
<One observable line for each result that will be commissioned separately.>
```

Center parent `Success` on what must remain true across identity, authority, state, continuity, or other relevant seams. Require evidence capable of falsifying the integrated claim.

Passing every child locally is supporting evidence, not parent proof.

Keep child-local success, evidence, and design choices in later child Briefs. When confirmed child-local decisions are omitted from Mission 0, point from parent `Context` to a durable Authority Source that preserves them. Label useful non-binding plans or investigation records as Reference Sources rather than allowing a link to promote them into the parent contract.

If no durable source exists, ask whether to create an appropriate durable Authority Source or leave the child-local contract unsettled for confirmation when that child is commissioned. Do not copy child-local obligations into the parent merely to avoid this disposition decision. A temporary path or source conversation alone does not complete the handoff.

Deferring child commissioning is not an information-disposition decision. When confirmed child-local obligations exist only in transient context, write no parent Brief until the user explicitly chooses durable preservation or explicitly accepts that those obligations remain unsettled and must be confirmed again when each child is commissioned.

If the topology is already adopted and only this preservation disposition remains open, do not repeat the topology as a `Candidate Mission 0`, draft parent, section outline, or fenced result map. Briefly identify the blocked parent outcome, state that confirmed child-local obligations would otherwise be lost, and ask only whether to preserve them in a durable Authority Source or leave them unsettled for later confirmation. Any child-local examples used to identify the at-risk information remain outside the parent contract.

A child clause belongs in the parent only when violating it would independently falsify the integrated result. A later child Brief remains self-contained, preserves applicable parent invariants, and leaves Mission 0 unchanged unless the approved topology or parent contract changes.

If an existing parent Result Boundary already contains a valid link to the commissioned child path, do not edit the parent merely to rename, relabel, or announce that link. Change the parent only when its contract or adopted topology changes, or when a required bidirectional link is absent or invalid.

## Store the topology

Mission 0 uses the same `brief.md` artifact as any other Mission Brief. At one documentation boundary, store it at `docs/missions/<integration-outcome-slug>/brief.md`; place a commissioned child at `children/<child-outcome-slug>/brief.md`, link its parent Result Boundary to it, and link the child back through `Parent Mission`.

When children belong to different packages or repositories, keep each Brief at the documentation boundary that owns its result. Store Mission 0 at their lowest common authority boundary and carry the topology through explicit bidirectional links rather than forced physical nesting.

In saved documents, every parent, child, and source link must be repository-relative and resolve from that document. Never embed a temporary or scratch absolute path.

Do not create empty child directories for uncommissioned Result Boundaries. Mission 0 is a parent role in result topology, not a global `mission-0.md` filename, phase number, implementation program, or ownership tree.
