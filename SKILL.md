---
name: mission-brief
description: Create one self-contained Mission Brief for a fresh agent.
disable-model-invocation: true
---

# Mission Brief

Use **mission command**: define the outcome, boundaries, authority, and credible evidence; leave the route to the agent with the freshest context. Produce one artifact, not a plan or task list.

## 1. Frame the commission

Ground the brief in the conversation, named artifacts, and only enough workspace inspection to identify the target, current behavior, and established constraints. Reference authoritative repository material instead of reproducing it.

Apply the **commission test** to each material statement:

- **Outcome:** changing it would change what the user or system can observe.
- **Constraint:** the user explicitly fixed it, or an external contract imposes it.
- **Delegation:** it is a preference, example, proposed solution, implementation choice, or discoverable unknown.

Detail does not make a proposal binding. Preserve preferences as decision principles. Ask one focused question only when unresolved user judgment leaves materially different valid outcomes; delegate everything the executing agent can resolve from evidence.

Completion criterion: one coherent outcome exists, every material statement has one home, and no user-only decision blocks delivery.

## 2. Write the brief

Write for a fresh capable agent with access to the target environment but none of this conversation. Omit optional sections that carry no information. Use bullets as assertions, not as an execution sequence.

```markdown
# Mission Brief: <observable outcome>

## Outcome
<What becomes possible or true at the user or system boundary.>

## Context
<Motivation, target environment, confirmed facts, and pointers to authoritative artifacts.>

## Required Behaviors
<The minimum representative scenarios and durable invariants that distinguish success from a plausible but wrong result.>

## Constraints
<Only binding product, compatibility, safety, permission, or external-contract boundaries.>

## Non-goals
<Adjacent outcomes intentionally outside this commission. Omit when obvious.>

## Evidence of Completion
<A task-appropriate body of evidence that challenges the real outcome from useful independent angles. Tests may contribute evidence but do not define the solution.>

## Delegated Decisions and Unknowns
<Solution-shaping choices and discoverable unknowns, with decision principles where known.>

## Autonomy and Approval Boundaries
<Authorized local reversible action, and actions requiring confirmation because they are external, destructive, costly, irreversible, or scope-expanding.>

## Execution Directive
You own delivery of the outcome above. Investigate the relevant environment, choose an efficient path consistent with its existing conventions, make the in-scope changes, and validate the result with evidence appropriate to the task.

Adapt the route as evidence appears. Preserve the Outcome and Constraints when assumptions conflict with repository facts, and report material divergence. Resolve discoverable implementation questions yourself; escalate only decisions requiring user judgment or approval.

Continue until the outcome is delivered and credibly verified. Report the result, evidence, and remaining uncertainty.
```

Completion criterion: a fresh agent can identify the target, outcome, boundaries, authority, and completion evidence without inheriting a prescribed implementation route.

## 3. Compress and save

Reapply the commission test to every clause. Collapse operational inventories into the principle they serve, keep only examples that disambiguate that principle, and move solution shape back to delegation. A brief that reads like a subsystem design or acceptance checklist is not yet compressed.

Save exactly one Markdown artifact:

- Return it inline when the user asks for inline output or file writes are unavailable.
- Otherwise honor a requested path, then an established repository convention, then default to `docs/mission-briefs/<outcome-slug>.md` at the relevant repository or package documentation boundary.
- Form `<outcome-slug>` from concise, stable domain terms. When that path exists, update it only for the same commission; otherwise add a meaningful distinguishing term.

For a saved artifact, report its path plus any blocker or consequential assumption. For inline output, return the complete artifact plus those notices. This Skill ends after producing the brief; the brief itself is the complete commission for the executing agent.

Final completion criterion: exactly one minimal, self-contained, contradiction-free brief can be handed unchanged to a fresh agent.
