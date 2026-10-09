# 半DIY申研PS修改

`semi-diy-ps-revision` 是一套面向“已经有 PS 初稿”的 Codex Skill 与工作流。它不从零代写文书，而是帮助申请者研究目标项目，并把中介或自己写出的初稿修改成更有记忆点、逻辑更完整、与项目更匹配的 PS。CV、经历库和项目材料能提高核对深度，但不是开始审阅的前提；只有 PS、批注和项目官网也可以直接进入工作流。

## 为什么需要半DIY修改

很多同学会选择由中介完成第一版文书。文书老师通常熟悉申请写作，却不一定来自你的专业，也未必完整理解你学过的课程、实习中真正做过的工作、项目方法，以及目标学位具体训练什么。因此，初稿即使语言流畅，仍可能出现：

- 专业概念或工作内容有细小但关键的偏差；
- 把团队工作写成个人独立负责，或把结果写得过满；
- 只扩写 CV，没有写出理解如何形成；
- 罗列学校课程，却没有解释它们补足什么能力；
- 不同学校只替换名称，缺少真正的项目适配；
- 修改意见散落在多个 Word 版本里，问题是否解决无法追踪。

申请者最了解自己的经历，但未必知道如何把资料、官网和多个文书版本组织成稳定的修改流程。这个 Skill 让 Agent 负责读取、研究、比较和审阅，让申请者负责提供真实材料、判断表达是否代表自己，并决定最终版本。

## 它做什么

- 把 CV、个人经历和项目材料整理成一次生成、跨项目复用的 `Applicant_Master_Profile.md`；
- 在没有 CV 或准备材料时，把当前 PS 正文、批注和申请者确认作为临时证据基础，直接开始审阅；
- 从申请者主动提供的项目官网出发，生成每个项目独立的 `Programme_Research_Memo.md`；
- 读取已有 DOCX 初稿，区分当前正文、接受/拒绝的修订、Word 批注；
- 先做整篇论证审阅，再给少量、可直接粘贴到 Word 的段落批注；
- 比较新旧版本，判断原问题是否解决、是否产生新问题；
- 按申请者授权的范围重构、扩充和包装经历，包括为可调整的 FYP/项目提出候选机制、细节和叙事方案；
- 在提交前复核项目匹配、题目、字数、文件一致性和语言。

修改时以录取说服力为第一目标：先判断招生官应该记住怎样的申请人，再处理故事推进、素材取舍、能力缺口和项目匹配。事实核查是必要底线，但不会替代内容判断，也不会为了预防假想质疑而堆叠限定语、责任范围说明或其他防御性表述。Skill 会尽量保留原文和文书老师已有的“活人感”，只在内容确实需要时改写。

## 它不做什么

- 不从零编造经历并代写整篇 PS；
- 不以“语言更高级”为理由重写已经有效的句子；
- 不替代申请者确认个人事实和最终表达；
- 不承诺录取，不自动填写或提交申请；
- 不以修改 CV 为主线。CV 是可选的一致性参照，不是 PS 审阅的必需输入；缺少 CV 时不会假装已经完成跨文件核对。

## 环境要求

- Codex 或支持 `SKILL.md` 的 Agent 环境；
- Python 3（仅 DOCX 修订与批注提取脚本需要，使用标准库，无额外依赖）；
- 项目研究阶段需要联网访问学校官方网页。

## 安装

发布到 GitHub 后可使用 Skills CLI：

```powershell
npx skills add 0imzero/semi-diy-ps-revision -g
```

也可以克隆仓库，并把整个 `semi-diy-ps-revision` 文件夹放到 Codex 的 skills 目录：

```text
%USERPROFILE%\.codex\skills\semi-diy-ps-revision
```

安装后，在新的 Codex 对话中使用 `$semi-diy-ps-revision`。Skill 也允许根据请求自动匹配。

## 推荐文件夹结构

详细说明见 [`assets/workspace-structure.md`](assets/workspace-structure.md)。核心原则是：

```text
Graduate_Application/
├─ CV/
├─ Personal_Materials/
├─ Academic_Projects/
├─ Applicant_Master_Profile.md       # 全部项目共用，只保留一份
├─ HKU_MDASC/
│  ├─ Programme_Info.md
│  ├─ Programme_Research_Memo.md
│  ├─ PS_Drafts/
│  ├─ Reviews/
│  └─ Final/
└─ Another_Programme/
   └─ ...
```

根目录存放长期复用资料；每个学校项目有独立文件夹。不要把 `Applicant_Master_Profile.md` 复制到各项目中，否则后续更新容易出现多个冲突版本。

## 开始前准备什么

### 只有 PS 也可以开始

最低输入是：一份已有 PS、申请者自己的批注或说明（如有），以及目标项目的官方 URL。Skill 会把当前正文当作工作中的经历版本，把 Word 批注和修订当作待判断的修改意图，并只追问会改变主线、可信度或项目匹配的少量问题。

此模式可以完成项目研究、整体审阅、逐条批注、新旧版本比较和中文回译。它暂时不能替代 CV、推荐信和申请表之间的一致性核对；这些材料之后补充即可，不需要为了开始修改先建立完整资料库。

### 根目录：一次准备、持续更新

1. `CV/`：当前 CV，必要时加入旧版或补充说明；
2. `Personal_Materials/`：实习、活动、动机和职业方向，可使用 [`assets/applicant-materials-template.md`](assets/applicant-materials-template.md)；
3. `Academic_Projects/`：项目报告、展示、代码说明、反馈等；
4. 其他能帮助理解真实经历的文件。

资料不需要先写成漂亮英文。第一人称、按 STAR（Situation、Task、Action、Result）具体记录，再补充“我学到了什么”和“我还缺少什么能力”，比一开始追求 PS 文风更有价值。

### 每个项目：分别准备

1. 创建项目文件夹，例如 `HKU_MDASC/`；
2. 复制并填写 [`assets/programme-info-template.md`](assets/programme-info-template.md)，最重要的是项目官方 URL；
3. 把已有 PS 初稿放入 `PS_Drafts/`；
4. 如有申请系统题目、字数限制或独立短文，也写入 `Programme_Info.md`。

## 完整工作流

| 阶段 | 申请者准备/输入 | Agent 做什么 | 主要输出 |
| --- | --- | --- | --- |
| 1. 建立申请人档案（可选，一次） | CV、个人经历、学术项目、动机与职业方向 | 读取全部材料，用 STAR + 反思 + 能力缺口整理证据，并提出少量高价值补问 | 根目录 `Applicant_Master_Profile.md` |
| 2. 提供目标项目 | 项目文件夹、学校与项目全名、入学年份、申请者主动提供的官网、题目和字数（如有） | 检查输入是否足以开始研究 | `Programme_Info.md` |
| 3. 研究项目（每个项目一次并按需更新） | `Programme_Info.md`，主档案如有 | 从给定官网进入，沿课程、招生、项目体验等官方页面研究，判断项目真正训练什么并映射现有个人证据 | `Programme_Research_Memo.md` |
| 4. 提取已有 PS | 当前 DOCX 初稿 | 只读提取正文、拒绝修订、全部修订、批注及锚点 | `Reviews/PS_<version>_Review_Extraction.json` |
| 5. 整体审阅 | 项目 Memo + 当前 PS，主档案如有 | 先判断主线、段落功能、证据递进、能力缺口、Why Programme 和职业方向 | `Reviews/PS_Overall_Review_<version>.md` |
| 6. 段落批注 | 整体审阅 + 指定段落或完整 PS | 只处理实质问题，提供精确原句、问题、第一人称中文批注与英文修改参考 | `Reviews/PS_Paragraph_Comments_<version>.md`（可选汇总） |
| 7. 比较新版本 | 旧版、新版、之前的审阅 | 独立重建两个版本，分类为已解决、部分解决、未解决和新问题 | `Reviews/PS_Version_Comparison_<old>_<new>.md` |
| 8. 提交前终审 | 最新 PS、项目要求、可用的 CV/推荐信/申请表 | 检查主线、真实性、项目事实、题目、字数、一致性与文件卫生 | `Final/PS_Final_Check.md` |

有完整材料时，推荐顺序是：申请人档案 → 项目研究 → 整体审阅 → 逐条批注 → 版本比较 → 终审。第二个项目不需要重新生成一份申请人档案。

只有 PS 时，使用快捷路径：项目研究 → 提取 PS/批注 → 整体审阅 → 逐条批注 → 版本比较 → 终审。之后拿到 CV 或其他材料，再补做跨文件一致性检查。

## 改写与包装的边界

PS 不是审计报告。对已经存在的经历，Skill 可以重新排序、合并、删减、扩写和转换叙事角度，也可以把原文隐含的决策、机制、转折、反思和能力缺口写清楚。若申请者明确说明 FYP、课程项目或某个场景的细节可以调整，Skill 可以提出更完整的候选机制、例子、过程和表达，由申请者确认后采用。

边界不是“只能改措辞”，而是不能凭空制造固定事实，例如不存在的雇主、正式职位、奖项、量化成绩、已完成成果、学校课程或职业保证。对于团队范围、因果强度和不确定性，只在它们会实质影响可信度时处理；不会默认在正文里加入防御性限定。

## 一个合格 PS 的基本逻辑

授课型硕士 PS 通常需要形成下面的推进关系：

```text
真实动机
  → 经历证据与理解递进
  → 当前能力缺口
  → 目标项目提供的具体下一步
  → 可信的职业发展
```

这不是固定的五段模板，而是一条论证链。每个经历都要回答“它证明什么、我的理解发生了什么变化、为什么下一个经历或这个学位是必要的”。

需要特别避免：CV 扩写、经历堆砌、课程清单、官网宣传册、把授课型硕士 PS 写成研究计划，以及把应届生职业目标写成资深岗位说明书。段落批注必须提出一项实际修改；如果一段已经有效，就不为了留下审阅痕迹而解释哪些内容可以保留或哪些事实没有问题。

## 使用示例

### 生成一次性申请人档案

```text
使用 $semi-diy-ps-revision。请读取当前申请主文件夹中的 CV、个人资料和学术项目，生成根目录 Applicant_Master_Profile.md。先尽量使用现有信息，最后只问会影响 PS 选材和定位的问题，不要开始写 PS。
```

### 研究一个新项目

```text
使用 $semi-diy-ps-revision。当前目录是一个新的项目文件夹，Programme_Info.md 中有我提供的官网。请读取父目录 Applicant_Master_Profile.md，从该官网出发研究项目，并生成 Programme_Research_Memo.md。
```

### 审阅中介初稿

```text
使用 $semi-diy-ps-revision。请结合父目录申请人档案和本项目 Programme_Research_Memo.md，读取 PS_Drafts/PS_v1_Original.docx。先生成整体审阅，不要马上逐句重写。
```

### 没有 CV，直接审阅 PS

```text
使用 $semi-diy-ps-revision。我现在只有 PS、里面的批注和项目官网，没有 CV 或准备材料。请先研究项目，再把 PS 正文作为工作证据基础做整体审阅。只关注能明显提升录取说服力的问题，不要为了预防质疑加入防御性表述；我说明可以调整的项目经历，可以给出更完整的候选写法让我确认。
```

### 逐段修改与比较版本

```text
继续上一轮审阅，从第一段开始，只对实质问题给可粘贴进 Word 的第一人称中文批注和英文修改参考。
```

```text
请比较 PS_v1_Original.docx 和 PS_v2.docx，判断之前的问题哪些已解决、部分解决、未解决，以及新版是否产生新问题。
```

## DOCX 提取脚本

Skill 会在需要时调用：

```powershell
python -X utf8 scripts/extract_docx_review.py INPUT.docx -o review.json
python -X utf8 scripts/extract_docx_review.py INPUT.docx --format markdown -o review.md
```

脚本不会修改源文件。JSON 主要字段为 `paragraphs.accepted`、`paragraphs.rejected`、`paragraphs.all`、`comments`、`changes` 和 `word_counts`。

## 使用限制与隐私

- Agent 能帮助发现材料中的矛盾与缺口，但申请者仍需确认最终事实和措辞；
- 学校课程、项目结构和申请要求会变化，最终提交前应重新核对官方页面与申请系统；
- 不要把无法公开的客户信息、证件、账号或推荐人隐私上传到公开仓库；
- 公开分享案例时使用合成或匿名材料，不提交真实申请人的 CV、PS、联系方式或完整主档案；
- 任何录取结果都受多项因素影响，本项目只提供工作流，不保证录取。

## 许可证

MIT License。见 [`LICENSE`](LICENSE)。
