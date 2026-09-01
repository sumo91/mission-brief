# Runtime preflight before release evaluation

Status: live runtime rolled back to the committed historical baseline while the revised candidate is evaluated in isolation.

## Selected identities

- Repository baseline: `8adf782bf61e7051f9afe14d2e25166790e8bdc3`.
- Revised candidate runtime digest before freezing: `018df60e53aaeb22891d31714b6897c9889ff5fc4ddf141463360b966a3787a9`.
- Live Mission Brief location: `/Users/admin/.agents/skills/mission-brief`.
- Live Mission Review location: `/Users/admin/.agents/skills/mission-review`.

## Premature live state observed

Before rollback, the live runtime already contained an unfrozen revision:

| Runtime file | Observed SHA-256 |
|---|---|
| `mission-brief/SKILL.md` | `11a9f455c133e3794a780c102a0618959d35999447c855b753771d9c98538f56` |
| `mission-brief/agents/openai.yaml` | `5dc4b7d32e7175b072fbf31b2a4493cca00ba90f02209ace39e2a77d4e570921` |
| `mission-brief/references/mission-zero.md` | `121818f6bf8a8ff9be043c5cb9e9e44fd6cc856afc8fce28b5234c0ddb87710c` |
| `mission-review/SKILL.md` | `7efd502d167b0bfbe5c5451a7fa93f91aab59f53f1ea97bd67343033509c46ff` |
| `mission-review/agents/openai.yaml` | `44d1e768cc568f072119dcd8e6f3cd7a7c4b5abe2a276660bc98fc1cd04a807e` |

This state was not accepted as a release because it preceded a frozen candidate, executable evidence, and independent Closure.

## Rollback target

The live runtime was restored byte-for-byte from the detached worktree for baseline `8adf782`:

| Runtime file | Baseline SHA-256 |
|---|---|
| `mission-brief/SKILL.md` | `5972cc3b55e77025e8f36311ff1b150d5cd2d91c235b91e149571ce2bc61d667` |
| `mission-brief/agents/openai.yaml` | `2bc07b45b4e4935d06c103f54292359b50383dc1452eb9b1d0f9c1111194d465` |
| `mission-brief/references/mission-zero.md` | `60268a603b99805f00cce7b28483fa8f3ade78991abd79cbd6d0d3b2e30f21e4` |
| `mission-review/SKILL.md` | `de1c5f55dad8091c76fead408feb7f5c61d75180890713bbd00d2e0272707cd4` |
| `mission-review/agents/openai.yaml` | `44d1e768cc568f072119dcd8e6f3cd7a7c4b5abe2a276660bc98fc1cd04a807e` |

The release gate remains closed. The revised runtime may be synchronized only after the frozen candidate's static suite, two blind handoffs, durable evidence verification, and independent Mission Review all pass.
