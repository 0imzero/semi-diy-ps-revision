# Version comparison and final review

## Compare a new PS version

Extract and reconstruct each DOCX independently. Do not assume the newer file contains all earlier accepted changes, and do not compare only visible comments.

Read:

- applicant master profile and CV when available;
- programme memo and info;
- earlier overall review and paragraph comments;
- extraction/body of the old version;
- extraction/body of the new version.

For every material earlier issue, classify:

- **Solved** — the underlying factual, logical or fit problem is resolved;
- **Partly solved** — direction improved but the problem remains material;
- **Unresolved** — body text did not address it;
- **New issue** — the revision introduced a new factual, logical, tonal or length problem.

Reassess the whole argument after comparison. A local fix can damage chronology, repetition or programme positioning elsewhere.

If the user is reviewing meaning rather than requesting another rewrite, a faithful Chinese back-translation of the new accepted body may be provided after comparison. Preserve the English version's claims, emphasis and uncertainty so the applicant can spot semantic drift.

Write `Reviews/PS_Version_Comparison_<old>_<new>.md`:

```markdown
# PS Version Comparison — <old> to <new>

## Executive Assessment
## Change Summary
## Earlier-Issue Status
| Earlier issue | Status | Evidence in new version | Remaining action |
## New Issues Introduced
## Current Argument and Flow
## Submission-Level Priorities
```

## Final submission review

Use the latest body, not filenames alone. Recheck current official programme facts when they appear in the essay or may have changed.

This is the stage for exhaustive factual and application-wide checking. Earlier creative and paragraph-review stages should remain focused on admissions argument, narrative and fit unless a material credibility problem is already visible.

Audit:

1. applicant proposition, central thesis, reader impact and paragraph functions;
2. narrative progression, evidence weighting and programme fit;
3. truth, chronology, responsibility and quantified claims;
4. programme name, degree terminology, courses and opportunities;
5. prompt coverage and exact word/character limit;
6. CV, PS, recommendations and application-form consistency when those files are available; otherwise mark this check as not performed rather than blocking PS review;
7. grammar, readability, natural voice and formatting;
8. unresolved comments, tracked deletions, placeholders and accidental metadata.

Write `Final/PS_Final_Check.md` with exactly one status:

- `可以提交` — no material issue remains; or
- `修改后提交` — list the smallest set of changes required before submission.

Suggested structure:

```markdown
# PS Final Check

## Status
可以提交 / 修改后提交

## Submission Summary
## Material Issues Before Submission
## Programme-Fact Check
## Prompt and Length Check
## Cross-Document Consistency
## Language and File Hygiene
## Final Actions
```

Do not label a draft “可以提交” merely because it is grammatical. Submission readiness requires a coherent, truthful, programme-specific argument that satisfies the actual prompt and limit.

When cross-document materials are unavailable, `可以提交` means the PS itself has no material issue under the evidence reviewed. State the outstanding cross-document check once in the final file without turning it into repeated defensive language.
