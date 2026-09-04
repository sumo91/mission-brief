<p align="center">
  <img src="./assets/readme-cover.svg" alt="Mission Brief" width="100%">
</p>

<p align="center">
  <a href="./LICENSE"><img alt="MIT License" src="https://img.shields.io/badge/license-MIT-313131?style=flat-square"></a>
  <a href="#给人类读"><img alt="Human guide" src="https://img.shields.io/badge/guide-for_humans-2F5D50?style=flat-square"></a>
  <a href="#给-agent-读"><img alt="Agent install" src="https://img.shields.io/badge/install-for_agents-6B6258?style=flat-square"></a>
</p>

<p align="center">
  <a href="#给人类读">给人类读</a> ·
  <a href="#怎么用">怎么用</a> ·
  <a href="#给-agent-读">给 Agent 读</a> ·
  <a href="https://github.com/sumo91/mission-brief/issues">提交问题</a>
</p>

大模型越来越强。以前那类强约束、强门禁、把步骤写得很具体的计划类 Skill，反而容易把它绑住。OpenAI 在新版模型引导里建议用户把提示词写瘦，重点说清结果和硬限制；Anthropic 也公开说过，他们为更强模型砍掉了80%以上的系统提示词，评估没有明显掉。

这个仓库就是顺着这个方向做的：参考了两家公司最新的大模型引导和提示词指引，给新一代强模型用的任务委托 Skill。它不写具体执行步骤，重点是这六样：

1. 要做成什么
2. 怎样算做成
3. 用什么证明
4. 哪些线不能碰
5. 这次明确不承诺什么
6. 什么可以自己做，什么要先问你

剩下的全部交给 Agent 和大模型本身。

仓库里是三件配套 Skill，按任务阶段分开：

- [`mission-align`](./mission-align/) 目标还不清楚、几个决定缠在一起、或还没定该不该立项时，先跟你对齐
- [`mission-brief`](./mission-brief/) 在动手前，把已经谈定的目标收成一份稳定的任务简报
- [`mission-review`](./mission-review/) 在做完后，让独立 Agent 对照简报检查结果有没有兑现

`mission-align` 可以按对话自己上场。`$mission-brief` 和 `$mission-review` 仍要手动调用。

> Specify the destination, proof, and hard boundaries - not the route.

---

## 给人类读

### 它适合什么时候用

目标已经大致清楚、准备交给 Agent 执行时，用 Brief 和 Review。尤其是下面这些场合。

- 任务会跨好几个对话，怕中途目标漂走
- 涉及兼容、安全、数据写入、外部系统，边界必须写死
- 你希望做完以后能独立验收，而不是听实现者自报完成

目标还不清楚时，先用 Align。例如结果本身含糊、几个结果缠在一起、该不该立项还没定，或者不同理解会写出完全不同的合同。

小修小补、当场排错、纯 UI 微调，往往用不着这套仪式。Align 只对齐，不替你脑暴方案；Brief 只钉合同，不替你实施。

### 怎么用

```text
$mission-align   →  目标不清时，对齐结果、边界和拓扑
$mission-brief   →  生成 / 修订任务简报
实施 Agent       →  按简报做事（不必再加载这个 Skill）
$mission-review  →  独立检查结果是否兑现
```

目标已经清楚，可以直接 `$mission-brief`。做完需要验收时，另开对话 `$mission-review`。

#### 1. 目标还不清楚

把含糊的委托交给 Align。它会说出当前理解、会改变合同的分歧，以及建议走 Brief、继续讨论，还是直接动手。你明确确认之后，再交给 `$mission-brief`。对齐不等于简报，它也不会开始实施。

```text
你：把导出和审计一起做了吧，最好还能给运营看报表。

你：$mission-align 先对齐这次到底要做成什么。

（Agent 说出目前理解、还没定的点、建议拆成几份还是一份）

你：确认。这次只做导出，审计另开。

你：$mission-brief 根据上面已确认的 Alignment 生成 Brief。
```

#### 2. 你已经知道要做什么

直接说清楚目标，再调用 `$mission-brief`。简报满意以后，就可以让它开始实施。

```text
你：Safari 里登录表单按回车没反应，Chrome 正常。鼠标点提交必须继续可用，别改成别的交互。

你：$mission-brief 帮我写一份任务简报。

（Agent 写出 Brief，写明要修的现象、成功标准、需要的证据、兼容边界）

你：按这份简报开始实施。
```

这时 Brief 的作用，是把“修什么、怎样算修好”钉住，把实现细节留给执行。

#### 3. 你刚跟别的 Skill 讨论完

很多时候你会先用 grill-me、brainstorming 一类 Skill 把需求谈开。谈完以后，不要把整段脑暴原样丢给执行 Agent。

决定已经拍板，调用 `$mission-brief`，只保留你已经采纳的内容。几个关键选择还在争，先 `$mission-align`，确认后再写 Brief。

```text
你：（和 brainstorming / grill-me 讨论完导出能力、审计约束、范围）

你：$mission-brief 把刚才已经确定的内容整理成任务简报，实现交给执行 Agent。

（Agent 写出 Brief。讨论里提过但你没拍板的方案，例如某套消息队列，不会写进合同）
```

讨论中的例子、批评、风险猜测、候选架构，默认都还不是合同。只有你明确采纳的部分，才会进 Brief。

### 目标太多时怎么拆

一次塞进很多彼此独立的结果时，先让 `$mission-align` 看拓扑：这是一个整体结果，还是几个可以分别验收的结果。

它可能提议一份父级 Mission，管接缝和不变量；再拆成若干份子级 Mission，各自有独立成败。你也可以主动说“拆开做”。先定拓扑，再分别写 Brief，比硬塞进一份长委托更稳。所有 Brief 的标题都是 `# Mission Brief: …`。父级靠 `Result Boundaries` 标明，子级靠 `Parent Mission` 链回父级。

没有 Align 时，`$mission-brief` 仍会在合同还写不清时停下来，只问那个会改变结果的最小决定。

### 做完以后怎么审查

实施结束后，另开对话调用 `$mission-review`。最好把采用的 Brief、最终产物和现场证据一起给它。

```text
你：$mission-review 独立审查这个已完成任务是否兑现 Mission。Brief 在 docs/missions/.../brief.md，产物在仓库里。
```

Review 只审查和裁决，不会在同一次调用里偷偷把产物修完再改判通过。结构检查、测试通过、实现者自述，只证明它们实际检查到的内容。

### 简报里通常有什么

和上面那六样对应。核心一般是 Outcome、Success、Evidence Required、Boundaries；需要时再写 Non-goals 和 Execution Authority。Intent、Context 只在确有信息时补上。

路线、阶段、测试命令、提交号不属于 Brief。Align 确认过的委托，也只把已采纳的部分写进这些栏目。

---

## 给 Agent 读

### 仓库里有什么

根目录是仓库说明与维护材料。三个运行时 Skill 各自成包。

```text
mission-align/
  SKILL.md
  agents/openai.yaml
mission-brief/
  SKILL.md
  agents/openai.yaml
  references/parent-child.md
  references/source-fidelity.md
mission-review/
  SKILL.md
  agents/openai.yaml
README.md
CONTEXT.md             # 领域语言，不安装
assets/
docs/                  # 维护材料，不安装
evals/                 # 维护材料，不安装
EVALS.md
LICENSE
```

只把 `mission-align/`、`mission-brief/` 和 `mission-review/` 拷进 Skills 目录。不要安装 `README.md`、`CONTEXT.md`、`docs/`、`EVALS.md`、`evals/`、`assets/`。

### 让 Agent 安装

把下面这句话发给你的 Agent。

```text
帮我安装这个仓库里的三个 Skill。
https://github.com/sumo91/mission-brief
只安装 mission-align/、mission-brief/ 和 mission-review/ 这三个运行时目录。
```

### 手动安装

**当前项目**

```sh
mkdir -p .agents/skills
cp -R mission-align mission-brief mission-review .agents/skills/
```

**本机所有项目**

```sh
mkdir -p ~/.agents/skills
cp -R mission-align mission-brief mission-review ~/.agents/skills/
```

**Windows PowerShell**

```powershell
$dest = "$HOME\.agents\skills"
New-Item -ItemType Directory -Force $dest | Out-Null
Copy-Item -Recurse -Force mission-align, mission-brief, mission-review $dest
```

装好后目录长这样。

```text
~/.agents/skills/mission-align/
  SKILL.md
  agents/openai.yaml
~/.agents/skills/mission-brief/
  SKILL.md
  agents/openai.yaml
  references/parent-child.md
  references/source-fidelity.md
~/.agents/skills/mission-review/
  SKILL.md
  agents/openai.yaml
```

目录名必须与各 Skill 的 `name` 一致。`mission-align` 可以按描述自动上场；`$mission-brief` 与 `$mission-review` 仍需显式调用。

维护者评估另设 `MISSION_REVIEW_HARNESS_SRC`。评估材料不进入运行时目录。

运行时行为以 [`mission-align/SKILL.md`](./mission-align/SKILL.md)、[`mission-brief/SKILL.md`](./mission-brief/SKILL.md) 与 [`mission-review/SKILL.md`](./mission-review/SKILL.md) 为准。维护者评估见 [`EVALS.md`](./EVALS.md) 与 [`evals/`](./evals/)。
