# Mission Skills Astra 适配实施记录

日期：2026-09-05。对应[已批准方案](../specs/mission-skills-astra-adaptation.md)。

状态：实施、发布验证、独立 Closure 及本地安装已完成。八个安装文件与下述冻结候选逐字节一致。

## 已实施的行为

| Skill | 当前行为 |
| --- | --- |
| Mission Align | 完整、明确的局部修正可以同时采纳其余摘要；候选提问、含糊同意和沉默不算采纳。保留委派范围及外部决定；对齐后恢复仍有效的原请求，取消后不恢复。等待决定时可继续已授权且独立的事实核实。 |
| Mission Brief | 按需携带具体授权及其限制；修改同一合同只更新受影响条款和证明义务。已有保存授权时自行选择持久位置，保留未立项 child 的已采用义务而不代其立项。最终计划或设计请求造成歧义时先厘清交付物，不无授权地承诺计划和 Brief 两种产物。 |
| Mission Review | 裁决标识实际受审状态；复用适用证据并复现决定性或有疑点的检查。读者独立性以真实上下文判断；审查加修复先保存原裁决，再验证改后结果。 |

运行时仍为 **2 / 4 / 2 个文件**；三个调用元数据未改。Align 允许自动发现，Brief 和 Review 显式调用。没有新增模型专属版本或第四个 Skill。

按用户补充要求控制运行时膨胀：三份主文件分别为 Align 106→108 行、Brief 100→108 行、Review 77→79 行；英文词数合计 3185→3594，约增加 12.8%，不把行数近似不变当作零注意力成本。独立审查未发现需要再追加或拆分的实质规则。只因重复的产品范围行为修正 Brief，没有为文风、固定选项、路径重复或文件布局增加提示词。评估和复核说明均留在维护者目录；本轮没有证据支持“普遍降低 Token”或“模型整体变聪明”的结论。

| 运行时 | 完整包 SHA-256 |
| --- | --- |
| Align | `4871a9ad6a16b5e4f27bf21c24691ee53c1e039ffa6bea7aa7328421bdf1dcb0` |
| Brief | `85d3dd68a7a93edc6fef132a19101dba77be332787150da286d6780a46be23a2` |
| Review | `a80d5ef6a5f6309d0331d3236717cfde2996b2bd6c89cf0a7055b7d248aba224` |

这些摘要标识未提交内容；单独的 Git HEAD 不能标识本次候选。首轮 Brief 为 `de780c861f646502b8c88c60099a102cd3e6f8e64c911aec4c39de2a08021845`；因产品范围问题重复出现，增加一条规则后，第二版 `bb62f3db0ac2b90d87039f3adc746c9c9ea6d2f7c652d923707252a8fe90a79c` 又在类与测试请求上误触发。该规则收窄到最终计划或设计，重新冻结为表中版本。新 Brief 使用自己的完整分组、接缝和盲读证据，首轮通过不迁移到新字节。Align 与 Review 未变。

## 实验配置与观察

同模型对照基线为 `32c1d2a7e91c494e89e1d1b4f5e9a68c52c177f4`。执行者与语义裁判均为 `gpt-6-astra`、`medium`；入口核对真实私有会话中的模型和推理档位，未生效会使采集不能通过。使用 `/Applications/ChatGPT.app/Contents/Resources/codex`，版本 `0.153.0-alpha.5`，复用未修改的外部 SkillEvalTestPlatform 0.5.0。各 run 单独记录 harness、Pack、案例集合、运行时与证据清单身份。

| 对照 | 观察 | 可得结论 |
| --- | --- | --- |
| 完整修正并接受其余摘要，两轮成对实验 | 基线两次要求再次确认；候选两次直接交接，且保留订单、退款、时限、兼容和排除范围 | 在该固定输入和配置下，修订消除了重复确认。基线遵守的是被明确修订的旧规则；这不是通用模型能力排名。 |
| 原始 Brief 经 Align 返回 | 基线与首轮候选都能继续；最终候选的接缝也通过，实际按需读取 Align | 支持连续性、取消与装载行为，未证明相对基线的普遍增益。 |
| 保存授权、局部兼容修正及权限携带 | 基线定向案例通过；候选纳入完整回归和新鲜交接 | 验证产品规则，不能单凭新增文字声称更快或更省 Token。 |
| 当前/过期证据、先审后修 | 基线定向案例通过；候选纳入完整 Review 回归 | 未证明普遍减少检查。保留合同需要的证据适用条件，没有额外增加模型调优规则。 |
| 计划与 Brief 的产品歧义 | 最终统一评分下，基线两次仍提前承诺双产物；候选的独立定向运行与完整组内运行均正确澄清产品范围 | 固定输入下的重复差异支持该条收窄规则；全部原始失败保留，不外推到普遍能力。 |

两轮完整修正对照的总耗时（含裁判）分别为基线 78.94 / 76.03 秒、候选 78.10 / 74.97 秒；差距不足以支持速度结论。CLI 各轮原始用量保留在会话中，缓存和读取量不同，未作成本节约推断。有限重复不支持统计显著、普遍效率提升或跨模型兼容结论。

## 发布覆盖

所有原始档案位于 `evals/runs/astra-adaptation/`，遵循仓库现有规则保存在本地，不随 Git 克隆。[证据索引](../../evals/runs/astra-adaptation/evidence-index.json)记录对照、配置及完整清单身份。下表的 PASSED 表示案例行为符合预期；Review 正确判出 fixture 的失败或生产证据不确定，同样可以使行为案例通过。

| 范围 | 冻结证据 | 状态 |
| --- | --- | --- |
| Align 20 案例 / 26 轮，加隔离探针 | [align-full](../../evals/runs/astra-adaptation/align-full/20260905T065916Z-05579308/report.json) | PASSED |
| 有 Align 的耦合决定、取消、Loader、已定合同和单一缺项 | [seam-v3](../../evals/runs/astra-adaptation/seam-v3/20260905T081904Z-38961cdc/report.json) | 6 案例 / 8 轮，加隔离探针，PASSED |
| Brief Pack 1.8.5：35 行为 + 4 Loader / 45 轮；四个来源组各保留隔离探针 | [逐案发布校验](../../evals/runs/astra-adaptation/release-verification.json)：三个原组中 36 个内容未变案例，加修正组 3 案 | 当前案例完整通过；c10 采用显式独立裁决，原机器 FAILED 保留 |
| 三次新鲜交接：合同、来源与换路、修订后授权 | [blind-v3](../../evals/runs/astra-adaptation/blind-v3/20260905T085346Z-a713b78b/report.json)，由最终 c16/c22 实际产物派生 | 3 PASSED，执行与裁判均有不同的新鲜会话 |
| Review Pack 1.0.2：5 行为 + 3 Loader，加隔离 | [review-release](../../evals/runs/astra-adaptation/review-release/20260905T072600Z-2a0374cb/report.json) | PASSED |
| Review 原始八例，实际产物 | [full-artifacts 采集](../../evals/runs/astra-adaptation/review-full-artifacts/summary.json)；[mr-007 补充采集](../../evals/runs/astra-adaptation/review-webhook-portable/summary.json)；[独立行为裁决](../../evals/runs/astra-adaptation/review-artifacts-independent-grades/report.md) | 组合覆盖 8 PASSED；原全量保留 7 PASSED / 1 INCONCLUSIVE，补充只覆盖 mr-007 |
| 既有合成信息保存基线 | [历史运行](../../evals/runs/mission-brief-synthetic-baseline/20260901T233204Z-e287a235/report.json) | 仅保留既有历史门槛，非本轮 Astra 对照 |

接缝证据同时绑定 Align 和 Brief 的实际字节。隐式对齐探针记录了 Align 的真实读取；普通实现和清楚的 Brief 不读取 Align。没有可用 Align 的路径由 Brief 全量案例覆盖。

## 评估修正与保留的失败

- 旧 CLI `0.144.5` 被 Astra 服务拒绝；改用应用当前 CLI 后核实真实模型。旧请求不是模型行为证据。
- 旧隔离方式把可读 Skill 放在被禁读的凭据父目录内。现使用 Codex 原生支持的符号链接，指向独立只读运行时；凭据、原仓库、裁判材料及运行档案仍隔离。
- 最初退款修正未定义新增退款的时限和输出，两版都合理追问。完整定义后才进行同输入的成对比较，保留原始记录。
- 原 Brief 小型 CLI 案例没有任何可识别目标，Pack 1.8.1 增补唯一 CLI fixture。产品边界案例也遗漏了自然语言合同所说的方案，Pack 1.8.2 补足原始 proposal，原 prompt、断言及 rubric 不变。后者在补材料后仍提前承诺双产物，因此按真实重复行为修改运行时；没有把它归结为纯评估误判。旧完整运行在改候选前中断并保留原始采集及停机原因，新候选从头取得完整覆盖。
- Review 原 Python fixture 在隔离环境无法启动，改为等价的标准 shell 产物。另补足原文字包缺少的离线 HTML、导出数据及本地 webhook 产物；原文字包保留。Webhook 的 `mktemp` 显式使用获准临时目录，其旧失败采集保留，补测只覆盖该例。
- CLI 摘要轨迹遗漏了部分 code-mode 工具调用，导致一例实际已读 CSV 被误判。独立裁判从完整私有轨迹复核；新评分包只提取完整工具事件，不引入隐藏推理或开发者指令。旧失败报告不回写成通过。
- 修复 Review 子集汇总，明确采集、语义裁决和全量覆盖；盲读同时修改 prompt 与 rubric，允许合理选用原建议并验证环境变化后的路线自由。
- 独立复核发现两项文风误判：短的无来源/拓扑声明，以及产品问题未枚举“都要”，均没有破坏合同或暗自增加交付。Pack 1.8.3/1.8.4 明确把实际额外步骤、权限、路线约束或交接障碍作为失败条件，允许开放式产品问题；原机器评分不改写，不为固定措辞继续追加运行时规则。

Pack 1.8.5 另修正三处与产品合同冲突的前提：`c16` 输入已含多入口一致和未来导入的集成风险，故不强制禁止拓扑参考；`c18` 的原语义要求允许 Context 或独立持久来源，故取消固定单文件数量；`c23` 原输入只有只读及离线边界，补成明确的本地订单 Markdown 核对结果后再要求写成 Brief。原确定性失败不改成通过；仅重新执行这三案，复用完整输入、断言及 rubric 未变的其他案例。

`c10` 是另一类问题：[独立语义复核](../../evals/runs/astra-adaptation/brief-case-independent-grades/c-10000010.md)确认两份持久文件、三项未立项义务和双向链接满足原 rubric。机器因用户可见 response 未列路径而判失败；审计字段 artifact_paths 不当作用户可见输出，亦无需靠它补救本条实际保存与可恢复义务。此表达缺口没有证明合同未履行。原报告维持 FAILED，显式独立裁决绑定其 SHA、完整清单、候选与逐条 rubric；它不能覆盖确定性失败、缺失评分或全局不确定性。

最小本地检查为 `python3 evals/scripts/test_eval_adaptation.py`，覆盖缺例、未评分、身份漂移、配置、原生装载、完整工具事件及证据篡改。发布校验拒绝重复、异候选、异 harness、未变案例的失败和全局不确定性；修改过评估前提的案例必须有当前完整内容的新通过证据。输出逐案来源、被替代的旧评估和独立裁决摘要，不改写原报告。三个 Skill 的元数据校验、fixture 摘要、文档链接与 `git diff --check` 另行核对；这些不替代行为运行。

## 证据范围与安装

本轮多轮 replay 验证跨轮修正和取消。选用的 CLI 采集入口没有接入工作进行中的用户消息，因此没有把普通 replay 算作真实 in-flight steering 验证。未在前代模型重跑，不新增其兼容声明。历史原始反馈仍缺少完整真实输入，原历史复现维持 `INCONCLUSIVE`；合成材料不冒充生产或历史事实。

[独立 Closure](2026-09-05-astra-independent-closure.md) 得到有证据支持的 PASSED 后，已把三个最小包同步到 `/Users/admin/.agents/skills/mission-align/`、`mission-brief/`、`mission-review/`，重新核对完整目录清单和每个文件字节。总计 2 / 4 / 2 个文件，安装摘要与冻结摘要一致，维护者材料未进入运行时。

[安装回执](../../evals/runs/astra-adaptation/installation-receipt.json)记录安装时间、前后文件摘要、Closure 与发布校验身份。前版完整组合保留在 `evals/runs/astra-adaptation/installed-before/`；若需回退，恢复这一组合并核对，不删除失败记录。此次未提交或推送 Git。
