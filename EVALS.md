# Mission Brief regression evals

Maintainer-only evaluation set for `mission-brief`. This file is not runtime instruction and should not be loaded while producing a brief.

## Protocol

Run each case in a fresh session with the same model, harness, workspace fixture, and Skill version. Invoke cases 2–12 explicitly as `/skill:mission-brief <prompt>`; cases 1 and 13 verify that natural-language requests do not load this user-invoked Skill. Capture invocation, artifact content, write location, and final response. When tuning the Skill, change one instruction group at a time and rerun all cases.

A run passes only when both its case-specific expectation and every invariant below hold.

## Global invariants

- The Skill triggers only for preparing a commission for another agent.
- Exactly one brief is produced, inline or at the expected path.
- A fresh agent can identify the target, outcome, boundaries, authority, and credible completion evidence.
- The brief contains assertions rather than phases, implementation steps, tasks, or checkboxes.
- Proposed solutions and discoverable unknowns remain delegated unless the user or an external contract makes them binding.
- Evidence challenges the delivered outcome through task-appropriate signals; visible tests are not treated as the complete definition of success.
- Authoritative repository material is referenced with only its delivery consequence summarized.
- The artifact is materially shorter and clearer than its source discussion without losing confirmed intent.

## Cases

### 1. Ordinary implementation request does not trigger

**Prompt:** `修复登录页在 Safari 下无法提交的问题，并运行相关测试。`

**Expected:** The agent performs the requested work normally. It does not create a Mission Brief.

### 2. Small bug commission stays small

**Prompt:** `不要现在修。整理成一份可以直接交给另一个 Agent 的委托：Safari 下登录表单按回车没有提交，Chrome 正常；不能改变鼠标点击提交的行为。`

**Expected:** A compact brief describes the observable regression, compatibility boundary, and representative verification. It does not invent architecture or expand into a general form rewrite.

### 3. Complex capability does not become an implicit task list

**Prompt:** Provide a long discussion of a competitor-research capability containing user outcomes, examples of research topics, suggested worker lanes, possible registry fields, existing workflow boundaries, and several candidate architectures; ask for an agent-ready Mission Brief.

**Expected:** Durable research behavior, evidence provenance, workflow boundaries, and explicitly confirmed mechanisms remain. Lane taxonomies, registry field inventories, orchestration topology, and candidate architecture are compressed into principles or delegated decisions unless explicitly fixed.

### 4. Explicit architecture decision remains binding

**Prompt:** `生成 Mission Brief。由于现有审计合同明确要求所有付款事件写入 PostgreSQL，必须继续使用 PostgreSQL；缓存可以考虑 Redis，但我没有决定。`

**Expected:** PostgreSQL appears as a constraint with its rationale. Redis appears only as a preference or delegated option.

### 5. Examples do not become an exhaustive taxonomy

**Prompt:** `准备一份 Agent 委托。导出能力需要支持订单，未来可能还有退款、发票、订阅等对象；这次确认只交付订单导出。`

**Expected:** Order export is the outcome. Other objects define scope context or non-goals, not required behaviors to implement.

### 6. Tests remain evidence

**Prompt:** `整理成 Mission Brief：修复金额舍入错误。仓库里现有测试只覆盖 1.005 和 2.675，但正确行为必须适用于所有合法两位小数金额。`

**Expected:** Evidence includes representative and boundary coverage without defining the implementation around the two visible cases.

### 7. Authoritative artifacts are referenced

**Fixture:** A repository contains `AGENTS.md` and `docs/contracts/payments.md` with detailed established rules.

**Prompt:** `根据我们刚才的支付重试讨论生成 Mission Brief，已有仓库合同继续有效。`

**Expected:** The brief points to both authoritative artifacts and summarizes only consequences relevant to the commission. It does not reproduce either document.

### 8. Inline output writes no file

**Prompt:** `在回复里直接给我 Mission Brief，不要创建文件：为后台列表增加空状态。`

**Expected:** One complete inline brief and no workspace write.

### 9. Default path respects repository scope

**Fixture:** A monorepo with `packages/billing/docs/`; the commission affects only billing and no existing brief convention is present.

**Prompt:** `为这个 billing 改动准备一份可直接执行的 Mission Brief。`

**Expected:** The artifact is saved under `packages/billing/docs/mission-briefs/<specific-slug>.md`.

### 10. Same commission updates; different commission distinguishes

**Fixture:** `docs/mission-briefs/password-reset-rate-limit.md` already exists.

**Prompt A:** `根据刚确认的限流阈值修订现有密码重置委托。`

**Expected A:** The existing commission is updated.

**Prompt B:** `为登录失败限流生成一份 Mission Brief。`

**Expected B:** A separately named brief is created; the password-reset brief is preserved.

### 11. Partial intent may trigger one blocker question

**Prompt:** `整理成给 Agent 的委托：我们要更换账户删除行为，但还没决定是立即硬删除还是提供 30 天恢复期。`

**Expected:** The Skill triggers despite unsettled intent and asks one focused product question because the alternatives produce materially different outcomes. It does not draft competing implementations.

### 12. Discoverable unknown does not block

**Prompt:** `生成 Mission Brief：让现有 CLI 支持 JSON 输出。具体命令入口和测试框架你让执行 Agent 自己从仓库调查。`

**Expected:** No clarification question. Command location, internal design, and test framework remain delegated.

### 13. Natural-language handoff or brief requests do not auto-invoke

**Prompt A:** `把当前工作整理成 Handoff，方便另一个 Agent 继续。`

**Prompt B:** `把这个需求整理成一份 Mission Brief。`

**Expected:** `mission-brief` is not loaded for either prompt. The user must invoke `/skill:handoff` or `/skill:mission-brief` explicitly; no model-invoked Skill substitution occurs.

## Review record

For each Skill revision, record model and harness versions, cases passed, observed regressions, and the single instruction group changed. Promote a new instruction into `SKILL.md` only after a representative failure demonstrates that the existing Skill does not already produce the desired behavior.
