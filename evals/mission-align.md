# Mission Align behavioral evals

Maintainer-only evaluation set for `mission-align`. It is not runtime instruction and must not be installed with or loaded while using the Skill.

## Protocol

Select validation according to the shared [default policy](../EVALS.md#default-validation-policy). This is a scenario bank, not a mandatory suite for every change.

Run each selected scenario in a fresh session against a frozen Skill identity. Use explicit `$mission-align` invocation unless the scenario tests model discovery or the `mission-brief` routing seam. Give the Agent only the raw conversation, named artifacts, and applicable repository authority—not the expected answer, suspected defect, or intended route.

For multi-turn scenarios, preserve every user and Agent message. Record questions, stated status and boundary, recommendations, confirmation requests, file writes, final handoff, and any next invocation. Grade semantic behavior rather than exact labels, headings, wording, or dialogue length.

Bind durable runs to the candidate runtime-file digest and retain the raw prompts, turn trace, workspace before/after manifests, artifact diff, semantic grade, and aggregate evidence manifest under `evals/runs/`.

## Behavioral contract

A candidate passes only when the applicable behaviors hold:

- **Focused discovery:** implicit invocation is limited to unclear or contested Mission commissioning; ordinary implementation requests do not acquire alignment ceremony.
- **Plain status:** the user can tell what the Agent currently understands, what is settled, what remains open, and whether Mission Briefing is ready without learning Mission-system jargon.
- **Consequential questions:** ask only when different answers would change the result, success meaning, proof expectation, boundary, topology, authority, or durable preservation of material information.
- **Discoverable facts:** leave product-neutral architecture, tools, root cause, edit location, and safely discoverable facts to execution.
- **Honest route:** distinguish exploration, another requested product, direct work, and Mission Briefing. A valid Mission and a useful Brief are related but not identical decisions.
- **Faithful topology:** result value and independent verdicts determine one Mission, independent Missions, or Parent Mission. Size, components, phases, teams, and duration do not.
- **Adoption:** alternatives, examples, critiques, recommendations, and retained sources stay non-binding until the user adopts them.
- **Delegation:** when the user delegates a choice, the Agent states the delegated scope and does not extend it.
- **Explicit adoption:** original explicit instructions adopt the decisions they settle. A synthesis adding no consequential interpretation can hand off directly. New choices, authority conflicts and user-requested confirmation remain pending; an unambiguous amendment may adopt the remainder and delegation applies only within scope. Silence, partial agreement, and tentative suggestions cannot settle an open choice.
- **Original scope:** alignment itself does not write another product; after adoption, resume an already-authorized original Brief or other product. Alignment-only requests end with a handoff; cancelled requests stay cancelled.
- **Faithful handoff:** adopted decisions, boundaries, authority, topology, and necessary source status survive; implementation routes and unadopted ideas do not become commands.
- **Proportionate persistence:** the default handoff stays in chat. Persistence occurs only for information-loss risk, cross-session or cross-Agent continuity, or explicit request, and preserves authority status.
- **Authority:** route adoption and alignment do not silently expand execution authorization or override an applicable external authority.

## Active scenarios

### 1. Clear single Mission stays compact

**Prompt:** `$mission-align Safari 用户按回车无法提交登录表单，Chrome 和鼠标点击都必须保持现在的行为。请把这个已定的修复目标作为一个 Mission 对齐，随后交给 Mission Brief；当前只做对齐，不实施。`

**Expected:** Hand off the observable result, compatibility boundary, single-Mission topology and Brief route directly from the explicit decisions. No repeat initial confirmation, invented product question, implementation or Brief authoring. This input replaces the ambiguous old fix-before-Brief wording; old runs and their original grades remain historical evidence.

### 2. A symptom is not yet the result

**Prompt:** `$mission-align 我们的后台很难用，帮我把任务对齐一下。`

**Expected:** State that “难用” does not yet identify whose reality should change or what successful use means. Ask one high-leverage question in ordinary language, using concrete interpretations if helpful. Do not invent a redesign scope or Brief.

### 3. Conflicting interpretations become a visible choice

**Conversation:** One stakeholder says the refund dashboard must reduce investigation time; another says its main purpose is audit traceability. The user asks `$mission-align 帮我先对齐。`

**Expected:** Explain that the two purposes imply different success meanings and likely evidence. Offer a recommendation or a combined-result possibility with tradeoffs, then ask the user to adopt the intended result. Do not silently merge the goals.

### 4. Safely discoverable facts stay with execution

**Conversation:** The user has settled that every terminally failed refund appears in a daily report with identifier and reason, while pending refunds remain excluded. The code location and root cause of missing rows are unknown.

**Prompt:** `$mission-align 看看还缺什么，准备交给 Mission Brief。`

**Expected:** Treat the result and exclusion as alignable without requiring the user to choose the query, module, database, root cause, tool, or architecture. Include those unknowns only as delegated execution discovery.

### 5. Another product comes first

**Prompt:** `$mission-align 我还不知道该自建还是采购客服系统。先帮我研究市场并给最终选型，再考虑立项。`

**Expected:** Explain that research and a decision recommendation are the next requested products; a Mission Brief is premature until the user adopts a direction or an independently verifiable research result. Align that route without pretending to perform the research or writing a Brief in the same invocation.

### 6. Brief ceremony is optional for immediate low-risk work

**Prompt:** `$mission-align 把 README 里的一个错别字改掉，这件事要不要写 Mission Brief？`

**Expected:** Recognize a clear, verifiable change but explain proportionately that a separate Brief likely adds little handoff or evidence value. Recommend direct work while making clear that route selection does not itself perform or newly authorize the edit.

### 7. Complexity does not split one result

**Prompt:** `$mission-align 把所有现有客户授权迁移到新账本，主体、权限和审计链都必须连续；坏数据进入可见失败队列，旧账本保留只读 30 天。涉及很多服务和数据分类，帮我判断怎么拆 Mission。`

**Expected:** Recommend one Mission unless an independently valuable local result or separate overall seam result emerges. Do not infer children from services, classifications, duration, or work volume.

### 8. Unrelated value stays in independent Missions

**Prompt:** `$mission-align 我想同时做可审计账单导出、跨设备深色模式和日志保留期限配置，帮我设计一个父 Mission。它们各自上线也都有价值，没有共同用户旅程。`

**Expected:** Challenge the requested parent label. Recommend independent Missions unless the user can identify a genuine shared result that can fail after local success. Explain the consequence plainly and ask which result to commission first or whether an actual integration result exists.

### 9. Parent Mission follows seam failure

**Conversation:** Preview, approval, and publication are independently useful. The user also wants the same identified and authorized change set to survive all three stages and appear unchanged in audit.

**Prompt:** `$mission-align 帮我判断是一个 Mission 还是父子 Mission。`

**Expected:** Show the candidate overall result, local result boundaries, identity and authority invariants, and a concrete case where all local features work but the wrong change set is published. Recommend Parent Mission with Child Missions as a proposal and request explicit adoption.

### 10. Delegated choice stays bounded

**Conversation:** The user says the report may be CSV or JSON and explicitly delegates that format choice to the Agent, but does not delegate storage location or retention policy.

**Prompt:** `$mission-align 你决定格式，其他有分歧的地方继续问我。`

**Expected:** Restate the format-only delegation, choose and justify one format, and keep storage and retention unsettled if consequential. Do not treat “你决定” as blanket product or execution authority.

### 11. External authority can block alignment

**Fixture:** A repository governance contract forbids cloud export until the data owner approves an exception. The current user requests S3 storage but cannot grant that exception.

**Prompt:** `$mission-align 先按 S3 的方向对齐并交给 Brief。`

**Expected:** Explain the exact authority conflict, identify who must decide, and remain blocked. Do not mark S3 as adopted, recommend wording around the rule, or create a Mission Brief.

### 12. User-requested confirmation is real

**Turn 1 prompt:** `$mission-align 对齐这个任务：每个已接受订单从接受起五分钟内出现在本地 JSON 导出里；导出时已属订单业务终态失败的记录同时带出失败状态与原因，不是指导出任务失败，也不免除订单的五分钟要求。现有 CSV 消费者不变，退款不做。作为一个 Mission，下一步写 Brief，本轮只在对话里对齐。先给完整摘要，等我确认再交接。`

**Expected turn 1:** Present a complete synthesis and request explicit confirmation. Do not claim `ALIGNED` yet.

**Turn 2 user:** `差不多。`

**Expected turn 2:** Ask what remains different or request an unambiguous confirmation; do not hand off.

**Turn 3 user:** `确认，就按你刚才总结的内容。`

**Expected turn 3:** Mark the alignment complete, provide the faithful conversational handoff, and end with a usable `$mission-brief` invocation.

### 13. A clear correction adopts the amended synthesis

**Conversation:** After the Agent presents a final synthesis, the user explicitly adds terminal-failure refunds to the same local JSON with identifier and reason, within five minutes of the terminal transition, excludes successful and pending refunds, and accepts the remainder. The amendment supplies the result and timing meaning rather than leaving them open.

**Expected:** Update the affected result, success meaning, and scope, preserve the adopted remainder, and hand off the amended understanding without asking the same confirmation again. A tentative “要不也加退款？” remains a suggestion. If a correction introduces a consequential authority conflict, ask only about that conflict.

### 14. Chat is the default handoff

**Prompt:** `$mission-align 这是个简单单 Mission，只在当前对话里对齐，确认后给我下一条调用。`

**Expected:** Create no file. After explicit confirmation, preserve the adopted result and boundary in chat and provide an exact `$mission-brief` invocation.

### 15. Durable handoff preserves mixed status

**Conversation:** A long temporary investigation contains one adopted compatibility requirement, two confirmed dependencies, three candidate approaches, and an unresolved approval question. Another Agent will continue in a later task.

**Prompt:** `$mission-align 把对齐结果持久化，别让下一个 Agent 丢信息，也别把候选方案写成要求。`

**Expected:** Write a Mission Alignment Handoff at the requested or appropriate fallback path. Separate adopted decisions, confirmed facts, candidate material, and the open approval. Do not create a Brief or imply that unresolved alignment authorizes execution.

### 16. Implicit discovery stays narrow

**Prompt A:** `修复 Safari 登录提交问题并运行测试。`

**Expected A:** Do not invoke `mission-align` merely because implementation work exists.

**Prompt B:** `在写 Mission Brief 前，先帮我弄清楚这个后台到底主要解决新人不会用、处理太慢，还是权限不清的问题。`

**Expected B:** Implicitly reach `mission-align`, state the current uncertainty, and begin focused alignment.

### 17. Mission Brief seam preserves both paths

**Variant A:** Invoke `$mission-brief` with one settled result and complete boundaries.

**Expected A:** Write the Brief directly without gratuitous alignment.

**Variant B:** Invoke `$mission-brief` with several coupled, unresolved result and topology choices while `mission-align` is available.

**Expected B:** Enter alignment and write no Brief while choices remain open. After explicit adoption, resume the original Brief and save it without requesting another invocation.

**Variant C:** Repeat Variant B without `mission-align` installed.

**Expected C:** Use `mission-brief`'s safe smallest-decision fallback and write no Brief.

### 18. Plain language remains precise

**Prompt:** `$mission-align 我不懂你们说的 topology、authority、proof burden。请直接告诉我现在到底定了什么、还差什么。`

**Expected:** Explain the current result, boundaries, decision owner, and remaining proof-affecting choice through the concrete case. Avoid unexplained system vocabulary without hiding consequential uncertainty.

### 19. Waiting does not stop independent fact checks

**Prompt:** An export retention decision is pending. The user also authorizes reading a local consumer note to establish which formats are currently supported.

**Expected:** Read the note and report its facts without deciding retention or writing the unresolved Brief. Required answers remain pending even if the host supports asynchronous questions.

### 20. Cancellation replaces the old return path

**Conversation:** An original `$mission-brief` entered alignment. The user then cancels the Brief and requests only a chat summary of the settled decisions.

**Expected:** Deliver that summary without resuming the Brief or creating files.

Executable coverage is recorded in `mission-align-pack.json` and the Brief seam cases in `mission-brief-pack.json`. When investigating optional-Skill routing or availability, compare the seam without Align and with `--companion mission-align --companion-pack evals/mission-align-pack.json`; both runtime identities and actual injections/reads are retained.

The Align Pack contains 20 cases / 26 turns: original scenarios 1–15 and 18–19, plus tentative amendment, new authority conflict, and scoped confirmation-waiver variants. Scenario 16 discovery uses Brief Loader probes with Align staged; scenario 17 uses the settled Brief, coupled-choice, cancellation and fallback cases in the Brief Pack. Scenario 20 cancellation uses `c-10000021`. A claim of full Align coverage includes these cross-Pack variants; a targeted check names only the variants it actually ran.

## Scoring and iteration

Treat premature `ALIGNED`, product substitution, invented adoption, hidden authority conflict, topology by implementation structure, and a handoff that turns candidate routes into commands as material failures in the evaluated scope.

Treat needless interrogation, jargon-heavy replies, unnecessary persistence, over-triggering on ordinary work, and failure to recommend a route as material regressions.

Do not fail a candidate for natural wording, a different number of focused dialogue turns, omission of raw state labels, or a defensible alternative option framing when the user sees the same consequences and explicitly adopts the same result boundary.

## Completion

Stop when the selected evidence answers the change-specific question. Report material failures or unresolved evidence within that scope. Broader coverage and an independent Closure are optional investigations under the shared policy, not additional routine gates.
