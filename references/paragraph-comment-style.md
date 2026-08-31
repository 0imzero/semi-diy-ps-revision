# Paragraph comment workflow

Use this route only after the whole-document review exists or has been completed in the same task. Move through the PS in order and comment only on material issues.

## Scope each comment precisely

- Anchor one sentence when only that sentence is wrong.
- Anchor a span when several sentences share one issue.
- Use a whole-paragraph comment only for a genuinely shared structural problem.
- Do not change a sentence that is already good merely to demonstrate editing.

Before writing a comment, determine what the source says, why it matters in the complete PS, and what exact change would improve it.

## Paste-ready contract

For each material issue, use:

```text
对应原句：
> exact source span

问题：
short explanation outside the Word comment

批注内容：
> paste-ready first-person Chinese comment

修改参考：
> natural English replacement

原文约N词，修改后约M词。
```

The Chinese comment should sound like the applicant discussing their draft with a document adviser:

- “这里我想表达的是……”
- “这里和我的实际经历不太一致……”
- “这个内容本身我想保留，但能不能把重点放在……”
- “我目前能做到的是……，还没有形成文中所说的……”

Avoid reviewer-report language, vague phrases such as “建议优化表达”, praise or debate about another reviewer, forced politeness, inflated claims and generic AI transitions.

## Replacement examples

Preserve facts, tone and paragraph function. Do not invent a result, mechanism, course status, responsibility or emotional reaction.

When length parity matters, compare English word counts:

`ratio = abs(replacement_words - source_words) / source_words`

Normally keep the replacement within about 10% of the source. A larger reduction is appropriate when redundancy or excessive technical detail is the diagnosed problem; disclose the counts instead of padding.

Keep technical detail that proves individual contribution. Compress detail that turns the PS into a report or paper abstract, but replace it with the actual interpretation or growth.

## Existing comments and tracked changes

Judge existing feedback from scratch. Treat a comment as evidence of intention, not as the correct diagnosis. Absorb useful reasoning into the new applicant-voice comment without naming or debating the previous reviewer inside the paste-ready text.

Outside the comment, state when the new feedback fully supersedes an old comment and it may be deleted. Discard inaccurate or immaterial advice.

## Continuation

When the user says “继续”, handle the next unreviewed paragraph. Do not repeat the overall diagnosis, ask which paragraph is next, or add unrelated advice.

If the user wants a single reusable artifact, append comments to `Reviews/PS_Paragraph_Comments_<version>.md`. An annotated DOCX is optional and should be created only when requested; never overwrite the source.

