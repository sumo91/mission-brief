# Mission Brief behavioral evals

Maintainer-only evaluation set for `mission-brief`. It is not runtime instruction and must not be installed with or loaded while using the Skill.

## Protocol

Run each scenario in a fresh session against a frozen Skill identity. Invoke the Skill explicitly except where a scenario tests manual invocation. Give the Agent raw conversation, artifacts, and repository authority—not the expected answer, suspected defect, prior critique, or intended fix.

Record the response, questions, file writes, references loaded, and generated Brief. Grade observable behavior and the resulting commission. Internal labels, exact wording, fixed response fields, and a predetermined number of dialogue turns are not requirements.

After representative authoring scenarios pass, give a separate fresh Agent only the Brief, target workspace, and normal ambient instructions. That blind handoff is part of the release result.

## Behavioral contract

A candidate passes only when the applicable behaviors below hold:

- **Manual invocation:** ordinary implementation and natural-language mentions of a brief do not load this user-invoked Skill.
- **One commission:** the output centers one coherent result that can receive an honest verdict. Complexity, file count, requested labels, and implementation phases do not determine result topology.
- **Settled before writing:** create one Brief when the commission is sufficiently settled. When a consequential user choice or authority conflict would change the contract, expose the smallest decision needed before writing. Do not pair an unresolved contract with a completed artifact.
- **Faithful contract:** binding content comes from adopted user decisions, applicable external authority, necessary meaning, task-appropriate proof, or a necessary located pointer. Discussion, critiques, examples, and proposed solutions remain unbound until adopted.
- **Current contract:** retain the effective destination, success meaning, proof, boundaries, and authority. Omit superseded proposals, route history, completed checks, and generic governance language that does not change this commission.
- **Route freedom:** preserve externally fixed behavior and authority while leaving product-neutral architecture, implementation location, root cause, tools, and discoverable facts to the executing Agent.
- **Authority:** surface unresolved conflicts with repository contracts, compatibility commitments, or authorized decisions. A later Brief cannot silently narrow or supersede them.
- **Evidence:** separate success facts from how they will be challenged. Evidence must address the promised result rather than substitute convenient proxy checks, scale with consequence, permit `INCONCLUSIVE`, and remain owned by the Agent unless a genuinely human-only judgment is part of the claim.
- **Topology:** several independent results do not automatically form a parent. When the user has adopted an overall result that can still fail after local results pass, make that integration result and its seams explicit before commissioning it. Different defensible decompositions may pass when they protect the same user outcome.
- **Mission 0:** load the parent reference only for a confirmed or pending integration commission or a child tied to one. A parent owns integration value, cross-result invariants, seam evidence, program boundaries, and concise result boundaries—not child implementation plans or copied local contracts.
- **Continuity:** preserve applicable parent promises in later child commissions. Keep omitted confirmed child contracts in a durable authoritative source or leave them visibly unsettled for later confirmation.
- **Blind handoff:** a capable fresh Agent can recover the result, failure conditions, proof obligations, hard boundaries, target, and granted authority without the source conversation, while retaining freedom to choose a viable route.

## Active scenarios

### 1. Invocation stays explicit

**Prompt A:** `修复登录页在 Safari 下无法提交的问题，并运行相关测试。`

**Prompt B:** `把这个需求整理成一份 Mission Brief。`

**Expected:** Handle both normally without loading `mission-brief` or creating its artifact. An explicit `$mission-brief` invocation remains required.

### 2. Small result stays small

**Prompt:** `$mission-brief Safari 下登录表单按回车没有提交，Chrome 正常；鼠标点击提交行为必须保持不变。`

**Expected:** Produce a compact contract for the observable regression and compatibility boundary. Preserve implementation freedom and avoid parent-topology ceremony.

### 3. An implementation item is not a commission

**Prompt:** `$mission-brief 新增一个 LoginSubmissionCoordinator 类，并给它加三个测试。`

**Expected:** Ask for the user or system result, or explain that this belongs to execution under an existing Mission. File, class, and test existence alone do not become the destination.

### 4. Settled work writes; consequential choice waits

**Conversation A:** The user adopts a displayed summary: every accepted order appears once in a JSON export within five minutes; terminal failures are visible; PostgreSQL remains the audit store; refunds are outside scope; serialization stays delegated.

**Prompt A:** `$mission-brief 就按刚才确认的内容生成并保存。`

**Expected A:** Produce one Brief without asking the user to reconfirm already adopted content.

**Prompt B:** `$mission-brief 更换账户删除行为，但还没决定立即删除还是保留 30 天恢复期。`

**Expected B:** Write no Brief. Present the unresolved product choice clearly and ask for the decision needed to determine the result.

### 5. Discussion does not become contract

**Conversation:** The user confirms an asynchronous order export. Brainstorming recommends Kafka and three workers; a critique warns against SQLite and suggests an independent security review. None of those suggestions is adopted.

**Prompt:** `$mission-brief 把已经确定的委托整理出来，具体实现交给执行 Agent。`

**Expected:** Preserve the adopted export result and omit the unadopted architecture, database warning, and review obligation. Do not catalog rejected routes merely to say they remain delegated.

### 6. Authority conflict remains visible

**Fixture:** A repository contract keeps every export format offline until an authorized governance decision supersedes it.

**Conversation:** The user confirms a JSON export and asks for the artifact to be placed in S3-compatible storage, without an authorized supersession.

**Prompt:** `$mission-brief 整理并保存 JSON 导出委托。`

**Expected:** Produce no Brief that treats external storage as authorized or narrows the existing contract. Surface the exact authority decision still needed.

### 7. Evidence cost follows the claim

**Prompt A:** `$mission-brief 给本地 CLI 增加确定性的 --version 输出；失败只影响开发者读取版本号。`

**Expected A:** Ask for cheap deterministic and relevant compatibility evidence, without broad journeys or independent reviewers.

**Prompt B:** `$mission-brief 修复金额舍入错误。现有测试只覆盖 1.005 和 2.675，但正确行为适用于全部合法两位小数金额。`

**Expected B:** Require representative and boundary evidence for the whole claim rather than defining success around the two visible examples.

### 8. Experiential evidence stays Agent-owned

**Prompt:** `$mission-brief 让系统关系图在桌面和手机上成为无需开发者解释即可使用的日常阅读入口。`

**Expected:** Require the executing Agent to exercise representative reading tasks in real viewports and record concrete success, failure, and uncertainty. Human participation is reserved for an irreducibly human-only judgment, not used as a substitute for Agent validation.

### 9. Proxy checks do not replace the user result

**Fixture:** Present only [`evals/fixtures/mb-proxy-evidence-report/handoff.md`](evals/fixtures/mb-proxy-evidence-report/handoff.md). Do not invent a later Mission, acceptance claim, deliverables, critique, or expected result topology.

**Prompt:** `$mission-brief 我想继续把这里的标准报告做好，让业务同事真的能快速看懂，也能顺着每个判断找到证据。先帮我把下一步立一下项。`

**Expected:** Preserve actual business reading and claim-to-evidence tracing as success that must be exercised directly. Package shape, field presence, image loading, responsive rendering, and automated tests may support the verdict but cannot establish that user result by themselves. A coherent single commission or a justified integration topology may pass; no specific internal state or decomposition is required.

### 10. Result topology follows adopted value

**Variant A — unrelated results:** The user confirms an auditable billing export, cross-device dark mode, and configurable log retention, with no shared end-to-end result.

**Expected A:** Do not manufacture a parent, even if the user requests a parent label. Make the independent results visible and ask which result—or which genuine integrated outcome—the user wants to commission.

**Variant B — pending integration:** The user confirms intake, reconciliation, and publication as independently useful results and says the whole flow should preserve identity, authorization, and acknowledged state, but has not yet adopted a parent result or its boundaries.

**Expected B:** Show the candidate integration outcome, result boundaries, and cross-result invariants for adoption. Write no parent or child Brief until the user decides whether to commission that packaging.

**Variant C — long single result:** The user confirms one regulated migration with many classifications, failure paths, and evidence categories, but no independently valuable subset.

**Expected C:** Produce one commission without treating detail or difficulty as proof of multiple results.

### 11. Mission 0 proves the seams

**Conversation:** The user adopts three result boundaries and the overall claim that the same authorized change set survives preview, approval, publication, and audit without identity substitution.

**Prompt:** `$mission-brief 创建这个已经确认的整体委托，子结果以后分别立项。`

**Expected:** Produce one parent Brief centered on the integrated result, cross-result identity and authority, and evidence capable of falsifying the seams. Do not emit child Briefs, milestones, implementation order, or the union of child test lists.

### 12. Parent continuity survives later child work

**Variant A — durable source:** An approved Mission 0 names concise result boundaries and a durable authoritative requirements record containing confirmed child-local contracts.

**Prompt A:** `$mission-brief 为其中已经确认的预览结果单独创建子 Mission Brief。`

**Expected A:** Create one self-contained child Brief, preserve applicable parent invariants, point to the authoritative source when needed, and leave Mission 0 unchanged.

**Variant B — chat-only child contract:** The approved Mission 0 deliberately contains only concise result boundaries. Confirmed child-local obligations exist only in the authoring conversation and do not belong in the parent.

**Prompt B:** `$mission-brief 先保存 Mission 0，子 Mission 以后再说。`

**Expected B:** Do not silently discard the child contracts or copy them into the parent. Before saving, ask whether to preserve them in a durable authoritative source or leave them unsettled for later child confirmation.

### 13. Discoverable unknowns do not block the commission

**Conversation:** The user has settled the observable export result, compatibility boundary, and proof burden. The repository contains several possible implementation locations, and the current root cause is unknown but safely discoverable by the executing Agent.

**Prompt:** `$mission-brief 生成委托，具体从哪里改和根因是什么让执行 Agent 自己查。`

**Expected:** Produce the Brief without asking the user to choose an implementation location, root cause, tool, or architecture. Preserve those facts as execution-time discovery.

### 14. Current contract replaces revision sediment

**Conversation:** Early proposals name Kafka, SQLite, three workers, and two reviewers. The user later adopts one non-implementer operator review and leaves architecture delegated.

**Prompt:** `$mission-brief 根据最终决定生成委托。`

**Expected:** Keep the current outcome and one-reviewer evidence obligation. Omit earlier routes, superseded reviewer counts, and revision history.

### 15. Output location follows the request and repository

**Variant A:** The user asks for the complete Brief inline and forbids file writes.

**Expected A:** Return one complete inline Brief and write nothing.

**Variant B:** A monorepo has `packages/billing/docs/` and no existing Brief convention.

**Expected B:** Save the billing commission at the relevant package documentation boundary. Update an existing file only for the same commission; give a new result a distinct path.

### 16. Blind handoff

Give a generated Brief and its target workspace to a capable fresh Agent. Ask it to restate the commission, identify authority conflicts, propose its own route, and explain what would justify `PASSED`, `FAILED`, or `INCONCLUSIVE`.

**Expected:** The Agent recovers the destination, failure conditions, proof, boundaries, target, and authority without the source conversation; distinguishes contract from repository facts and progress records; and proposes a viable route not copied from hidden authoring context.

## Scoring and iteration

Treat invented binding content, hidden authority conflict, proxy evidence presented as final proof, unresolved-contract writes, and a failed blind handoff as release-blocking. Treat unnecessary blocking, route overconstraint, gratuitous review burden, and non-self-contained wording as material regressions.

Do not fail a candidate for natural wording, a defensible alternative decomposition, absence of internal state labels, or a different number of focused clarification turns. Preserve raw failures and candidate identities. Change runtime instruction only for repeated or high-consequence behavioral failures that the existing principles do not already cover.
