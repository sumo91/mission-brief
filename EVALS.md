# Mission Brief regression evals

Maintainer-only evaluation set for `mission-brief`. This file is not runtime instruction and must not be loaded while producing a brief.

## Protocol

Run each case in a fresh session with the same model, harness, workspace fixture, and Skill version. Invoke every case except 1 and 24 explicitly as `/skill:mission-brief <prompt>`; cases 1 and 24 verify that natural-language requests do not load this user-invoked Skill. Capture invocation, questions, artifact content, write location, and final response.

A run passes only when both its case-specific expectation and every invariant below hold. After the authoring cases pass, run the blind-handoff check with a separate fresh agent that receives only the Brief, target workspace, and normal ambient instructions—not the source conversation or expected solution.

## Global invariants

- The Skill triggers only through explicit user invocation and prepares a commission for another agent.
- One coherent reality change supports one independently honest verdict; implementation units do not become Missions.
- The freeze gate reaches a justified state: `READY` produces exactly one Brief without ceremonial confirmation; `CONFIRM` or `BLOCKED` asks one question and produces no artifact. Optional unadopted synthesis is omitted rather than promoted into `CONFIRM`.
- The commission boundary is understandable without the source conversation; external references add detail and rationale.
- A fresh executor can classify representative success, boundary, and failure cases without inventing product policy.
- Every binding clause traces to an explicit user decision, explicit acceptance of a clear summary, or an external contract; unadopted advice, examples, preferences, critiques, and agent synthesis do not become contract.
- Before `READY`, proposed clauses are compatible with applicable repository contracts, compatibility commitments, and governance decisions, or carry an explicit authorized supersession; unresolved authority conflicts produce `BLOCKED`.
- The Brief contains stable assertions, not phases, status, implementation steps, task ownership, test commands, counts, hashes, or completed results.
- The Brief contains only the current effective contract; unadopted or superseded proposals, earlier draft states, and discussion history are absent unless a confirmed prohibition is itself binding.
- Confirmed external reading, collaboration, compatibility, governance, and user-facing mechanisms remain contractual; candidate solutions and discoverable unknowns remain delegated.
- `Success` defines falsifiable facts. `Evidence Required` names proportionate proof categories and permits `INCONCLUSIVE` without becoming an acceptance checklist.
- Repository facts, ADR rationale, execution records, and closure evidence retain their separate authority; conflicts are surfaced.
- A working plan, implementation ledger, QA artifact, or Closure Report may coexist with the Brief but cannot redefine it.
- The artifact is materially shorter and clearer than its source discussion, and two capable agents retain room to choose different valid routes.

## Cases

### 1. Ordinary implementation does not trigger

**Prompt:** `修复登录页在 Safari 下无法提交的问题，并运行相关测试。`

**Expected:** Perform the work normally. Do not load the Skill or create a Brief.

### 2. Small observable commission stays small

**Prompt:** `不要现在修。/skill:mission-brief Safari 下登录表单按回车没有提交，Chrome 正常；鼠标点击提交行为必须保持不变。`

**Expected:** Produce a compact result contract for the observable regression and compatibility boundary. Do not expand it into a form architecture or general rewrite.

### 3. Internal work item is not promoted into a Mission

**Prompt:** `/skill:mission-brief 新增一个 LoginSubmissionCoordinator 类，并给它加三个测试。`

**Expected:** Ask one question about the user/system outcome or explain that the input is execution work under an existing Mission. Do not manufacture a result contract around file and test existence.

### 4. Complex capability remains route-free

**Prompt:** Provide a long discussion of a competitor-research capability containing confirmed user outcomes, provenance requirements, suggested worker lanes, possible registry fields, existing workflow boundaries, and several candidate architectures; invoke the Skill.

**Expected:** Preserve the observable research result, evidence integrity, and workflow boundaries. Compress lanes, registries, orchestration, and candidate architecture into decision principles or delegation.

### 5. Explicit architecture contract remains binding

**Prompt:** `/skill:mission-brief 现有审计合同要求所有付款事件写入 PostgreSQL，必须继续使用；缓存可以考虑 Redis，但尚未决定。`

**Expected:** Keep PostgreSQL as a boundary with its external-contract reason. Leave Redis delegated.

### 6. Confirmed collaboration mechanism is not misclassified

**Prompt:** `/skill:mission-brief 新策划案必须以设计地图作为第一阅读入口；规则锚点必须稳定、可见、可复制；具体 Markdown 结构和锚点语法由执行者决定。`

**Expected:** Preserve the reading entry and anchor properties as success or boundary contracts. Delegate document topology and syntax.

### 7. Examples do not become a taxonomy

**Prompt:** `/skill:mission-brief 导出能力本次只交付订单；退款、发票、订阅只是未来可能支持的例子。`

**Expected:** Make order export the outcome. Treat other objects as context or non-goals, not required behaviors.

### 8. Evidence covers the claim, not visible tests

**Prompt:** `/skill:mission-brief 修复金额舍入错误。现有测试只覆盖 1.005 和 2.675，但正确行为适用于全部合法两位小数金额。`

**Expected:** Require representative and boundary evidence without defining the solution around the two visible cases or naming a test file.

### 9. Evidence cost is calibrated

**Prompt:** `/skill:mission-brief 给本地 CLI 增加确定性的 --version 输出；失败只影响开发者读取版本号。`

**Expected:** Require cheap deterministic verification and relevant compatibility evidence. Do not demand independent reviewers, broad human testing, or unrelated end-to-end journeys.

### 10. Subjective success receives independent evidence

**Prompt:** `/skill:mission-brief 让系统关系图在桌面和手机上成为无需开发者解释即可使用的日常阅读入口。`

**Expected:** Require real viewport and human-readable evidence proportionate to the subjective and cross-device claim while leaving layout and controls delegated.

### 11. Authority references preserve a self-contained boundary

**Fixture:** A repository contains `AGENTS.md`, `docs/contracts/payments.md`, ADRs, and an implementation ledger.

**Prompt:** `/skill:mission-brief 根据刚确认的支付重试讨论准备委托；已有仓库合同继续有效。`

**Expected:** State the commission boundary without requiring the original discussion, point to authoritative sources for detail, and keep the ledger as progress evidence rather than product authority.

### 12. Inline output writes no file

**Prompt:** `/skill:mission-brief 在回复里直接给我，不要创建文件：为后台列表增加明确的空状态。`

**Expected:** Return one complete inline Brief and make no workspace write.

### 13. Default path respects repository scope

**Fixture:** A monorepo with `packages/billing/docs/`; no existing Brief convention.

**Prompt:** `/skill:mission-brief 为 billing 的可观察结果准备委托。`

**Expected:** Save under `packages/billing/docs/mission-briefs/<specific-slug>.md`.

### 14. Same commission revises; new outcome distinguishes

**Fixture:** `docs/mission-briefs/password-reset-rate-limit.md` exists.

**Prompt A:** `/skill:mission-brief 根据刚确认的限流阈值修订现有密码重置委托。`

**Expected A:** Update the existing commission and identify the contract change.

**Prompt B:** `/skill:mission-brief 为登录失败限流生成委托。`

**Expected B:** Create a distinct Brief and preserve the password-reset commission.

### 15. Product ambiguity asks one question per round

**Prompt:** `/skill:mission-brief 更换账户删除行为，但尚未决定立即硬删除还是提供 30 天恢复期。`

**Expected:** Ask only the current blocking product question and produce no competing or premature Brief. A later round may ask another blocker if one remains.

### 16. Discoverable unknown does not block

**Prompt:** `/skill:mission-brief 让现有 CLI 支持 JSON 输出。命令入口和测试框架由执行者从仓库调查。`

**Expected:** Ask no clarification question. Leave location, framework, and internal design delegated.

### 17. Undefined validity blocks drafting

**Fixture:** A repository contains sample schema-v1 session records and a migration contract that names the source version and target transform but does not define valid source field types, extra-field policy, or identifier uniqueness.

**Prompt:** `/skill:mission-brief 将所有合法 schema-v1 session 迁移成 schema-v2；非法记录必须整体拒绝，不能产生部分目标。`

**Expected:** Ask one current blocking question about the authoritative validity contract and produce no Brief. Do not let the executing agent invent which records are legal.

### 18. Defined validity does not trigger clarification

**Fixture:** A repository contract defines every required schema-v1 field and type, identifier uniqueness, and that unknown fields are valid but omitted from the schema-v2 projection.

**Prompt:** `/skill:mission-brief 将所有合法 schema-v1 session 迁移成 schema-v2；非法记录必须整体拒绝，不能产生部分目标。`

**Expected:** Ask no clarification question. Preserve the repository's validity and projection policy in the result contract while delegating validation and publication mechanics.

### 19. Explicitly accepted summary is ready

**Conversation:** The agent presents a clearly enumerated summary: every accepted order appears exactly once in a JSON export within five minutes; terminal failures are visible to operators; PostgreSQL remains the audit store; refunds are out of scope; serialization mechanics stay delegated. The user replies, `就按以上五点形成 Mission Brief。`

**Prompt:** `/skill:mission-brief 生成并保存委托。`

**Expected:** Reach `READY` and produce one Brief without another confirmation. Preserve exactly the accepted contract and do not infer additional obligations from earlier discussion.

### 20. Brainstorming recommendation remains unbound

**Conversation:** The user explicitly chooses asynchronous order export in which every accepted order appears exactly once within five minutes and terminal failures are visible to operators; existing audit behavior and human-readable export remain compatible. During brainstorming, the agent recommends Kafka and a three-worker topology, but the user neither accepts nor rejects those ideas.

**Prompt:** `/skill:mission-brief 把已经确定的委托整理出来，具体实现交给执行 Agent。`

**Expected:** Reach `READY` without confirmation. Preserve the chosen export outcome; keep Kafka and worker topology delegated rather than turning them into boundaries or success conditions.

### 21. Grill critique remains review input

**Conversation:** The user confirms a local read-only glossary-search CLI and its output compatibility boundary. During a grill, the agent warns that SQLite could harm portability and calls an independent security review desirable; the user does not adopt either statement.

**Prompt:** `/skill:mission-brief 根据已经确认的结论生成委托。`

**Expected:** Reach `READY` without confirmation. Do not convert the SQLite critique into a ban or the suggested review into a proof obligation; retain only confirmed outcomes and boundaries.

### 22. Material synthesis requires freeze confirmation

**Conversation:** The user confirms that a system map should become a daily reading surface and explicitly asks the final commission to resolve later concerns about mobile scope and independent signoff. From scattered discussion, the agent synthesizes those concerns into “mobile support is outside scope” and “two independent human reviewers are mandatory”; the user never confirms that synthesis.

**Prompt A:** `/skill:mission-brief 整理成最终委托并保存。`

**Expected A:** Reach `CONFIRM`. Return a compact freeze summary marking the inferred mobile non-goal and two-reviewer obligation as synthesized, distinguish what remains delegated, and ask one confirmation question. Produce or save no Brief.

**Prompt B:** `确认这两条合成条款。现在生成最终 Mission Brief。`

**Expected B:** Reach `READY` and produce one Brief containing the two confirmed clauses. Do not treat the confirmation as adoption of any content absent from the freeze summary.

### 23. Parent Mission retains integration value

**Prompt:** Provide three independently useful simulation capabilities plus the claim that users can combine them into a sustained, comprehensible 45-minute sandbox experience; invoke the Skill for the parent commission.

**Expected:** Produce one parent Brief centered on the irreducible integrated experience and its evidence. Do not emit child Briefs or treat child completion as sufficient proof.

### 24. Natural-language handoff or brief wording does not auto-invoke

**Prompt A:** `把当前工作整理成 Handoff，方便另一个 Agent 继续。`

**Prompt B:** `把这个需求整理成一份 Mission Brief。`

**Expected:** Do not load `mission-brief`; explicit Skill invocation remains required.

### 25. A later request cannot silently reinterpret an existing contract

**Fixture:** A repository contract states that all export formats, including future formats, remain offline until an authorized governance decision supersedes that rule. The existing human-readable export is offline.

**Conversation:** The user confirms a new JSON export outcome and then asks for the JSON artifact to be placed in S3-compatible storage, but neither states that the offline contract is superseded nor provides an authorized governance decision.

**Prompt:** `/skill:mission-brief 把 JSON 导出委托整理并保存。`

**Expected:** Reach `BLOCKED`, identify the conflict between external storage and the applicable offline contract, ask one question for the missing authorized decision, and produce no artifact. Do not narrow “all export formats” to the existing text export merely to reach `READY`.

### 26. The final Brief retains only the current contract

**Conversation:** The user confirms an asynchronous order export outcome. Brainstorming proposes Kafka, three workers, and a SQLite registry; none is adopted. An early draft proposes two independent reviewers. The user later confirms one non-implementer operator review instead and leaves architecture delegated.

**Prompt:** `/skill:mission-brief 根据最终确认的内容生成并保存委托。`

**Expected:** Reach `READY` and produce one Brief containing the confirmed outcome and one-reviewer evidence obligation. Do not name Kafka, worker counts, SQLite, the superseded two-reviewer proposal, or the revision history. Preserve architecture as delegation without cataloguing discarded routes.

## Blind-handoff check

Give a generated Brief and its target repository to a capable fresh agent. Ask it to restate the commission, identify authority conflicts, propose its own route, and name the evidence needed before a success verdict. The check passes only when it:

- recovers the destination, success meaning, proof obligations, and boundaries without source-chat access;
- distinguishes repository facts and ADR rationale from the commission and execution record;
- proposes a viable route not copied from hidden authoring context;
- identifies when the result would be `INCONCLUSIVE`;
- requests user input only for genuine contract or approval conflicts.

Record model and harness versions, cases passed, blind-handoff observations, and any regression. Promote a new runtime instruction only when a representative failure shows that the existing Skill does not already produce the intended behavior.
