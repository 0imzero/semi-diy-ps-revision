# 推荐工作区结构

一个申请人只建立一个主文件夹。长期复用的资料放在根目录；每个学校项目单独建文件夹。

```text
Graduate_Application/
├─ CV/
│  ├─ CV_Current.pdf
│  └─ CV_Current.docx
├─ Personal_Materials/
│  ├─ Personal_Experiences.md
│  └─ Motivation_and_Career.md
├─ Academic_Projects/
│  ├─ Project_A/
│  └─ Project_B/
├─ Applicant_Master_Profile.md
├─ HKU_MDASC/
│  ├─ Programme_Info.md
│  ├─ Programme_Research_Memo.md
│  ├─ PS_Drafts/
│  │  ├─ PS_v1_Original.docx
│  │  └─ PS_v2.docx
│  ├─ Reviews/
│  │  ├─ PS_v1_Review_Extraction.json
│  │  ├─ PS_Overall_Review_v1.md
│  │  ├─ PS_Paragraph_Comments_v1.md
│  │  └─ PS_Version_Comparison_v1_v2.md
│  └─ Final/
│     └─ PS_Final_Check.md
└─ Another_University_Programme/
   └─ ...
```

## 只准备一次

- `CV/`：当前 CV 与必要的旧版本；它是事实与一致性输入，但本工作流不重点修改 CV。
- `Personal_Materials/`：个人经历、动机、职业方向、补充问答。
- `Academic_Projects/`：报告、展示、代码说明、导师反馈等证据。
- `Applicant_Master_Profile.md`：Agent 汇总生成的可复用主档案。

主档案不复制进项目文件夹。多个项目从同一个根目录档案选择不同证据，避免版本漂移。

## 每个项目单独准备

- `Programme_Info.md`：申请人提供项目官网入口、入学年份、题目与字数。
- `Programme_Research_Memo.md`：Agent 针对该项目的研究结论。
- `PS_Drafts/`：该项目的原始初稿与后续版本。
- `Reviews/`：抽取结果、整体审阅、段落批注与版本比较。
- `Final/`：提交前检查。

文件夹名不必与示例完全相同，但同一申请季应保持一致。不要把不同项目的 PS 和研究 Memo 混在同一目录。

