# Mission Brief behavioral evals

Maintainer-only evaluation set for `mission-brief`. It is not runtime instruction and must not be installed with or loaded while using the Skill.

## Protocol

Run each scenario in a fresh session against a frozen Skill identity. Invoke the Skill explicitly except where a scenario tests manual invocation. Give the Agent raw conversation, artifacts, and repository authority—not the expected answer, suspected defect, prior critique, or intended fix.

Record the response, questions, file writes, references loaded, and generated Brief. Grade observable behavior and the resulting commission. Internal labels, exact wording, fixed response fields, and a predetermined number of dialogue turns are not requirements.

Enumerate and execute every prompt variant rather than treating a scenario heading as one run. Bind the run to the candidate runtime-file digest and retain the raw prompt, turn trace, final response, workspace before/after manifests, artifact diff, semantic grade, and aggregate evidence manifest under `evals/runs/`. A `/tmp` artifact or a Closure summary alone is not release evidence.

For a regression introduced by an earlier candidate, run the authentic source set against the named baseline revision when those originals are available. When an authentic source is missing, preserve the gap explicitly; a reconstruction may exercise the rule but cannot be labeled as the historical baseline.

After representative authoring scenarios pass, give a separate fresh Agent only the Brief, target workspace, and normal ambient instructions. That blind handoff is part of the release result.

## Behavioral contract

A candidate passes only when the applicable behaviors below hold:

- **Manual invocation:** ordinary implementation and natural-language mentions of a brief do not load this user-invoked Skill.
- **One commission:** the output centers one coherent result that can receive an honest verdict. Complexity, file count, requested labels, and implementation phases do not determine result topology.
- **Settled before writing:** create one Brief when the commission is sufficiently settled. When a consequential user choice or authority conflict would change the contract, expose the smallest decision needed before writing. Do not pair an unresolved contract with a completed artifact.
- **Faithful contract:** binding content comes from adopted user decisions, applicable external authority, necessary meaning, task-appropriate proof, or a necessary located pointer. Discussion, critiques, examples, and proposed solutions remain unbound until adopted.
- **Artifact fidelity:** a result contract does not silently replace a requested final plan, design review, decision recommendation, or implementation plan. When the requested product differs, expose the difference and settle the smallest consequential choice before writing.
- **Information disposition:** material source information is not silently lost merely because it is non-binding. Keep contract-shaping content in the Brief, preserve valuable non-contract findings in a durable labeled source, expose consequential unsettled decisions, and omit only content that is irrelevant, rejected, superseded, or safely discoverable without erasing completed investigation.
- **Source authority:** a source may mix adopted decisions, applicable authority, confirmed facts, and candidate approaches. Preserve their actual status; linking or retaining a source does not make all of it binding.
- **Durable traceability:** necessary context remains retrievable after handoff. A temporary path, expiring attachment, or source conversation alone is not a completed handoff when material information exists only there.
- **Current contract:** retain the effective destination, success meaning, proof, boundaries, and authority. Omit superseded proposals, route history, completed checks, and generic governance language that does not change this commission.
- **Route freedom:** preserve externally fixed behavior and authority while leaving product-neutral architecture, implementation location, root cause, tools, and discoverable facts to the executing Agent.
- **Authority:** surface unresolved conflicts with repository contracts, compatibility commitments, or authorized decisions. A later Brief cannot silently narrow or supersede them.
- **Evidence:** separate success facts from how they will be challenged. Evidence must address the promised result rather than substitute convenient proxy checks, scale with consequence, permit `INCONCLUSIVE`, and remain owned by the Agent unless a genuinely human-only judgment is part of the claim.
- **Topology:** several independent results do not automatically form a parent. When the user has adopted an overall result that can still fail after local results pass, make that integration result and its seams explicit before commissioning it. Different defensible decompositions may pass when they protect the same user outcome.
- **Mission 0:** load the parent reference only for a confirmed or pending integration commission or a child tied to one. A parent owns integration value, cross-result invariants, seam evidence, program boundaries, and concise result boundaries—not child implementation plans or copied local contracts.
- **Continuity:** preserve applicable parent promises in later child commissions. Keep omitted confirmed child contracts in a durable authoritative source or leave them visibly unsettled for later confirmation.
- **Blind handoff:** a capable fresh Agent can recover the result, failure conditions, proof obligations, hard boundaries, target, and granted authority without the source conversation, while retaining freedom to choose a viable route.
- **Mission storage:** a Mission uses `<documentation-boundary>/docs/missions/<outcome-slug>/brief.md`. Mission 0 is the parent role of that same artifact, not a separate global file type; physical nesting may mirror same-boundary topology, while explicit links carry topology across package boundaries.

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

**Fixture:** Present only [`evals/fixtures/mr-001-standard-report-v2/handoff.md`](evals/fixtures/mr-001-standard-report-v2/handoff.md). Do not reveal the later Mission, acceptance claim, deliverables, critique, or expected result topology.

**Prompt:** `$mission-brief 我想继续把这里的标准报告做好，让业务同事真的能快速看懂，也能顺着每个判断找到证据。先帮我把下一步立一下项。`

**Expected:** Preserve actual business reading and claim-to-evidence tracing as success that must be exercised directly. Package shape, field presence, image loading, responsive rendering, and automated tests may support the verdict but cannot establish that user result by themselves. A coherent single commission or a justified integration topology may pass; no specific internal state or decomposition is required.

### 10. Result topology follows adopted value

**Variant A — unrelated results:** The user confirms an auditable billing export, cross-device dark mode, and configurable log retention, with no shared end-to-end result.

**Expected A:** Do not manufacture a parent, even if the user requests a parent label. Make the independent results visible and ask which result—or which genuine integrated outcome—the user wants to commission.

**Variant B — pending integration:** The user confirms intake, reconciliation, and publication as independently useful results and says the whole flow should preserve identity, authorization, and acknowledged state, but has not yet adopted a parent result or its boundaries.

**Expected B:** Show the candidate integration outcome, result boundaries, and cross-result invariants for adoption. Write no parent or child Brief until the user decides whether to commission that packaging.

**Variant C — long single result:** The user confirms one regulated migration: every existing customer authorization record moves without interruption to a new ledger, preserving subject, permission, and audit chain; invalid records enter a visible failure queue; the old ledger remains read-only for 30 days. It has many classifications, failure paths, and evidence categories, but no independently valuable subset.

**Expected C:** Produce one commission without treating detail or difficulty as proof of multiple results. Population-level reconciliation may be combined with representative and boundary behavioral challenges; topology does not itself require exhaustive execution of every behavior.

### 11. Mission 0 proves the seams

**Conversation:** The user adopts the overall claim that the same authorized change set survives preview, approval, publication, and audit without identity substitution. The three adopted result boundaries are concrete: preview inspects one identified change set without publishing it; approval accepts or rejects that same set through an authorized reviewer; publication applies only that approved set and records it for audit.

**Prompt:** `$mission-brief 创建这个已经确认的整体委托，子结果以后分别立项。`

**Expected:** Produce one parent Brief centered on the integrated result, cross-result identity and authority, and evidence capable of falsifying the seams. Do not emit child Briefs, milestones, implementation order, or the union of child test lists.

### 12. Parent continuity survives later child work

**Variant A — durable source:** An approved Mission 0 names concise result boundaries and a durable authoritative requirements record containing confirmed child-local contracts.

**Prompt A:** `$mission-brief 为其中已经确认的预览结果单独创建子 Mission Brief。`

**Expected A:** Create one self-contained child Brief, preserve applicable parent invariants, point to the authoritative source when needed, and leave Mission 0 unchanged.

**Variant B — chat-only child contract:** The approved Mission 0 deliberately contains only concise preview, approval, and publication boundaries. Confirmed child-local obligations—invalid preview inputs are visible, approval rejections retain a reason, and publication failures can roll back—exist only in the authoring conversation and do not belong in the parent. The user has not decided whether to preserve them durably or leave them for later reconfirmation.

**Prompt B:** `$mission-brief 先保存 Mission 0，子 Mission 以后再说。`

**Expected B:** Do not silently discard the child contracts or copy them into the parent. Before saving, ask whether to preserve them in a durable authoritative source or leave them unsettled for later child confirmation.

### 13. Discoverable unknowns do not block the commission

**Conversation:** The user has settled that each accepted order appears exactly once in a local JSON export within five minutes, terminal failures are visible, existing CSV consumers continue to work, and evidence covers successful export, terminal failure, and CSV regression. The repository contains several possible implementation locations, and the current root cause is unknown but safely discoverable by the executing Agent.

**Prompt:** `$mission-brief 生成委托，具体从哪里改和根因是什么让执行 Agent 自己查。`

**Expected:** Produce the Brief without asking the user to choose an implementation location, root cause, tool, or architecture. Preserve those facts as execution-time discovery.

### 14. Current contract replaces revision sediment

**Conversation:** The settled result gives operators an offline export with visible terminal failures and requires one non-implementer operator review. Early proposals name Kafka, SQLite, three workers, and two reviewers; all are superseded, and architecture remains delegated.

**Prompt:** `$mission-brief 根据最终决定生成委托。`

**Expected:** Keep the current export outcome and one-reviewer evidence obligation. Omit earlier routes, superseded reviewer counts, and revision history.

### 15. Output location follows the request and repository

**Variant A:** The user asks for the complete Brief inline and forbids file writes. The settled result is a local CLI that deterministically returns every exact glossary match and source location, gives an explicit empty result, and neither writes files nor accesses the network.

**Expected A:** Return one complete inline Brief and write nothing.

**Variant B:** A monorepo has `packages/billing/docs/` and no existing Brief convention. The same commission later adopts CSV-consumer compatibility, then a separate settled result: a daily report of terminally failed or amount-mismatched refunds, with identifiers and reasons, excluding pending refunds and making no state changes.

**Expected B:** Save the billing commission at `packages/billing/docs/missions/<outcome-slug>/brief.md`. Update an existing file only for the same commission; give a new result a distinct directory.

### 16. Blind handoff

Give a generated Brief and its target workspace to a capable fresh Agent. Ask it to restate the commission, identify authority conflicts, propose its own route, and explain what would justify `PASSED`, `FAILED`, or `INCONCLUSIVE`.

**Expected:** The Agent recovers the destination, failure conditions, proof, boundaries, target, and authority without the source conversation; distinguishes contract from repository facts and progress records; and proposes a viable route not copied from hidden authoring context.

### 17. A contract does not replace a final plan

**Conversation:** The user supplies a detailed but partly unadopted architecture proposal and asks `$mission-brief 阅读方案并给出最终可行方案。`

**Expected:** Do not author a final plan inside the `$mission-brief` invocation or silently relabel a Mission Brief as that plan. Explain the result-contract boundary and determine whether the user wants the adopted commission frozen, the proposal reviewed and completed as a separate product, or both. Preserve an already adopted detailed plan as authority only to the extent actually adopted.

### 18. Detailed findings survive contract compression

**Fixture:** Use [`evals/fixtures/mb-001-detailed-plan-preservation/`](evals/fixtures/mb-001-detailed-plan-preservation/) according to [`evals/cases/mission-brief/mb-001-detailed-plan-preservation.md`](evals/cases/mission-brief/mb-001-detailed-plan-preservation.md).

**Expected:** Preserve the adopted retirement, compatibility, permission, and behavioral-proof contract. Keep the confirmed shared consumers, importer recreation mechanism, and distinct stale entry points recoverable through concise context or a durable labeled pointer. Candidate approaches and investigation order do not become commands, while the Brief remains a contract rather than a copied plan.

### 19. One source may carry mixed authority

**Conversation:** A durable proposal contains an adopted offline export result, confirmed PostgreSQL audit facts, a candidate Kafka design, a rejected SQLite experiment, and an unresolved recommendation for human approval.

**Expected:** Extract the adopted result and applicable facts without treating the whole proposal as authority. Keep useful non-binding material in its durable source when it aids execution, omit superseded sediment from the contract, and stop only if the unresolved approval choice would materially change proof or authority.

### 20. Temporary context is not a durable handoff

**Conversation:** The only copy of a detailed investigation is a temporary attachment. It contains a confirmed shared dependency and a concrete import-recreation mechanism that do not themselves prescribe the implementation. The user asks to save the settled Mission Brief in the repository.

**Expected:** Do not complete the handoff with only a temporary link. Preserve the necessary findings in the Brief's concise Context, place them in an appropriate durable reference when authorized by the requested save, or request the smallest disposition decision when a material source cannot be persisted. Do not turn the findings into a mandatory route.

### 21. Known findings differ from safe discovery

**Conversation:** The commission is settled. A supported consumer is already confirmed to depend on a shared script, while the actual defect root cause and best edit location remain unknown but safely discoverable.

**Expected:** Keep the confirmed dependency recoverable because losing it would erase completed investigation. Leave the unknown root cause, edit location, tools, and architecture to the executing Agent without blocking the Brief.

### 22. Mission storage follows result topology and ownership

**Variant A — standalone:** One independently verifiable result belongs to the repository root.

**Expected A:** Save it at `docs/missions/<outcome-slug>/brief.md` without an empty `children/` directory or mandatory context record.

**Variant B — same-boundary Mission 0:** One package owns an adopted integration result in which the same authorized change set retains identity and authority from Preview to Approval. The commissioned Preview child inspects an identified set without applying it and exposes invalid or unauthorized input; the Approval child accepts or rejects that unchanged set through an authorized reviewer and records rejection reasons.

**Expected B:** Store the parent as `<package>/docs/missions/<integration-slug>/brief.md`; identify its role with a `# Mission 0:` title and `Result Boundaries`; and use `children/<child-slug>/brief.md` plus child `Parent Mission` links for commissioned children. Mission 0 is not a global `mission-0.md` file type.

**Variant C — cross-package Mission 0:** The integration result spans independently owned packages. The parent preserves one authorized change set through preview, approval, and publication; each package-owned child has a concrete commissioned result at its own boundary.

**Expected C:** Keep the parent at the lowest common documentation boundary and each child at its owning package boundary. Use explicit bidirectional links rather than forcing physical nesting to override ownership.

### 23. Simple Missions do not acquire preservation ceremony

**Prompt:** `$mission-brief Safari 下登录表单按回车没有提交，Chrome 和鼠标点击行为必须保持不变。`

**Expected:** Produce a compact `brief.md` with the observable regression, compatibility boundary, and proportionate proof. Do not create a context record, source inventory, ADR, or reference appendix when no material external context needs preservation.

### 24. Blind handoff checks contract and traceability

Give a generated Brief, its durable labeled sources, and the target workspace to a capable fresh Agent. Do not provide the authoring conversation or expected implementation.

**Expected:** The Agent recovers the contract, distinguishes Authority Sources from Reference Sources, locates material known dependencies and risks, identifies which candidate ideas remain optional, and proposes a viable route. Passing requires both contract recovery and source traceability; sentence-by-sentence reconstruction of the original proposal is not required.

### 25. Irrelevant bulk does not inflate the contract

**Conversation:** A settled local export commission is accompanied by a long durable source containing meeting history, superseded naming debates, unrelated roadmap ideas, generic security advice, and one confirmed compatibility fact that changes the result boundary.

**Expected:** Preserve the settled export contract and the one material compatibility fact. Leave the durable source labeled as reference when it remains useful, but do not copy its unrelated or superseded bulk into the Brief, add obligations from generic advice, or create preservation ceremony merely because the source is long. Judge compactness by whether each retained clause changes the contract, proof, boundary, or handoff—not by a fixed word count or ratio.

## Scoring and iteration

Treat invented binding content, hidden authority conflict, proxy evidence presented as final proof, unresolved-contract writes, and a failed blind handoff as release-blocking. Treat unnecessary blocking, route overconstraint, gratuitous review burden, and non-self-contained wording as material regressions.

Do not fail a candidate for natural wording, a defensible alternative decomposition, absence of internal state labels, or a different number of focused clarification turns. Preserve raw failures and candidate identities. Change runtime instruction only for repeated or high-consequence behavioral failures that the existing principles do not already cover.

## Release evidence gate

A release candidate is eligible for independent Closure only when every active scenario and prompt variant has a durable result, every release-blocking finding is resolved or honestly makes the run `FAILED`/`INCONCLUSIVE`, both blind handoffs have fresh task identities, and the evidence aggregate identifies the exact candidate used. The installed runtime is synchronized only after that Closure returns an evidence-supported `PASSED`.
