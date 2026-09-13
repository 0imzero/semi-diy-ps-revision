# Whole-document PS review

Review the complete existing PS before suggesting sentence edits. Use the accepted DOCX body as the current draft, while reading rejected changes and comments as separate review evidence. The primary standard is whether the essay makes the applicant memorable, credible and desirable for the target programme. Accuracy is a baseline, not the organising principle of the review.

## Required context

Read the parent `Applicant_Master_Profile.md`, the programme's `Programme_Research_Memo.md`, `Programme_Info.md`, the current PS and relevant prior reviews. If the programme memo is absent, explain that programme-fit conclusions are provisional and run programme research first when the official URL is available.

For DOCX input, run:

```powershell
python -X utf8 scripts/extract_docx_review.py INPUT.docx -o Reviews/PS_<version>_Review_Extraction.json
```

Use `--format markdown` for an additional readable extraction. Never overwrite the DOCX.

## Pass 1: reconstruct the admissions argument

State in one sentence who the admissions reader should remember the applicant as and what the draft asks that reader to believe. A viable taught-master PS usually follows:

`real motivation -> evidence and developing understanding -> present ability gap -> programme-specific next step -> credible career progression`

This is a logic test, not a mandatory paragraph template.

Check:

- **Opening:** Is the scene specific, engaging and useful? Does it create curiosity and introduce a question the later essay genuinely develops?
- **Applicant proposition:** Is there a distinctive and programme-relevant identity, or only a list of competent experiences?
- **Evidence chain:** What does each experience prove? Does it change the applicant's understanding or merely repeat a CV bullet? Is it the strongest available material for this function?
- **Evidence weight:** Is paragraph space proportional to admissions value? Should an experience be expanded, compressed, merged, replaced or removed?
- **Progression:** Are chronology and causal development accurate? Is a later insight projected backwards into an earlier experience?
- **Ability gap:** Does the applicant show readiness without sounding as if they have already mastered the field?
- **Programme fit:** Does each named resource answer a demonstrated gap and make the degree feel necessary rather than merely relevant?
- **Career direction:** Is the first step credible, and does the longer progression follow from the training sought?
- **Reader impact:** What concrete scene, decision or insight will remain after one reading? Has cautious abstraction flattened the applicant's strongest material?
- **Completeness:** Can every paragraph's function be named, and does the ending resolve the thesis persuasively?

## Common structural failures

- CV expansion: actions appear, but judgement and development do not.
- Experience pile: several strong examples do not form one argument.
- Course list: programme resources are named without an applicant-specific gap.
- Brochure paragraph: official wording is paraphrased but not interpreted.
- Research proposal voice: a taught-master applicant claims a mature framework they have not established.
- Inflated job description: the career goal begins at senior responsibility rather than a plausible entry step.
- Manufactured motivation: abstract passion or an anecdote carries conclusions unsupported by the experience.

## Pass 2: paragraph audit

First decide whether the paragraph deserves its place and whether its function advances the admissions argument. Then check evidence before reflection, proportional technical detail, natural transitions, reader interest and student-level voice. Do not edit a sentence merely because another synonym or more cautious formulation is possible.

Comment only when at least one is true:

1. the applicant proposition or narrative progression would become stronger;
2. the paragraph's function, evidence selection or weighting is weak;
3. chronology or causal development is distorted;
4. repetition or technical reporting materially slows the essay;
5. the programme link does not answer a demonstrated need;
6. tone weakens reader interest or places the applicant at the wrong level;
7. a factual or professional error creates a material credibility problem;
8. a change clearly improves persuasiveness, fit or readability.

Use fact checking proportionately. Accept user-confirmed details. Raise a fact or scope issue during paragraph review only when it materially changes the story, responsibility, result or programme claim. Save exhaustive consistency checking for final review.

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

