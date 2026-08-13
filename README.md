# Mission Brief

Mission Brief 是面向高能力执行 Agent 的稳定结果契约：定义目的地、成功含义、证明要求与硬边界，把实现路线留给拥有最新现场上下文的 Agent。

> Specify the destination, proof, and hard boundaries—not the route.

本仓库是 `mission-brief` Skill 的版本与评估仓库。README 面向维护者，不属于运行时 Skill；实际行为以 [`SKILL.md`](./SKILL.md) 为唯一真源。

## 适用范围

适合在讨论和关键产品决策基本结束、准备交给新 Agent 执行时使用，尤其适用于：

- 长期、复杂或跨上下文的任务；
- 容易发生目标、范围或权威漂移的任务；
- 涉及兼容性、安全、治理、数据或外部写入的任务；
- 需要独立证据和可审查最终结论的任务。

普通小修复、排错、实现迭代和 UI 微调，如果没有改变可观察结果、成功语义、证明义务、边界或授权，不需要新建 Mission Brief。

Mission Brief 用来压缩已经确认的委托，不替代 brainstorming、grilling、需求讨论或产品决策。

## 核心模型

Skill 在落盘前选择一种状态：

- `READY`：任务语义闭合，所有绑定条款都有确认来源，可以生成一份 Brief。
- `CONFIRM`：形成忠实委托必须加入实质性的 Agent 合成条款；先向用户确认，不生成文件。
- `BLOCKED`：存在产品语义缺失、多个有效委托、权威冲突或不兼容要求；只询问当前最阻塞的决定，不生成文件。

一份有效 Brief 应当：

- 围绕一个能够独立判断成败的现实变化；
- 让新 Agent 不读取原始对话也能理解任务边界；
- 区分 `Success` 与 `Evidence Required`；
- 保留正式产品、兼容、安全与治理约束；
- 不包含实施计划、阶段、状态、测试结果、提交号或修复流水账；
- 不通过列举候选或被拒路线来表达“仍可自由决定”；
- 允许最终结论为 `PASSED`、`FAILED` 或 `INCONCLUSIVE`。

完整规则见 [`SKILL.md`](./SKILL.md)。

## 文档职责

Mission Brief 不是大型任务的唯一持久化载体：

| 载体 | 职责 |
|---|---|
| Mission Brief | 目标、成功语义、证明义务、硬边界与执行授权 |
| Working Plan / Implementation Ledger | 临时路线、进度、发现、下一安全切片与中间证据 |
| Closure Report | 实际证据、反证、最终裁决、残留风险与不确定性 |

执行记录可以变化，但不能重新定义 Mission Brief。Brief 只在任务契约本身改变时修订。

## 调用

该 Skill 设置了 `disable-model-invocation: true`，不会因自然语言中的 “Mission Brief” 或 “handoff” 自动触发。请显式调用：

```text
$mission-brief 根据刚才确认的决定生成最终委托。
```

Skill 只生成或修订一份 Mission Brief，不实施委托内容。

## 仓库文件

- [`SKILL.md`](./SKILL.md)：运行时 Skill，任务行为的唯一真源。
- [`EVALS.md`](./EVALS.md)：维护者回归集；生成 Brief 时不得加载。
- `README.md`：仓库维护说明；不复制到运行时安装目录。

## 安装与同步

从仓库根目录同步到当前默认安装位置：

```sh
install_dir="/Users/admin/.agents/skills/mission-brief"
mkdir -p "$install_dir"
cp SKILL.md "$install_dir/SKILL.md"
cp EVALS.md "$install_dir/EVALS.md"
```

验证安装内容与仓库一致：

```sh
install_dir="/Users/admin/.agents/skills/mission-brief"
cmp -s SKILL.md "$install_dir/SKILL.md"
cmp -s EVALS.md "$install_dir/EVALS.md"
```

不要把 README 同步到安装目录；它不是 Agent 执行所需内容。

## 评估方法

回归要求见 [`EVALS.md`](./EVALS.md)。维护时遵循以下原则：

1. 在新鲜上下文中调用候选 Skill，不向 Agent 泄露预期答案或待验证缺陷。
2. 提供原始讨论、仓库合同和任务材料，而不是维护者结论。
3. 记录 Gate 状态、询问内容、文件副作用和最终 Brief。
4. 对生成产物进行盲交接：新 Agent 只读取 Brief、目标仓库与正常环境说明。
5. 分别观察危险的 `false READY` 与造成摩擦的 `false BLOCKED`。
6. 优先根据重复、代表性的失败做小幅修改；避免为了单次波动增加通用检查表。

Skill 不追求让每份 Brief 第一次生成就完美。更重要的是让重大错误可见、可审查、可证伪，并在实施前以较低成本被发现。

## 版本与回退

所有行为修改应独立提交，并在提交前完成相应回归。使用以下命令查看演进历史：

```sh
git log --oneline
```

初始默认 Skill 已归档在提交 `b6ec2fc`。需要回退时，从目标提交恢复 `SKILL.md` 与 `EVALS.md`，重新同步到默认安装目录即可。

评估产物和临时 fixture 放在工作区外的临时目录，不提交到本仓库。
