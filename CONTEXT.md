# Mission Commissioning

This context defines the language used to commission, hand off, and review independently verifiable Agent results. It separates the stable promise from useful execution knowledge and from the records created while fulfilling that promise.

## Language

**Mission**:
An adopted commission for one independently verifiable change in user or system reality.
_Avoid_: Task, project, work item

**Mission Brief**:
The normative artifact that records a Mission's outcome, success meaning, proof obligations, hard boundaries, and commission-specific authority.
_Avoid_: Final plan, implementation brief, requirements summary

**Parent Mission**:
A Mission Brief in the parent role, owning an irreducible integration result, cross-result invariants, seam evidence, and concise result boundaries. The artifact title is `# Mission Brief: <outcome>`, the same as any other Brief. The parent role is marked by `Result Boundaries`, not a numbered name. When reading an existing Brief, treat `# Mission 0:` as a legacy parent-role title.
_Avoid_: Mission 0, Phase 0, root, master plan, program folder

**Child Mission**:
An independently verifiable Mission commissioned within a Result Boundary of an adopted Parent Mission while preserving the applicable parent invariants. The artifact title is `# Mission Brief: <outcome>`; the child role is marked by a `Parent Mission` link.
_Avoid_: Subtask, Mission 1, sub, implementation phase

**Authority Source**:
A user decision, repository contract, governance decision, or other applicable source whose adopted content may bind a Mission.
_Avoid_: Background material, helpful reference

**Reference Source**:
A durable source of useful facts, dependencies, risks, rationale, examples, or candidate approaches that does not become binding merely because it is preserved or linked.
_Avoid_: Requirement, approval, authorization

**Information Home**:
The single durable destination of material information: the Mission Brief, a labeled durable source, a consequential decision still to settle, or a justified omission.
_Avoid_: Duplicate requirements, preservation without authority status

**Mission Package**:
The logical set of a Mission Brief and any linked context, working records, and Closure Reviews needed across commissioning, execution, and review. Its members retain their own authority rather than inheriting authority from the package.
_Avoid_: Single combined document, mandatory folder template

**Blind Handoff**:
A check that a capable fresh Agent can recover the Mission contract and locate necessary durable context without the source conversation, while distinguishing authority from reference and retaining freedom to choose a viable route.
_Avoid_: Document completeness check, wording comparison
