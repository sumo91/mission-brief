# Mission Brief

面向高能力执行 Agent 的稳定结果契约：定义目的地、成功含义、证明要求与硬边界，把实现路线留给拥有最新现场上下文的 Agent。

> Specify the destination, proof, and hard boundaries—not the route.

本仓库是 `mission-brief` Skill。运行时行为以 [`SKILL.md`](./SKILL.md) 为唯一真源。

## 它做什么

在讨论和关键产品决策基本结束后，把已经确认的委托压缩成一份 Brief。新 Agent 不读原始对话，也能判断成败、证明义务和硬边界。

它**只生成或修订一份 Mission Brief，不实施委托内容**。

适合：

- 长期、复杂或跨上下文的任务
- 容易发生目标、范围或权威漂移的任务
- 涉及兼容性、安全、治理、数据或外部写入的任务
- 需要独立证据和可审查最终结论的任务

普通小修复、排错、实现迭代和 UI 微调，如果没有改变可观察结果、成功语义、证明义务、边界或授权，不需要新建 Mission Brief。它也不替代 brainstorming、grilling、需求讨论或产品决策。

## 安装

面向 Codex、Claude Code 等兼容 Agent Skills 的环境。运行时**只安装 `SKILL.md`**。不要把 `README.md`、`EVALS.md` 或 `examples/` 拷进 Skill 目录，以免评估用例被当成运行时指令。

安装目录名必须是 `mission-brief`，与 Skill 的 `name` 一致。

**当前项目可用：**

```sh
mkdir -p .agents/skills/mission-brief
cp SKILL.md .agents/skills/mission-brief/SKILL.md
```

**本机所有项目可用：**

```sh
mkdir -p ~/.agents/skills/mission-brief
cp SKILL.md ~/.agents/skills/mission-brief/SKILL.md
```

Windows PowerShell：

```powershell
New-Item -ItemType Directory -Force "$HOME\.agents\skills\mission-brief" | Out-Null
Copy-Item SKILL.md "$HOME\.agents\skills\mission-brief\SKILL.md"
```

### 验证

安装后，Skill 目录里应当只有 `SKILL.md`。新开对话后应能通过 `/mission-brief` 显式调用。

## 调用

该 Skill 设置了 `disable-model-invocation: true`，**不会**因为对话里出现 “Mission Brief” 或 “handoff” 而自动触发。必须显式调用：

```text
/mission-brief 根据刚才确认的决定生成最终委托。
```

其他兼容 Agent Skills 的工具，用该工具的显式调用方式指向 `mission-brief` 即可。

## 会得到什么

Skill 在落盘前选择一种状态：

| 状态 | 行为 |
|---|---|
| `READY` | 任务语义闭合，所有绑定条款都有确认来源；生成一份 Brief |
| `CONFIRM` | 忠实陈述委托需要加入 Agent 合成的实质性条款；先确认，不写文件 |
| `BLOCKED` | 产品语义缺失、多个有效委托、权威冲突或不兼容要求；只问当前最阻塞的一个问题，不写文件 |

默认保存到 `docs/mission-briefs/<outcome-slug>.md`。也可以要求内联输出、指定路径，或遵循仓库已有约定。完整示例见 [`examples/async-order-export.md`](./examples/async-order-export.md)。

一份有效 Brief 应当：

- 围绕一个能够独立判断成败的现实变化
- 让新 Agent 不读取原始对话也能理解任务边界
- 区分 `Success` 与 `Evidence Required`
- 保留正式产品、兼容、安全与治理约束
- 不包含实施计划、阶段、状态、测试结果、提交号或修复流水账
- 不通过列举候选或被拒路线来表达“仍可自由决定”
- 允许最终结论为 `PASSED`、`FAILED` 或 `INCONCLUSIVE`

完整规则见 [`SKILL.md`](./SKILL.md)。

## 和执行记录的关系

Mission Brief 不是大型任务的唯一持久化载体：

| 载体 | 职责 |
|---|---|
| Mission Brief | 目标、成功语义、证明义务、硬边界与执行授权 |
| Working Plan / Implementation Ledger | 临时路线、进度、发现、下一安全切片与中间证据 |
| Closure Report | 实际证据、反证、最终裁决、残留风险与不确定性 |

执行记录可以变化，但不能重新定义 Mission Brief。Brief 只在任务契约本身改变时修订。

## 仓库文件

| 文件 | 给谁用 | 是否安装到 Skill 目录 |
|---|---|---|
| [`SKILL.md`](./SKILL.md) | 运行时 Agent | 是，唯一需要拷贝的文件 |
| [`examples/async-order-export.md`](./examples/async-order-export.md) | 阅读者 | 否 |
| [`EVALS.md`](./EVALS.md) | 维护者回归 | 否 |
| `README.md` | 人类说明 | 否 |

## 维护者

回归要求见 [`EVALS.md`](./EVALS.md)。维护时遵循：

1. 在新鲜上下文中调用候选 Skill，不向 Agent 泄露预期答案或待验证缺陷。
2. 提供原始讨论、仓库合同和任务材料，而不是维护者结论。
3. 记录 Gate 状态、询问内容、文件副作用和最终 Brief。
4. 对生成产物进行盲交接：新 Agent 只读取 Brief、目标仓库与正常环境说明。
5. 分别观察危险的 `false READY` 与造成摩擦的 `false BLOCKED`。
6. 优先根据重复、代表性的失败做小幅修改；避免为了单次波动增加通用检查表。

Skill 不追求让每份 Brief 第一次生成就完美。更重要的是让重大错误可见、可审查、可证伪，并在实施前以较低成本被发现。

所有行为修改应独立提交，并在提交前完成相应回归：

```sh
git log --oneline
```

初始默认 Skill 已归档在提交 `82d40de`。需要回退时，从目标提交恢复 `SKILL.md` 与 `EVALS.md`，再按上文只同步 `SKILL.md` 到安装目录。

评估产物和临时 fixture 放在工作区外的临时目录，不提交到本仓库。
