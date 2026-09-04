# Parent and Child Missions

Use this branch for an adopted overall result that can still fail after every local result passes, or for a child explicitly commissioned within such a parent.

Every Brief uses the same title form `# Mission Brief: <outcome>`. Parent and child are roles, not numbered names and not a separate file type. When reading an existing Brief, treat `# Mission 0:` as a legacy parent-role title with the same meaning.

## Adopt the result topology

Before writing a new parent, show the user a compact proposal containing:

```text
Parent result: <overall result not proved by local success alone>

Result boundaries:
- <independently acceptable result>

Cross-result invariants:
- <what must remain true through their connection>
```

Write the parent after the user adopts the integration result, boundaries, and cross-result invariants. Resolve any remaining Contract Core or authority decision through the main Skill.

## Write the parent

Use `# Mission Brief: <outcome>` and add `## Result Boundaries` after the Contract Core. Center parent `Success` and evidence on the identity, authority, state, continuity, or other seam that creates integrated value.

A parent clause belongs only when violating it would falsify the integration result. Child-local success, evidence, and design belong to self-contained child Briefs. Keep confirmed child contracts that are not yet commissioned in a durable Authority Source; keep useful non-binding plans and investigation in Reference Sources.

A later child preserves applicable parent invariants. Leave an already-linked parent unchanged unless its contract, adopted topology, or a required link actually changes.

## Write the child

Use the same `# Mission Brief: <outcome>` title. Add `## Parent Mission` with a repository-relative link to the parent Brief. Preserve applicable parent invariants; do not copy the parent's local child contracts or invent implementation order.

## Store the topology

The parent is the parent role of the same `brief.md` artifact:

```text
docs/missions/<integration-outcome-slug>/brief.md
docs/missions/<integration-outcome-slug>/children/<child-outcome-slug>/brief.md
```

Link every commissioned boundary to its child and every child back through `Parent Mission`. Across package boundaries, keep each Brief where its result is owned, place the parent at the lowest common documentation boundary, and express topology with repository-relative links.

Create child directories only for commissioned results. Add or edit an index only when the user requests it or the repository requires it.

This branch is complete when the parent can receive an independent integration verdict, each child can recover its applicable invariants, and the stored links describe the adopted result topology.
