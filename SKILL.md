---
name: mission-brief
description: Create one stable result contract for a capable fresh agent.
disable-model-invocation: true
---

# Mission Brief

Use **mission command**: specify the destination, proof, and hard boundaries—not the route. Treat the brief as a commission compressed after the material product decisions are settled, not as the sole memory for execution.

## 1. Qualify the mission

Ground the commission in the conversation, named artifacts, and only enough workspace inspection to locate the target, established contracts, and current reality.

Define one Mission as one coherent change in user or system reality that can receive an independent, honest verdict from a bounded body of complementary evidence. Diagnose its scale before drafting:

- **Mission:** the result has independent value, can independently fail, and changes observable capability, experience, risk, or trust—not merely the existence of an internal artifact.
- **Too broad:** the request contains several success centers that need materially different evidence or make failure attribution ambiguous. Select one coherent level. Create a parent Mission only when integration has a success claim that cannot be inferred by adding up child results.
- **Too narrow:** success means only that a file, class, field, test, or other implementation unit exists, or several proposed Missions share one verdict and evidence set. Treat these as execution work under one Mission.
- **Same commission:** implementation iterations, debugging, UI polish, and newly found defects stay under the existing Brief while destination, success, proof obligations, boundaries, and authority remain unchanged.

Run a **semantic closure test** before drafting: for each term that classifies admissible inputs, supported states, compatibility, identity, safety, failure, or success, verify that user decisions or authoritative repository material can classify plausible boundary cases. If two reasonable readings would change observable output, writes, rejection behavior, scope, or verdict, the term is an unresolved product contract—not delegation.

Run a **freeze gate** over every clause that would bind the destination, success meaning, proof obligations, boundaries, non-goals, or execution authority. Trace each clause to an explicit user decision, the user's explicit acceptance of a clearly enumerated summary, or an external contract. Let a faithful paraphrase inherit that provenance only if it neither adds, selects, nor strengthens meaning. Let proportionate, task-normal evidence that directly challenges a confirmed success claim inherit that claim's provenance; treat a new costly, subjective, or external proof obligation as synthesis. Treat recommendations, examples, preferences, critiques, risk hypotheses, proposed solutions, and agent-written summaries as discussion input until the user adopts them. Treat Skill invocation as a request to package confirmed decisions, not as adoption of earlier discussion.

Choose one gate state:

- **READY:** the commission is semantically closed and every binding clause has confirmed provenance. Draft and save without ceremonial reconfirmation.
- **CONFIRM:** the discussion supports one coherent commission, but faithfully stating it requires a binding clause derived through material agent synthesis—for example, an inferred non-goal, authority boundary, or high-cost evidence obligation. Use this state only when omitting the clause would materially misstate or under-specify the apparent commission; otherwise omit the unadopted material and choose `READY`. Return only a compact freeze summary of what will bind, what remains delegated, and which clauses are synthesized; ask one confirmation question. Produce no Brief yet.
- **BLOCKED:** multiple materially different commissions remain valid, a required semantic classification is missing, or confirmed requirements conflict. Ask one current blocking decision question. Produce no Brief yet.

Produce one Brief at the selected level, never a generated Mission tree, and resolve repository-discoverable questions yourself. A user confirmation of the freeze summary moves `CONFIRM` to `READY`; it does not confirm anything absent from that summary.

Completion criterion: the gate has one justified state. In `READY`, the commission has one success center, an independently supportable verdict, a stable route-free boundary, and traceable provenance for every binding clause; a fresh executor can classify representative success, boundary, and failure cases without inventing product policy. In `CONFIRM` or `BLOCKED`, this invocation ends after one question and no artifact.

## 2. Establish the contract

Make the **commission boundary** self-contained: without the original conversation or linked rationale, a fresh capable agent can identify the target, intent, desired outcome, success meaning, proof obligations, and hard boundaries. Point to repository sources for detailed facts and reasoning instead of copying them.

Assign authority by subject, not by a single priority ladder:

- The Mission Brief owns this commission's intent, destination, success meaning, proof obligations, scope, and granted authority.
- Repository contracts and current implementation own present system facts and compatibility reality.
- ADRs own recorded decisions and their rationale.
- Working plans, implementation ledgers, commits, and QA records own route, progress, discoveries, and interim evidence; they cannot redefine the commission or product facts.
- A Closure Report owns the final verdict, actual evidence, counterevidence, and remaining uncertainty.

Surface conflicts between authorities; never silently choose the convenient source. Preserve current facts and the commission separately, then seek user judgment only when both cannot be honored.

Apply the **contract test** to every material statement:

- **Destination:** changing it changes why the work matters, what becomes observable, or what an honest verdict means.
- **Proof:** it names evidence needed to support or falsify the destination.
- **Boundary:** the user or an external contract fixes a product, safety, permission, data, compatibility, governance, resource, or scope limit.
- **Delegation:** it is a preference, example, candidate solution, discoverable unknown, or implementation choice.

A mechanism belongs in the contract when the user or an external contract fixes it and substitution would change external reading, collaboration, compatibility, governance, or user-facing behavior. Preserve softer preferences only as decision principles. Express boundaries as risks and commitments to preserve rather than preselected call sequences.

Completion criterion: every material statement has one authoritative home, linked material adds depth rather than filling a missing commission boundary, and solution shape remains delegated unless externally binding.

## 3. Write the brief

Use the minimal structure below. Omit optional sections that carry no contract information. Use bullets as assertions, not as an execution sequence.

```markdown
# Mission Brief: <observable outcome>

## Intent
<Why this reality change is worth delivering.>

## Desired Outcome
<What becomes possible or true at the user or system boundary.>

## Success
<The minimum falsifiable facts and durable invariants that distinguish success from a plausible but wrong result.>

## Evidence Required
<The prospective, task-appropriate evidence categories needed for an honest verdict.>

## Boundaries
<Binding product, fact-authority, compatibility, safety, permission, data, governance, resource, and scope limits.>

## Non-goals
<Adjacent results this commission does not promise. Omit when obvious.>

## Context
<Only necessary target facts and pointers to authoritative material. Omit when the commission is already locatable.>

## Execution Authority
<Authorized reversible local action and the external, destructive, costly, irreversible, or scope-expanding actions that require confirmation. Omit when ambient authority is sufficient.>
```

When `Execution Authority` carries information, grant ownership of investigation, planning, implementation, correction, and validation within the authorized scope. Treat internal phases as execution choices, not approval points.

Keep `Success` about facts that must hold and `Evidence Required` about how the final claim will be challenged. Specify evidence categories rather than test modules, commands, counts, hashes, or completed results. Calibrate evidence strength to failure impact, irreversibility, cross-system reach, and the share of subjective judgment. Require real supported environments, human judgment, independent review, negative paths, or compatibility checks only where cheaper deterministic evidence cannot support the claim.

Evidence must permit `PASSED`, `FAILED`, or `INCONCLUSIVE`. Missing required evidence, a violated boundary, an unmet success condition, or unexplained counterevidence blocks a successful verdict. Improvements that do not affect the contract may remain as reported limitations; completion does not require exhausting every possible refinement.

Completion criterion: a fresh agent can distinguish success from failure and choose credible proof without inheriting an acceptance checklist or prescribed implementation route.

## 4. Compress, save, and freeze

Run two final tests on every clause:

- **Route-freedom test:** could two equally capable agents choose materially different routes and both satisfy the Brief? If not, retain the restriction only when its external-contract reason is explicit.
- **Deletion test:** would removing the clause leave destination, verdict, proof, authority, or necessary task location unchanged? If yes, remove it.

Collapse operational inventories into the principle they serve. Rewrite interface and implementation prescriptions as observable results unless they pass the contract test. Remove repeated intent across `Success`, `Evidence Required`, and `Boundaries`. Treat roughly one page as a pruning signal, not a hard limit.

Save exactly one Mission Brief artifact only after the freeze gate reaches `READY`:

- Return it inline when the user requests inline output or file writes are unavailable.
- Otherwise honor a requested path, then an established repository convention, then default to `docs/mission-briefs/<outcome-slug>.md` at the relevant repository or package documentation boundary.
- Form the slug from concise, stable domain terms. Update an existing file only for the same commission; create a distinct file for a new independently signable outcome.

Keep the Brief stable during execution. Revise it only when intent, destination, success meaning, proof obligations, boundaries, or authority change, and identify that revision as a contract change. Working plans, implementation ledgers, QA artifacts, and Closure Reports may be created later; the one-artifact rule limits this Skill's commission output, not the execution record.

For a saved artifact, report its path plus any blocker or consequential assumption. For inline output, return the complete artifact plus those notices. This Skill ends after producing the commission; it does not implement the work or record progress.

Final completion criterion: exactly one minimal, self-contained, contradiction-free result contract can be handed unchanged to a capable fresh agent, while execution and closure records remain free to evolve beneath it.
