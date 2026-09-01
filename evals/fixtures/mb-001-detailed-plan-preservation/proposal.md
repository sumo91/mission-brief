# Legacy workflow retirement proposal

The repository currently exposes a `legacy-workflow` skill through the Agent catalog, a command wrapper, a generated installation mirror, and an importer that scans legacy folders. The user has adopted the result that the legacy workflow must no longer be available or return after future imports, while capabilities still used by supported skills remain available without broader permissions.

## Adopted decisions

- Remove the user-visible `legacy-workflow` entry and prevent future imports from recreating it.
- Preserve behavior still required by supported skills; do not remove shared capability merely because it was originally introduced for the retired entry.
- Keep the command wrapper, generated installation mirror, and Agent catalog behaviorally consistent with the adopted retirement.
- Do not broaden execution or repository permissions.
- Verification must exercise a clean import and a representative supported consumer rather than relying only on file absence.

## Confirmed investigation

- `svn-impact` and `release-audit` both call `scripts/scan_dependencies.sh`; deleting that script with the retired entry would break supported workflows.
- The importer classifies any directory under `legacy/` that contains `SKILL.md` as a pending import. Deleting only the runtime catalog entry causes the next import to recreate it.
- `bin/import-skills`, `.generated/skills/`, and the Agent catalog are separate entry points with different stale-state risks.
- A previous cleanup removed a legacy entry but left the generated mirror intact, so catalog-only checks produced a false pass.

## Candidate approaches not yet adopted

- Add a registry tombstone for `legacy-workflow` so the importer can distinguish retirement from a missing installation.
- Move `scripts/scan_dependencies.sh` into a neutral shared-tools package.
- Keep `svn-impact` and `release-audit` unchanged unless direct compatibility testing exposes a necessary adaptation.
- Add a repository-wide import simulator as a permanent regression harness.

These approaches are recommendations, not authorization. The executing Agent may choose another route that satisfies the adopted result and boundaries.

## Suggested investigation order

Inspect the importer classification first, then map every entry point and shared consumer, choose the smallest compatible retirement mechanism, and finally exercise clean import and supported consumers. This sequence is advisory and may change with repository findings.
