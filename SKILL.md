---
name: semi-diy-ps-revision
description: Review and iteratively improve an existing graduate-application Personal Statement or Statement of Purpose using the applicant's reusable evidence base and current official programme information. Use for semi-DIY applicants who need applicant profiling, programme research, whole-document diagnosis, paste-ready paragraph comments, DOCX tracked-change extraction, version comparison, or final submission review. Do not use for CV rewriting, from-scratch ghostwriting, or application submission.
---

# Semi-DIY PS Revision

Help the applicant turn an existing PS draft into a more memorable and persuasive application. Prioritise applicant positioning, narrative logic, evidence selection and programme fit. Preserve confirmed facts and the applicant's own judgement, but treat verification as a guardrail rather than the purpose of revision.

## Route the request

Choose the smallest route that completes the request:

1. **Applicant profile** — create or update the reusable root-level `Applicant_Master_Profile.md`. Read [references/applicant-profile.md](references/applicant-profile.md).
2. **Programme research** — start from the official URL supplied in `Programme_Info.md` and create the programme-specific `Programme_Research_Memo.md`. Read [references/programme-research.md](references/programme-research.md).
3. **Overall PS review** — extract the current DOCX when needed, then audit the complete argument before sentence editing. Read [references/ps-review-framework.md](references/ps-review-framework.md).
4. **Paragraph comments** — comment only on material issues and produce paste-ready feedback. Read [references/paragraph-comment-style.md](references/paragraph-comment-style.md).
5. **New version comparison** — reconstruct the newer version independently and classify earlier issues as solved, partly solved, unresolved or newly introduced. Read [references/version-final-review.md](references/version-final-review.md).
6. **Final review** — check submission readiness, programme facts, prompt/word limit and cross-document consistency. Read [references/version-final-review.md](references/version-final-review.md).

For routes 3–6, use `scripts/extract_docx_review.py` whenever body text, tracked changes or Word comments matter. Do not treat a comment or rejected change as prose already present in the PS.

## Shared invariants

- Work on an existing applicant- or intermediary-written draft. Do not ghostwrite a PS from nothing.
- Keep `Applicant_Master_Profile.md` once at the applicant workspace root. Reuse it across all programme folders; never copy it into each folder.
- Require a user-supplied official programme URL before programme research. Follow relevant official pages from that starting point and date the memo.
- Keep each programme's `Programme_Info.md`, `Programme_Research_Memo.md`, drafts, reviews and final check inside that programme folder.
- Review from whole to part: applicant proposition, reader interest, central thesis and evidence chain first; paragraph comments second.
- Select evidence by relevance, not prestige. A PS normally needs one thesis and two or three mutually reinforcing experiences, not every CV entry.
- Be willing to restructure, merge, cut, replace or substantially reweight material when that clearly strengthens the admissions case.
- Judge changes in this order: memorable applicant identity, narrative movement, evidence strength and weighting, ability gap, programme fit, reader impact, then final factual consistency.
- Never invent metrics, outcomes, responsibilities, emotions, causal findings, course availability or career guarantees.
- Distinguish completed action, personal interpretation, possible mechanism and future ability gap.
- Treat uncertain details proportionately. Ask focused questions when they affect the chosen story or credibility; otherwise record them for final review rather than interrupting useful revision.
- Verify unstable programme facts through current official sources. Label electives, capstones, internships, exchanges and tracks accurately.
- Never overwrite an input DOCX. Write analysis artifacts to `Reviews/` and submission checks to `Final/`.
- Keep the applicant's natural voice. Different wording is not a defect unless a change materially improves persuasiveness, logic, fit, reader interest or readability.
- Accept facts the user has explicitly confirmed. Do not turn every scope note, team contribution or possible ambiguity into a defensive caveat.
- Every Word comment must request a concrete revision. Do not use comments to list what should remain unchanged, reassure the writer about their own prose or demonstrate that a review occurred. If there is no useful action, leave no comment.

## Workspace and output contract

Use [assets/workspace-structure.md](assets/workspace-structure.md) when setting up a workspace. Use [assets/applicant-materials-template.md](assets/applicant-materials-template.md) and [assets/programme-info-template.md](assets/programme-info-template.md) as copyable inputs.

Expected outputs:

- applicant root: `Applicant_Master_Profile.md`;
- programme folder: `Programme_Research_Memo.md`;
- extraction: `Reviews/PS_<version>_Review_Extraction.json`;
- overall review: `Reviews/PS_Overall_Review_<version>.md`;
- optional paragraph set: `Reviews/PS_Paragraph_Comments_<version>.md`;
- version comparison: `Reviews/PS_Version_Comparison_<old>_<new>.md`;
- final review: `Final/PS_Final_Check.md`.

When the request spans several routes, preserve this dependency order:

`Applicant profile (once) -> Programme research (per programme) -> Overall review -> Paragraph comments -> Version comparison -> Final review`
