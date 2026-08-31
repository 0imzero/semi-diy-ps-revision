# Whole-document PS review

Review the complete existing PS before suggesting sentence edits. Use the accepted DOCX body as the current draft, while reading rejected changes and comments as separate review evidence.

## Required context

Read the parent `Applicant_Master_Profile.md`, the programme's `Programme_Research_Memo.md`, `Programme_Info.md`, the current PS and relevant prior reviews. If the programme memo is absent, explain that programme-fit conclusions are provisional and run programme research first when the official URL is available.

For DOCX input, run:

```powershell
python -X utf8 scripts/extract_docx_review.py INPUT.docx -o Reviews/PS_<version>_Review_Extraction.json
```

Use `--format markdown` for an additional readable extraction. Never overwrite the DOCX.

## Pass 1: reconstruct the argument

State in one sentence what the draft asks the admissions reader to believe. A viable taught-master PS usually follows:

`real motivation -> evidence and developing understanding -> present ability gap -> programme-specific next step -> credible career progression`

This is a logic test, not a mandatory paragraph template.

Check:

- **Opening:** Is the scene specific, true and useful? Does it introduce a question the later essay genuinely develops?
- **Evidence chain:** What does each experience prove? Does it change the applicant's understanding or merely repeat a CV bullet?
- **Progression:** Are chronology and causal development accurate? Is a later insight projected backwards into an earlier experience?
- **Ability gap:** Does the applicant show readiness without sounding as if they have already mastered the field?
- **Programme fit:** Does each named resource answer a demonstrated gap? Is the wording accurate and current?
- **Career direction:** Is the first step credible, and does the longer progression follow from the training sought?
- **Completeness:** Can every paragraph's function be named, and does the ending resolve the thesis?

## Common structural failures

- CV expansion: actions appear, but judgement and development do not.
- Experience pile: several strong examples do not form one argument.
- Course list: programme resources are named without an applicant-specific gap.
- Brochure paragraph: official wording is paraphrased but not interpreted.
- Research proposal voice: a taught-master applicant claims a mature framework they have not established.
- Inflated job description: the career goal begins at senior responsibility rather than a plausible entry step.
- Manufactured motivation: abstract passion or an anecdote carries conclusions unsupported by the experience.

## Pass 2: paragraph audit

For each paragraph, check one clear function, evidence before reflection, proportional technical detail, accurate association/causation, natural transitions, factual consistency, and student-level voice. Do not edit a sentence merely because another synonym is possible.

Comment only when at least one is true:

1. a fact, role, chronology or programme claim is wrong;
2. the paragraph's function or logic is unclear;
3. the evidence does not support the conclusion;
4. repetition materially slows the essay;
5. tone places the applicant at the wrong academic or professional level;
6. a change clearly improves fit, credibility or readability.

## Output

Write `Reviews/PS_Overall_Review_<version>.md`:

```markdown
# Overall PS Review — <version>

## Overall Assessment
## Current One-Sentence Thesis
## Paragraph Function Table
| Paragraph | Current function | Evidence used | Link to thesis | Main issue | Action |
## Material to Retain
## Main Structural Problems
## Evidence Selection and Weight
## Ability Gap
## Why Programme
## Career Direction
## Recommended Argument Order
## Revision Priorities
## Information to Develop
```

Put the argument map inside this file; do not create another mandatory map. Prioritise a small number of changes that materially improve the document. Do not rewrite the full PS unless the user explicitly asks after the diagnosis.

