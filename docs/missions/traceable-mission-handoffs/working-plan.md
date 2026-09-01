---
source_status: adopted-authority
captured_at: 2026-09-01
source_sha256_before_header: b904c19e5bd0f01af7f6084233861eb62cc4ac1804900b817ab26f481f5ba6e5
---

# Working Plan: Traceable Mission handoffs

The body below is the verbatim user-adopted implementation plan captured from the commissioning attachment. This header records provenance; it does not alter the adopted plan.

---

总体方向已经比较清楚：

> 保留 Mission Brief 作为短而稳定的结果合同；增加信息去向和来源追溯机制；用统一的 Mission 目录承载 Mission 0、child Mission 及配套材料。

Mission 0 被定义为一种拓扑角色，不是另一种文件类型。

## 一、最终目标形态

### 独立 Mission

```text
docs/missions/<outcome-slug>/
├── brief.md
├── context.md          # 按需
├── working-plan.md     # 执行阶段按需
└── reviews/            # 按需
```

### Mission 0 与 child Mission

```text
docs/missions/<integration-outcome-slug>/
├── brief.md            # Mission 0
├── context.md          # 按需
├── children/
│   ├── <child-outcome-slug>/
│   │   └── brief.md
│   └── <child-outcome-slug>/
│       └── brief.md
└── reviews/
```

统一约定：

- 所有合同文件都叫 `brief.md`；
- Mission 0 使用 `# Mission 0:` 标题并包含 `Result Boundaries`；
- child 使用 `# Mission Brief:`，并包含 `Parent Mission` 链接；
- 同一文档边界内可以物理嵌套；
- 跨 package 时，Mission 0 放在最低共同边界，child 放在各自 package，通过双向链接表达拓扑；
- 目录表达材料所有权，文档链接表达结果关系。

## 二、最终职责划分

| 载体 | 职责 |
|---|---|
| Mission Brief | Outcome、Success、Evidence、Boundaries、Authority |
| Mission 0 | 集成结果、跨结果不变量、接缝证据、Result Boundaries |
| `context.md` 或既有来源 | 重要事实、依赖、风险、理由、候选建议和来源状态 |
| `working-plan.md` | 实现路线、调查发现、进度和中间证据 |
| Closure Review | 实际观察、证据、反证、裁决和不确定性 |

关键规则：

- 非绑定不等于可删除；
- 引用不等于授权；
- 未知且可安全发现的事实可以留给执行者；
- 已确认、调查成本高且会影响风险或兼容性的事实必须有持久去向；
- 重要信息只能进入 Brief、进入持久来源，或被明确判定为无关、失效、被拒绝；
- 不允许无声消失。

## 三、需要新增和修改的文件

### 新增

1. `CONTEXT.md`

   只定义统一术语：

   - Mission；
   - Mission Brief；
   - Mission 0；
   - child Mission；
   - Authority Source；
   - Reference Source；
   - Mission Package；
   - Information Disposition；
   - Blind Handoff。

2. `docs/adr/0001-separate-mission-contract-from-context.md`

   记录“合同与上下文分离”的设计决定，包括：

   - 为什么 Brief 不容纳完整方案；
   - 为什么重要非合同信息仍需持久保存；
   - 为什么 Mission 0 是角色而不是独立文件类型；
   - 为什么不用逐句映射、最低字数或强制附件。

3. 新增评估案例和 fixtures

   保存这次已经出现的“详细方案被过度压缩”问题及其他边界场景。

### 修改

1. [SKILL.md](/Users/admin/Documents/Codex/MissionBrief/SKILL.md)

   - 增加交付物类型识别；
   - 增加来源定位和信息分类；
   - 拆开“非绑定”和“可删除”；
   - 收紧“执行者可重新发现”的适用范围；
   - 明确 `Context` 的来源状态与持久性；
   - 增加转换保真检查；
   - 默认路径改为 `docs/missions/<outcome-slug>/brief.md`。

2. [references/mission-zero.md](/Users/admin/Documents/Codex/MissionBrief/references/mission-zero.md)

   - 对齐新目录约定；
   - 要求父子双向链接；
   - 明确 child 合同和参考来源的持久性；
   - 说明跨 package 时逻辑关系不依赖物理嵌套。

3. [README.md](/Users/admin/Documents/Codex/MissionBrief/README.md)

   - 增加 Mission Package 模型；
   - 更新职责表；
   - 更新目录与文件名约定；
   - 明确 Mission Brief 不等于最终可行方案；
   - 更新安装和使用示例。

4. [EVALS.md](/Users/admin/Documents/Codex/MissionBrief/EVALS.md)

   - 增加信息保留、来源状态、临时来源、交付物错位和目录拓扑场景；
   - 扩展 blind handoff 验收标准。

5. `agents/openai.yaml`

   更新简短描述，但继续保持手动调用。

6. `mission-review/SKILL.md`

   只做必要对齐：

   - 可以使用 Reference Source 定位证据；
   - 不能把 Reference Source 静默升级为合同；
   - 支持新的 Mission 存储位置。

## 四、运行时流程改造

新的 Mission Brief 流程建议为六步。

### 1. 识别产物类型

判断用户要的是：

- 结果合同；
- 完整方案；
- 方案评审；
- 决策建议；
- 实施计划。

如果不是结果合同，不能静默用 Mission Brief 替代。

### 2. 定位来源

识别：

- 已采用用户决定；
- 仓库和治理权威；
- 详细方案；
- 调查结果；
- 临时附件或聊天材料。

### 3. 分类和安排信息去向

每项重要信息判断：

- 是否已经采用；
- 是否具有约束力；
- 是否包含重要事实、依赖、风险或理由；
- 应进入 Brief、持久来源还是明确舍弃。

### 4. 选择结果并解决合同

继续保持现有优势：

- 以可观察结果立项；
- 暴露后果重大的未决选择；
- 保留权威和兼容性承诺；
- 不预选实现路线；
- 正确识别 Mission 0。

### 5. 编写和压缩

保持核心结构：

```markdown
# Mission Brief: <observable result>

## Outcome
## Success
## Evidence Required
## Boundaries
```

按需增加：

```markdown
## Intent
## Non-goals
## Context
## Execution Authority
## Parent Mission
## Result Boundaries
```

### 6. 双重 handoff 检查

同时验证：

- 新 Agent 能恢复合同；
- 新 Agent 能找到必要来源；
- 能区分权威和参考；
- 已知依赖和风险没有消失；
- 未采纳建议没有伪装成授权；
- 仍保留实现路线自由。

## 五、评估案例

至少新增八组行为测试：

1. 详细方案压缩；
2. 同一文档混合已采用决定和候选建议；
3. 未采纳但有参考价值的建议；
4. 临时目录或聊天附件中的来源；
5. 已调查的重要依赖和风险；
6. 未知但可安全发现的根因；
7. 大量无关材料，防止 Brief 膨胀；
8. 用户要求最终方案，防止产品类型被替换。

目录方面再增加：

9. 独立 Mission 存储；
10. 同边界 Mission 0 与 child；
11. 跨 package Mission 0；
12. child 双向链接与持久来源；
13. 同一委托更新原文件，新结果创建新目录。

## 六、具体执行顺序

### 阶段 1：固定基线

1. 记录当前 Git 版本；
2. 保存这次反馈涉及的原方案、首版 Brief、修订版 Brief和转换请求；
3. 确认当前版本能复现信息压缩问题；
4. 暂不修改运行时 Skill。

产物：

- 原始回归 fixture；
- 基线行为记录；
- 问题判定标准。

### 阶段 2：确定领域模型

1. 创建 `CONTEXT.md`；
2. 固定 Mission、Mission 0、Brief、Context 和 Source 的定义；
3. 创建 ADR；
4. 确认目录层级和命名规则。

验收：

- 一个术语只有一个含义；
- Mission 0 明确是拓扑角色；
- Brief 与详细方案职责没有重叠。

### 阶段 3：先写评估

1. 在 `EVALS.md` 增加新行为合同；
2. 添加详细方案 fixture；
3. 添加临时来源和混合权威案例；
4. 添加目录与跨 package 案例；
5. 用当前版本运行，证明新增测试能够捕获现有问题。

验收：

- 新测试不是围绕固定措辞；
- 旧版本确实暴露目标缺陷；
- 测试不会因为 Brief 较短就自动失败。

### 阶段 4：修改运行时规则

1. 修改 `SKILL.md`；
2. 对齐 `mission-zero.md`；
3. 修改默认存储路径；
4. 增加 Context 来源状态；
5. 扩展 blind handoff；
6. 必要时轻量对齐 `mission-review`。

原则：

- 优先修改通用判定规则；
- 不加入案例专用禁语；
- 不增加固定字数；
- 不要求完整复制原材料。

### 阶段 5：目录迁移

现有：

```text
docs/mission-briefs/mission-review-mvp.md
```

迁移为：

```text
docs/missions/reliable-mission-review/
└── brief.md
```

同时：

1. 更新所有内部链接；
2. 用 `rg` 检查旧路径引用；
3. 历史 review 文件第一轮可以保留原位；
4. 新 Closure Review 开始采用 Mission 目录内的 `reviews/`；
5. 不批量移动无关历史材料。

### 阶段 6：完整验证

1. 运行全部现有行为案例；
2. 运行全部新增案例；
3. 测试小任务是否仍保持短小；
4. 测试复杂方案是否保留来源；
5. 测试未采纳建议不会成为授权；
6. 测试临时来源不会只留下无效链接；
7. 完成独立 blind handoff；
8. 由新 Agent 根据 Brief 和来源自行提出不同实现路线。

### 阶段 7：独立 Closure

使用 `mission-review` 审查本次改造：

- 是否解决了信息无声丢失；
- 是否保持合同精炼；
- 是否没有扩大未采纳建议的权威；
- 是否没有过度阻塞；
- 是否保持 Mission 0 的接缝语义；
- 是否完成目录和链接迁移。

只有得到有充分证据的 `PASSED` 才发布。

### 阶段 8：发布和同步

1. 保留候选版本身份；
2. 更新 README；
3. 检查运行时包只包含必要文件；
4. 同步到 `/Users/admin/.agents/skills/mission-brief`；
5. 使用 `cmp` 验证运行时文件与仓库一致；
6. 不把 evals、fixtures、ADR 或维护者记录装入运行时目录。

## 七、建议的提交边界

为了方便审查和回退，建议拆成五个提交：

1. `docs: define mission domain and storage model`
2. `test: add information-preservation regressions`
3. `refactor: add source disposition to mission brief`
4. `docs: migrate mission storage convention`
5. `review: record independent closure evidence`

不要把领域定义、运行时修改、目录迁移和评估证据塞进同一个提交。

## 八、最终发布门槛

全部满足才算完成：

- Brief 仍然是结果合同，不是完整方案；
- Mission 0 与普通 Brief 使用统一文件类型；
- Mission 目录和父子关系清楚；
- 约束没有在压缩中缩水；
- 重要信息具有明确、持久的去向；
- 非绑定建议没有变成授权；
- 临时来源得到处理；
- 小任务没有新增不必要仪式；
- 跨 package 拓扑能够导航；
- 旧行为评估没有回归；
- 独立 Agent 能完成 blind handoff；
- Mission Review 给出有证据支持的通过结论。

这套落地的中心不是“让 Brief 写得更多”，而是让合同、上下文、执行和审查各自拥有明确边界，同时保证信息在它们之间移动时不会失踪。
