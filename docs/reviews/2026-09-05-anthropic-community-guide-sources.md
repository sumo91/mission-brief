# Anthropic 与社区指南：审阅依据

核查日期：2026-09-05（Asia/Shanghai）。本文只建立外部证据，不评价仓库内具体条文，也未执行模型对照实验。所有下列页面均实际打开；动态官方文档未展示修订日期的，以本次访问状态为准。

## 当前模型与证据适用范围

Anthropic 当前模型总览把 **Claude Fable 5.1** 用于高难推理与长程代理工作，建议多数任务先用 **Claude Opus 5**，其高 effort 仍不能满足自有评测时再选 Fable 5.1。这是厂商的定位，不是独立证明它在所有任务都最强。[Models overview](https://platform.claude.com/docs/en/models/overview)

Fable 5.1 官方详情标记 Latest、发布日期 2026-09-01、API ID `claude-fable-5-1`；Mythos 5.1 提供同级能力，但限 Project Glasswing 邀请访问。本次没有调用用户账户的模型列表，无法确认其具体订阅、区域、宿主是否已经开放这些模型。[Fable 5.1 overview](https://platform.claude.com/docs/en/models/fable-5-1/overview)

官方通用 prompting 页明确覆盖 Fable/Mythos 5.1、5、Opus 5 等；要求先读目标型号的专属指南，并将其他型号测得的建议重新纳入自己的评测。它仍推荐清晰目标、具体输出约束、在顺序重要时给出步骤、解释约束的用途、使用有代表性的例子；没有推荐清空全部流程。[Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)

## 可以直接用于审阅的官方原则

| 来源及版本 | 核实的原则 | 对审阅的意义 |
| --- | --- | --- |
| [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)，动态文档 | 假定 Claude 已经聪明，只补它缺少的内容；按任务脆弱性与变化程度设置自由度。开放任务允许判断，脆弱且顺序敏感的操作可以固定脚本。建议主文件正文少于 500 行、引用按需加载、避免深层引用。先建立无 Skill 基线与至少三个代表性场景，再为真实缺口写最少指令。 | 行数是组织建议，不是达标证明；必须检查规则解决了什么真实缺口。多步骤或低自由度本身不构成问题。 |
| [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)，2025-09-29 | 既反对在 prompt 中硬编码脆弱的分支逻辑，也反对空泛原则；最少必要信息不等于字数最少。用多样而典型的例子替代穷举边角情况，先在最好模型上测试简版，按失败补充。 | 应寻找重复与条件分支带来的维护成本，而不是凭长短判定“防御性”。这是较早的工程原则，需和当前型号指南一起使用。 |
| [Prompting Claude Fable 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)，Fable/Mythos 5 专属 | 多数行为可以用简洁原则控制，无须逐条列举；停点可归纳为破坏性操作、真实范围变化或只有用户能提供的信息。同时仍推荐根据工具结果核实进度声明、明确授权边界、记录可复用经验且去重。 | 新模型友好意味着减少替模型决策的枚举，同时保留证据、授权与记忆约束；不能把后一类一并删除。 |
| [Prompting Claude Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1)，Fable/Mythos 5.1 专属 | 目标清楚时无需细教方法；长任务可能过早收尾或询问已经授权的后续步骤，可明确继续执行可逆且在范围内的工作。迁移时应重新评测 effort。压缩应保留用户约束、已决事项和未完工作；限制顺手修复及多余永久测试，但完整交付请求本身。 | 应评价门槛是否阻断授权内工作、是否保持范围与交接信息，而不是统一增加确认。指南提醒自治提示也可能减少合理澄清，须测试权衡。 |
| [Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)，Opus 5 专属 | 给完整任务规格后让模型运行。该型号默认会自验；官方建议移除泛化的“所有非平凡任务都追加最终验证/子代理验证”，以减少过度验证。审查提示若过分强调“保守/只报高严重度”，可能降低召回，建议先发现再筛选。 | 可质疑无条件重复验证和提前压低审查召回的规则；不能据此删除业务验收标准或高风险操作的专门检查，也不能假定所有型号都相同。 |

## Claude Code 的手动调用机制

Claude Code 默认允许用户和模型调用 Skill。其官方机制是 `SKILL.md` 的 YAML frontmatter：`disable-model-invocation: true` 禁止模型自动调用；`user-invocable: false` 则隐藏用户调用入口，方向相反。用户设置也可通过 `skillOverrides` 的 `user-invocable-only` 达成手动调用。[Extend Claude with skills：Control who invokes a skill](https://code.claude.com/docs/en/skills#control-who-invokes-a-skill)

同一官方文档列出了 Claude Code 扩展字段及默认行为，本次检索全文没有 `openai.yaml`，也没有找到 Claude Code 识别 `agents/openai.yaml` 或 `allow_implicit_invocation` 的官方承诺。因此：**仅设置 Codex 的 `agents/openai.yaml`，不能据此保证 Claude Code 也仅手动调用**。这是文档级兼容性判断，不是对当前安装版本做过运行测试。若希望打包层面跨宿主保证手动调用，应分别提供宿主支持的调用控制，或明确限定支持范围。[Extend Claude with skills：Frontmatter reference](https://code.claude.com/docs/en/skills#frontmatter-reference)

## 社区一手指南与实证研究

### Kyle / HumanLayer：Writing a good CLAUDE.md

作者在 HumanLayer 自己的博客署名 Kyle，发表于 2025-11-25。其重点是只将普遍相关的项目知识放在常驻指令中，把专用细节按需展开，以权威文件的引用替代易过期副本，将格式化交给确定性工具，并警惕因一次不满而不断追加行为补丁。作者自己允许有理由的例外。[原文](https://www.humanlayer.dev/blog/writing-a-good-claude-md)

局限：这是当时的工程经验，主要对象是常驻 `CLAUDE.md`，不能无条件套给按需加载的 Skill。其“约 150–200 条指令”说法不应作为最新模型的通用上限：所引用的 IFScale 研究使用 2025 年模型与特定密集指令任务，展示的是随密度和模型变化的衰减曲线。[IFScale 原论文，2025-07-15 v1](https://arxiv.org/pdf/2507.11538)

### Simon Willison：Agentic Engineering Patterns

Willison 是 Django 共同创建者、Datasette 创建者；此处使用其本人持续维护的指南，而非转载总结。[作者介绍](https://simonwillison.net/about/)

《First run the tests》（2026-02-24 创建，02-28 更新）示范用极短的标准工程术语激活模型已有的工程知识，无须重新解释整个方法。[原文](https://simonwillison.net/guides/agentic-engineering-patterns/first-run-the-tests/)

《Prompts I use》（2026-02-28 创建，04-02 更新）同时展示有具体用途的强约束：例如为可直接复制至静态托管的产物指定原生 HTML/JS，为无障碍替代文字指定方便复制的输出形态。可推导的审阅原则是：限制应对应真实交付需求，并说明其用途；不能将“有禁止项”自动归类为差写法。[原文](https://simonwillison.net/guides/agentic-engineering-patterns/prompts/)

局限：这些是作者的实用模式，不是 Fable 5.1 或 GPT-6 的受控评测。尤其“先跑测试”与 Opus 5 对过度验证的最新提示存在适用范围差异，不应合并成普适硬规则。

### Gloaguen 等，ETH Zurich / LogicStar.ai：Evaluating AGENTS.md

采用 **2026-06-23 的 v2**，不是仍被搜索摘要引用的 02-12 v1。作者直接研究了 Python 仓库任务，使用 Sonnet 4.5、GPT-5.2、GPT-5.1 mini 和 Qwen3 等组合。v2 结论是上下文文件通常没有显著提高成功率，却使成本平均增加超过 20%；指令被遵守，引发更多测试、探索与推理。不能把它夸大为“所有上下文文件降低成功率”。[论文 v2 正文](https://arxiv.org/html/2602.11988v2)

反证同样重要：附录未发现文件长度与成功率的明确关系；去掉其他文档后，生成的上下文文件反而有帮助。研究也没有评测本仓库 Skill、非代码任务或 2026-09 的最新模型。因此它支持“额外流程须测增益”，不能证明“越短越好”或“Skills 无用”。[同文附录 B](https://arxiv.org/html/2602.11988v2)

## 证据允许怎样下结论

1. **符合指南**可以由静态阅读判断，例如是否明确触发范围、是否按需加载、是否将自由度与风险匹配；**能稳定实现愿景**则需要无 Skill、现版与精简版在相同模型和任务上的对照。
2. “防御性堆积”的可检验对象是：已经由宿主保障的重复规则、没有任务依据的全局门槛、因历史单例不断增加的例外、没有退出条件的验证循环。字数、否定词数量只能提示检查方向。
3. 评测既应记录成功率，也应记录多余澄清、违规越权、遗漏需求、调用与阅读成本、可恢复性。不能只优化 token 数，也不能只看一份示例输出是否漂亮。

以上三点是本次根据各来源形成的审阅方法推论，不是任何单一厂商的逐字规范。本次外部来源核查没有执行本仓库模型实验；仓库既有 Astra 实测由主报告另行审查，尚未找到 Claude 最新模型的运行证据。
