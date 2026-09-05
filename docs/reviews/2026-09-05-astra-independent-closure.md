# Mission Skills Astra 适配：独立 Closure

日期：2026-09-05。独立审查上下文：`/root/astra_independent_closure`。

**独立 Closure：PASSED。** 当前三个精确运行时满足已批准适配合同，可进入用户已授权的最小包安装。无剩余阻断项；本结论不证明安装已执行。

## 审查合同与身份

从已批准方案 `docs/specs/mission-skills-astra-adaptation.md`、当前 CONTEXT、README、三个 Skill 与评估合同恢复范围，再核对基线 `32c1d2a7e91c494e89e1d1b4f5e9a68c52c177f4` 至当前工作区差异。未把实施者报告或预期裁决当作证据。独立评分在读取原始产物后形成；实现过程通知只用于定位材料。未修改运行时、安装或重跑昂贵模型套件。

受审的是未提交工作区的精确运行时字节，HEAD 本身不够标识它：

| Skill | 文件数 | 最终 bundle SHA-256 |
| --- | --- | --- |
| mission-align | 2 | `4871a9ad6a16b5e4f27bf21c24691ee53c1e039ffa6bea7aa7328421bdf1dcb0` |
| mission-brief | 4 | `85d3dd68a7a93edc6fef132a19101dba77be332787150da286d6780a46be23a2` |
| mission-review | 2 | `a80d5ef6a5f6309d0331d3236717cfde2996b2bd6c89cf0a7055b7d248aba224` |

保留 Align 自动发现、Brief/Review 显式调用及三者职责；未新增模型分支、管理 Skill 或强制配套表单。分别从基线 Git 对象重算三个包，确认保留基线确实对应原始运行时，而非候选换标签。

## 设计与实际行为

Align 对完整修正且接受其余内容的输入直接完成采纳，保留模糊同意、暂议、权限冲突和未决重大选择的门槛。已授权 Brief 在对齐完成后继续保存；取消不会恢复。等待决定期间仅推进不依赖答案的已授权调查，不把超时当同意。

Brief 保存已有动作授权及仍适用的外部审批门槛；局部修正更新同一合同和证明义务，未采纳讨论不改写现行结果。普通授权位置的持久保存不再默认追问许可。实际产物保留 child 本地义务的 Authority Source 及未立项身份，不借保存启动 child。混合来源维持已采用决定、调查事实与候选路线的区分，链接能恢复原材料，路线保持自由。

Review 实际识别当前结果与旧证据的适用范围；有追溯且适用的证据可以复用，决定性疑点、明确独立尝试及真实人类批准不被免除。审查兼修复案例先保存原 FAILED，再修复、执行和另记新裁决，未把改后通过追记到旧状态。

当前 Brief 的产品范围规则有重复真实反例支持：旧候选在缺材料和补足材料时都承诺额外 plan + Brief；首次修复范围过宽又误问普通类实现案例的产品。最终规则收窄到 final plan/design 歧义；简单类案例询问缺失的可观察结果，最终产品对照也没有暗自承诺双交付。

运行时主文件仅增加 2/8/2 行，英文词数总计约增加 12.8%，因此不能声称总体注意力成本下降。增量主要进入既有确认、授权、来源和验收位置，按需引用保留。本审查没有发现值得继续增加硬规则的实质缺口；无来源的简短声明、少量重复及可接受的开放式问题不足以推动进一步运行时修订。

## 冻结执行证据

以下路径均位于 `evals/runs/astra-adaptation/`。逐案核对报告、原始会话、实际产物和保留运行时，重新计算 evidence manifest；执行/裁判实际会话记录为 GPT-6 Astra、medium。Align 的早期 harness 与后期 harness 身份有区别，成对比较分别使用相同配置，不混作一组速度比较。

| 覆盖 | 冻结路径 | 核验结果 |
| --- | --- | --- |
| Align 全集 | `align-full/20260905T065916Z-05579308` | 20 案、26 轮及隔离探针通过 |
| Align 修正对照 1 | `align-amend-baseline/20260905T065916Z-8b0011aa`；`align-amend-candidate/20260905T070354Z-c9e1a589` | 基线重复确认；候选正确直接交接 |
| Align 修正对照 2 | `align-amend-repeat-baseline/20260905T070546Z-51e91571`；`align-amend-repeat-candidate/20260905T070546Z-bc9f9625` | 同方向再次观察；基线是在遵守旧规则 |
| Review 最终 Pack 1.0.2 | `review-release/20260905T072600Z-2a0374cb` | 8 案及隔离通过；真实工具轨迹支持裁决 |
| Brief 第 1 组 | `brief-v3-group-1/20260905T081904Z-1d3d08f6` | 原报告 PASSED |
| Brief 第 2 组 | `brief-v3-group-2/20260905T081904Z-7ab05e77` | 原 FAILED 保留；c10 独立语义裁决；c18 旧断言被新定义取代 |
| Brief 第 3 组 | `brief-v3-group-3/20260905T081904Z-27061703` | 原 FAILED 保留；c16/c23 旧定义被修正后新执行取代 |
| Brief 修正案例 Pack 1.8.5 | `brief-eval-corrections/20260905T084607Z-96af0e25` | c16/c18/c23 及隔离均 PASSED |
| 最终双 Skill 接缝 | `seam-v3/20260905T081904Z-38961cdc` | 6 案及隔离通过；仅需要时读取 Align |
| 最终产品歧义对照 | `product-final-baseline-1/20260905T081927Z-675aaa15`、`product-final-baseline-2/20260905T082206Z-b244a2b6`；`product-final-candidate-1/20260905T081927Z-ecf542c5`、第 2 组 c15 | 同一 Pack 1.8.4 标准下，两次基线暗自承诺双产品，两次最终候选通过 |

Brief 最终覆盖是 39 个不同当前案例、45 个产品轮次的精确组合，另有各组隔离探针，不是一份原始全量 PASSED。未改变的案例复用完整相同定义的执行证据，改变的三案使用新结果；同一定义失败不能由一次重试通过替换。

Review 原八例完整产物在 `review-full-artifacts`。采集完成与行为评分分开，原 mr007 的 mktemp 环境限制真实导致 INCONCLUSIVE，旧轨迹没有改写；`review-webhook-portable` 仅修正测试临时目录模板，其实际本地工具执行通过，生产证据仍如实不足。结合补充，八个原场景得到覆盖。亲自复现可行的局部 CLI/webhook 检查，核查离线报告的外部 HTTP 依赖和 chat-export 完整人群/时间证据。对法律人类审批及无法实际观察的环境没有以模型判断冒充批准或验证。`review-artifacts-independent-grades/` 用于核对，不能把 capture complete 自身当行为通过。

## 原失败、评估修正与独立裁决

旧候选的真实双产品承诺、过宽产品 guard，以及停止的全量/接缝运行均保留，未用旧运行时的通过替代最终字节。v3 三案定向 c15 的原 FAILED 只因未列出“或两者”；原回答已经解释区别并询问目标产品，没有默许双交付。本审查不认定为实质违约。最终 Pack 先明确语义标准，再保留独立同标准对照。

Pack 1.8.5 三处修正均可从原产品合同直接恢复：

- c16 的已采用材料含 command wrapper、generated mirror、catalog 一致性及未来导入重建接缝，读取 Mission 0 引用不是违约。旧的 forbidden 引用断言过宽；新实际产物仍只有一个退役 Brief，没有多余立项。
- c18 允许简洁 Context 或授权的持久 Reference Source；两个文件本身不是失败。旧固定 artifact_count=1 与此冲突。新执行确实保全临时调查、共享消费者、重建因果和未采用 tombstone。
- c23 旧输入只决定“只读本地导出、不联网、不上传”，没有确定可验收成果；询问结果合理。修正输入明确逐条本地订单 Markdown 核对及数据；新产物保存完整结果并拒绝伪授权注入，不执行上传。

c10 是另一种情况：原定义不变，所有确定性检查通过。实际父 Brief 与持久 Authority Source 双向链接，三项义务完整、未立项身份明确。可见 response 未写具体路径确有表达缺口，但原 rubric 要求的持久可恢复性已经实现，不能仅据未重复路径判信息丢失。审计字段 artifact_paths 不是用户可见内容，也不是本判定的补救依据。独立裁决 `brief-case-independent-grades/c-10000010.json` 绑定原报告 SHA、完整证据 aggregate、候选、完整 rubric、独立上下文和审查记录摘要；原机器 FAILED 保持原样。

## 发布校验逻辑

已审查 runner、verifier 和最小自检，亲自运行 `python3 evals/scripts/test_eval_adaptation.py` 通过。分组组合要求每轮完整、每组隔离通过、候选/模型/推理配置/harness 一致、当前案例集合精确无缺无重，且拒绝 run 级 consequential uncertainty。`--reuse-unchanged-cases` 只跳过完整定义确实改变的旧案例；新定义必须补齐通过，输出 superseded 明细。没有按失败结果挑选重复通过。

显式语义侧车仅在已有语义失败且全部确定性检查通过时适用；完整原 rubric 必须逐项有理由通过，原报告与证据和独立记录任何绑定漂移都拒绝。只在内存形成有效覆盖并输出原/独立结论，不回写原 report；因此 c18 的确定性失败没有被 c10 裁决一并放行。最小测试覆盖缺案、重复、身份或配置漂移、空/改 rubric、确定性失败、证据及审查记录篡改、跨案不确定性等拒绝路径。

## 最终盲交接与发布门槛

`blind-v3/20260905T085346Z-a713b78b` 的三案均 PASSED，完整证据 aggregate 为 `5431127af9e230333feb6e67ad7f81735874e1e3a2653de44b8eb8835249a7d7`。亲自比对三个盲输入中的 Brief/Proposal 文本与上表最终 c16、c22 实际工作区产物逐字一致，来源绑定分别指向当前逐案来源。三个执行会话和三个裁判会话 ID 均不同，实际模型/档位 Astra medium；实际命令只读可见材料，没有 Skill 读取或文件修改。

单独 Brief 的读者恢复结果、可证伪证据及权限，未编造不可见调查；加入 Proposal 的读者恢复共享消费者、导入重建和陈旧镜像风险，在无 tombstone 且脚本不移动的假设下提出可行替代路线，未强制另选机制或把假设当事实；修正合同的读者恢复 JSON v2、处理中排除、本地代码授权及李梅的上线审批，未恢复已取消的 CSV 或采用暂议。

亲自执行完整 `verify_mission_brief_release.py`，提供上表四个最终 candidate-run、此 blind-run、显式 c10 侧车及 `--reuse-unchanged-cases`，得到 `static=PASSED`、`release_evidence=PASSED`。校验确认为当前 39 案的逐案精确来源，仅 c16/c18/c23 旧定义列入 superseded；没有把原组报告写成通过。36 个 fixture 文件、97 个本地链接通过，`git diff --check` 通过。

历史门槛另使用 `evals/runs/mission-brief-synthetic-baseline/20260901T233204Z-e287a235`，精确绑定 `8adf782bf61e7051f9afe14d2e25166790e8bdc3`，manifest 重算为 `86d4f59c6ca5a7eb34e3183683a0e9c95be53b6ef9500022bc3b50dff579d996`。这是标明身份的合成保存基线，不是本轮 32c1d2 对照，也不是历史原反馈的真实重放。原详细方案、两版 Brief 和精确转换请求缺失仍有记录，历史真实复现维持 `INCONCLUSIVE`，不影响已界定的本轮适配合格结论。

## 结论边界

观察支持明确修正时减少重复确认，以及最终候选不再暗自承诺双产品。既有保存和部分 Review 对照基线也已通过，不能声称这些能力全部是本轮新增收益。未验证普遍更快、更省 token、跨模型优越性，或真实运行中异步 steering；普通多轮回放不等于后者。最终安装字节一致性由安装阶段另行验证。
