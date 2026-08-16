# Mission Brief

你跟 Agent 讨论完一件事，准备让它动手时，真正需要交接的往往只有这四样。要去哪里，怎样算做成，用什么证明，哪些线不能碰。怎么走，留给现场那个 Agent。

Mission Brief 就是干这个的。它把已经谈定的目标收成一份稳定的任务简报。旁边还有配套的 Mission Review，任务做完后可以另开一次，让独立 Agent 对照简报检查结果有没有兑现。两个都要你手动调用，提一句“Mission Brief”不会自动跑起来。

> Specify the destination, proof, and hard boundaries - not the route.

---

## 给人类读

### 它适合什么时候用

适合目标已经大致清楚、准备交给 Agent 执行的时候。尤其是下面这些场合。

- 任务会跨好几个对话，怕中途目标漂走
- 涉及兼容、安全、数据写入、外部系统，边界必须写死
- 你希望做完以后能独立验收，而不是听实现者自报完成

小修小补、当场排错、纯 UI 微调，往往用不着。它也不替你脑暴。需求还没谈清楚时，先用你平时的讨论 Skill；谈定了再来写简报。

### 怎么用

下面两种情形最常见。

#### 1. 你已经知道要做什么

直接跟 Agent 说清楚目标，再调用 Skill，让它写成任务简报。简报满意以后，就可以让它开始实施。

```text
你：Safari 里登录表单按回车没反应，Chrome 正常。鼠标点提交必须继续可用，别改成别的交互。

你：$mission-brief 帮我写一份任务简报。

（Agent 写出 Brief，写明要修的现象、成功标准、需要的证据、兼容边界）

你：按这份简报开始实施。
```

这时 Brief 的作用，是把“修什么、怎样算修好”钉住，把实现细节留给执行。

#### 2. 你刚跟别的 Skill 讨论完

很多时候你会先用 grill-me、brainstorming 一类 Skill 把需求谈开。谈完以后，不要把整段脑暴原样丢给执行 Agent。调用 Mission Brief，让它只保留你已经采纳的决定。

```text
你：（和 brainstorming / grill-me 讨论完导出能力、审计约束、范围）

你：$mission-brief 把刚才已经确定的内容整理成任务简报，实现交给执行 Agent。

（Agent 写出 Brief。讨论里提过但你没拍板的方案，例如某套消息队列，不会写进合同）
```

讨论中的例子、批评、风险猜测、候选架构，默认都还不是合同。只有你明确采纳的部分，才会进 Brief。

### 目标太多时怎么拆

如果你一次塞进很多彼此独立的结果，Agent 会先帮你看清楚。这是一个整体结果，还是几个可以分别验收的结果。

它可能提议拆成一份大纲型 Mission，管整体接缝和不变量；再拆成若干份逐步推进的 Mission，各自有独立成败。

你也可以主动说“拆开做”。先定拓扑，再分别写 Brief，比硬塞进一份长委托更稳。

### 做完以后

实施结束后，如果需要独立验收，可以另开对话这样调用。

```text
$mission-review 独立审查这个已完成任务是否兑现 Mission。
```

Review 只审查和裁决，不会在同一次调用里偷偷把产物修完再改判通过。

### 简报里通常有什么

一份 Brief 尽量短。常见字段是 Outcome（最后变成可能或真实的事情）、Success（怎样区分做成了和看起来像做成了）、Evidence Required（用什么证据挑战这个结果）、Boundaries（哪些硬边界会改变合法执行）。

需要时再加 Intent、Non-goals、Context、Execution Authority。路线、阶段、测试命令、提交号不属于 Brief。

---

## 给 Agent 读

### 安装

面向 Codex、Claude Code 等兼容 Agent Skills 的环境。

运行时只安装两个最小包。不要把 `README.md`、`docs/`、`EVALS.md`、`evals/` 拷进 Skill 目录。

目录名必须分别是 `mission-brief` 和 `mission-review`。

### 当前项目

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

### 本机所有项目

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

### Windows PowerShell

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

### 安装后应有的文件

`mission-brief` 目录里放这三份。

- `SKILL.md`
- `agents/openai.yaml`
- `references/mission-zero.md`

`mission-review` 目录里放这两份。

- `SKILL.md`
- `agents/openai.yaml`

新开对话后显式调用 `$mission-brief` 或 `$mission-review`。维护者评估另设 `MISSION_REVIEW_HARNESS_SRC`，评估材料不进入运行时目录。

运行时行为以 [`SKILL.md`](./SKILL.md) 与 [`mission-review/SKILL.md`](./mission-review/SKILL.md) 为准。维护者评估见 [`EVALS.md`](./EVALS.md) 与 [`evals/`](./evals/)。
