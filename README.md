# Mission Brief + Mission Review

这是一对配套、手动调用的 Agent Skills：

- `mission-brief` 把已经采用的委托压缩成稳定的结果契约，交给拥有最新现场上下文的执行 Agent；
- `mission-review` 在任务完成后，由独立 Agent 亲自检查最终产物和实质证据，判断结果合同是否兑现。

两者共享同一个中心思想：

> Specify the destination, proof, and hard boundaries—not the route.

本仓库同时保存两项运行时 Skill、Mission 0 引用、维护者评估和真实回归材料。维护者文件不进入运行时安装目录。

## 核心行为

`mission-brief` 先选择一个能够独立判断成败的用户或系统结果，再判断合同是否已经充分明确：

- 没有可观察结果时，先定位真正应发生的变化。
- 一个结果无论多复杂，都可以直接形成一个 Brief。
- 多个独立结果默认分别立项。
- 用户已经提出、正在考虑或已经采用一个“局部都通过后仍可能失败”的整体结果时，进入 Mission 0 先把候选拓扑讲清楚；只有采用后才写父级 Brief。
- 会改变结果、证据、边界或授权的决定尚未作出时，先展示需要决定的内容，不写 Brief。

一份 Brief 只保留：

- `Outcome`：最终成为可能或真实的事情；
- `Success`：区分成功和相似失败的事实；
- `Evidence Required`：能够挑战真实结果的证据；
- `Boundaries`：会改变合法执行的硬边界；
- 确有信息时才增加 `Intent`、`Non-goals`、`Context` 或 `Execution Authority`。

绑定内容必须忠实于用户采用的决定和适用权威。讨论、例子、批评、风险猜测和候选方案不会自动进入合同。产品中立的架构、工具和实现路线留给执行 Agent。

## Evidence

证据应直接挑战 Mission 承诺的结果，不能用方便的代理指标替代。例如页面可加载、字段存在和自动化通过，只能证明它们实际检查的行为；如果结果是“读者能快速理解并追溯证据”，执行 Agent 还需要实际完成代表性的阅读与追证任务。

验证默认由 Agent 完成。只有 Agent 无法真实提供的人类决定或体验，才保留给人类。最终证据应允许诚实得出 `PASSED`、`FAILED` 或 `INCONCLUSIVE`。

## Mission Review

`mission-review` 从已采用的 Mission Brief 或等效权威合同恢复结果、证明义务、硬边界和授权条件，然后检查实际交付物：

- 亲自执行当前环境中可做的合理验证，不把常规审查转交给用户；
- 只按检查真实覆盖的行为采信自动化、截图、结构检查和实现者报告；
- 接受自然措辞、必要语义和合同留给执行阶段的路线自由；
- 只有实质结果、证据、边界或权威条件未满足时才判 `FAILED`；
- 决定性事实在可行检查后仍不可取得时判 `INCONCLUSIVE`；
- 先给审查结论，不在审查过程中静默修复产物或重写 Mission。

当独立 child Agent 能减少实现上下文偏差或真正模拟读者任务时，可以使用；它提供待核对的观察，不替代主审查者判断，也不能冒充合同指定的人类授权。

## Mission 0

[`references/mission-zero.md`](./references/mission-zero.md) 只在存在已采用或待确认的整体集成结果，或后来为该 Mission 0 创建 child Mission 时读取。

Mission 0 拥有：

- 不可约的整体结果；
- 跨结果不变量；
- 能挑战接缝的证据；
- 项目级边界；
- 简洁的结果边界。

它不复制 child 的局部成功条件、测试清单、实施顺序或详细合同。省略的已确认 child 合同需要由持久权威来源保存，否则留到对应 child 立项时重新确认。

## 文档职责

| 载体 | 职责 |
|---|---|
| Mission Brief | 结果、成功语义、证明义务、硬边界与授权变化 |
| Working Plan / Implementation Ledger | 路线、进度、发现和中间证据 |
| Closure Review | 实际证据、反证、裁决和不确定性 |

后两者可以演进，但不能静默改写 Mission Brief。

## 调用

两项 Skill 都是手动调用型，不因普通请求或自然语言提及自动触发：

```text
$mission-brief 根据刚才采用的决定生成最终委托。
$mission-review 独立审查这个已完成任务是否兑现 Mission。
```

`mission-brief` 只形成委托，不实施委托内容；`mission-review` 只审查和裁决，不在同一委托中修复结果。

## 仓库结构

- [`SKILL.md`](./SKILL.md)：普通运行路径。
- [`agents/openai.yaml`](./agents/openai.yaml)：界面元数据与手动调用策略。
- [`references/mission-zero.md`](./references/mission-zero.md)：按需加载的父级与 child 连续性规则。
- [`mission-review/SKILL.md`](./mission-review/SKILL.md)：独立结果审查流程。
- [`mission-review/agents/openai.yaml`](./mission-review/agents/openai.yaml)：Mission Review 界面元数据与手动调用策略。
- [`EVALS.md`](./EVALS.md)：维护者行为评估，不属于运行时内容。
- [`evals/mission-review.md`](./evals/mission-review.md)：Mission Review 外部行为评估合同。
- [`evals/fixtures`](./evals/fixtures)：公开回归材料。真实业务报告等私有夹具不进入本仓库。
- [`evals/scripts`](./evals/scripts)：可审计的维护者评估 runner；本地 `evals/runs/` 证据档案不进入版本仓库。

## 安装与同步

面向 Codex、Claude Code 等兼容 Agent Skills 的环境。运行时只同步两个最小包，不要把 README、docs、evals、cases、fixtures 或 runner 拷进 Skill 目录。

安装目录名必须分别是 `mission-brief` 和 `mission-review`。

**当前项目可用：**

```sh
mkdir -p .agents/skills/mission-brief/agents \
         .agents/skills/mission-brief/references \
         .agents/skills/mission-review/agents
cp SKILL.md .agents/skills/mission-brief/SKILL.md
cp agents/openai.yaml .agents/skills/mission-brief/agents/openai.yaml
cp references/mission-zero.md .agents/skills/mission-brief/references/mission-zero.md
cp mission-review/SKILL.md .agents/skills/mission-review/SKILL.md
cp mission-review/agents/openai.yaml .agents/skills/mission-review/agents/openai.yaml
```

**本机所有项目可用：**

```sh
mkdir -p ~/.agents/skills/mission-brief/agents \
         ~/.agents/skills/mission-brief/references \
         ~/.agents/skills/mission-review/agents
cp SKILL.md ~/.agents/skills/mission-brief/SKILL.md
cp agents/openai.yaml ~/.agents/skills/mission-brief/agents/openai.yaml
cp references/mission-zero.md ~/.agents/skills/mission-brief/references/mission-zero.md
cp mission-review/SKILL.md ~/.agents/skills/mission-review/SKILL.md
cp mission-review/agents/openai.yaml ~/.agents/skills/mission-review/agents/openai.yaml
```

Windows PowerShell：

```powershell
$brief = "$HOME\.agents\skills\mission-brief"
$review = "$HOME\.agents\skills\mission-review"
New-Item -ItemType Directory -Force "$brief\agents", "$brief\references", "$review\agents" | Out-Null
Copy-Item SKILL.md "$brief\SKILL.md"
Copy-Item agents\openai.yaml "$brief\agents\openai.yaml"
Copy-Item references\mission-zero.md "$brief\references\mission-zero.md"
Copy-Item mission-review\SKILL.md "$review\SKILL.md"
Copy-Item mission-review\agents\openai.yaml "$review\agents\openai.yaml"
```

安装后每个 Skill 目录里只应有上述运行时文件。新开对话后通过 `$mission-brief` / `$mission-review` 显式调用。维护者评估 runner 需要另外设置 `MISSION_REVIEW_HARNESS_SRC`，不要把评估夹具装进 Skill 目录。

README、docs、evals、cases、fixtures、runner 和本地 run 档案都不是运行时文件。候选通过评估和独立 Closure 前，不同步到运行设备。

## 评估原则

[`EVALS.md`](./EVALS.md) 验证外部行为，不要求固定状态名、表单、措辞或对话轮数：

1. 新鲜上下文只接收原始任务和权威材料，不接收预期答案或缺陷诊断。
2. 检查是否虚构合同、隐藏权威冲突、写死路线、过度阻塞或用代理指标替代真实结果。
3. 对合理的不同结果分解保持开放，只要求用户在意的结果和接缝不丢失。
4. 使用独立盲交接检查 Brief 是否自包含且保有路线自由。
5. 保留每次失败和候选身份；只为重复或高后果的行为缺陷修改运行时规则。

初始 Mission Brief 默认版本位于提交 `82d40de`。当前稳定版本、后续简化候选和配套 Mission Review 均可通过 Git 历史独立恢复与比较。
