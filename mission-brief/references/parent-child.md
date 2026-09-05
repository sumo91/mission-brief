# Parent and Child Missions

Use this branch for a Parent Mission with an adopted overall result that can still fail after every local result passes, or for a Child Mission explicitly commissioned within such a parent. Older Briefs call this parent role `Mission 0`.

## Adopt the result topology

If a new parent's integration result and boundaries have not already been adopted, show the user a compact proposal containing:

```text
Integration result: <overall result not proved by local success alone>

Result boundaries:
- <independently acceptable result>

Cross-result invariants:
- <what must remain true through their connection>
```

Write the parent after the user adopts the integration result, boundaries, and cross-result invariants. Resolve any remaining Contract Core or authority decision through the main Skill.

## Write the parent

Make the parent role explicit in the title, for example `# Parent Mission: <integration result>`, and add `## Result Boundaries` after the Contract Core. Center parent `Success` and evidence on the identity, authority, state, continuity, or other seam that creates integrated value.

A parent clause belongs only when violating it would falsify the integration result. Child-local success, evidence, and design belong to self-contained child Briefs. Keep confirmed child contracts that are not yet commissioned in a durable Authority Source; keep useful non-binding plans and investigation in Reference Sources.

A later child preserves applicable parent invariants. Leave an already-linked parent unchanged unless its contract, adopted topology, or a required link actually changes.

## Store the topology

Parent and Child Missions use the same `brief.md` artifact:

```text
docs/missions/<integration-outcome-slug>/brief.md
docs/missions/<integration-outcome-slug>/children/<child-outcome-slug>/brief.md
```

Link every commissioned boundary to its child and every child back through `Parent Mission`. Across package boundaries, keep each Brief where its result is owned, place the parent at the lowest common documentation boundary, and express topology with repository-relative links.

Create child directories only for commissioned results. Add or edit an index only when the user requests it or the repository requires it.

This branch is complete when the parent can receive an independent integration verdict, each child can recover its applicable invariants, and the stored links describe the adopted result topology.
