---
name: course-exam-review
description: Build professional course exam-review materials from courseware, class notes, teacher priorities, and exam requirements. Supports three combinable modes—knowledge organization, focused core-topic review, and predicted questions with reference answers—for understanding, application, and open-book lookup. Output Word, PDF, or Markdown as requested. Use for creating or updating exam-review materials, not isolated concept questions, full textbook writing, or slide-by-slide transcription.
---

# Course Exam Review

## Original purpose and non-negotiable boundaries

Prepare professional review materials grounded in the actual course and exam requirements. The user selects knowledge organization, focused core-topic review, and/or predicted questions with reference answers. If not specified, ask about modes and substantive requirements first; do not fill in modes, question types, counts, or marks for the user. Conditions invented for a simulated test are not real user preferences and do not establish that the requirement-elicitation flow was tested.

Knowledge organization preserves chapter structure. Focused review uses meaningful chapter/module → theme → specific-knowledge hierarchy, grouping concepts, principles, conditions, formulas, and distinctions rather than presenting everything at the same heading level. Question mode follows actual scope, wording, and marks rather than replacing organization with a fixed answer template.

Retain existing source examples within scope and content permissions. In knowledge/core-topic modes, add new explanatory examples only when requested to aid understanding or explicitly accepted. Selecting question mode authorizes questions and answers within its confirmed scope; these permissions are distinct.

Follow the user's approved professional review style: black-and-white, single-column, connected prose, clear hierarchy by default. Ask before compact two-column layout; do not automatically adopt textbook-style covers, blue accents, or chapter page breaks. The five quality improvements are internal checks and efficiency measures, not permission to expand scope, add unsolicited question sets, or change modes.

The English language of this skill does not prescribe English deliverables. Follow the user's requested output language and course materials, retaining their terminology and notation. Chinese reference samples illustrate Chinese typography, not a requirement to translate other courses into Chinese.

## Entry: confirm the task first

Before organizing materials, confirm the required modes; multiple selections are allowed:
- **Knowledge organization:** Organize by chapter, preserving what is needed for understanding and application.
- **Focused core-topic review:** Explain explicit priorities together and reduce scattered lookup.
- **Predicted questions with reference answers:** Organize short-answer, calculation, multiple-choice, fill-in, or other types according to exam requirements.

If already selected, record the choice and proceed without asking again. Otherwise ask and wait; do not select modes independently or generate all modes by default. For multiple modes, confirm whether to combine or deliver separately unless already specified.

Ask together about missing requirements that materially change the result: course/material scope, basis for priorities, mode-specific details, editing permissions, output format, and use. For prediction mode, confirm known question types, count or coverage target, marks, and difficulty. If unknown, ask which handling the user accepts rather than inventing an exam structure.

Reuse established requirements without repeated confirmation. Ask about ambiguities affecting content or delivery; do not substitute personal assumptions. Before the answer, inventory readable materials but do not write content dependent on it. Explicit constraints and applicable layout defaults may be executed directly; do not ask about every routine implementation detail.

## Materials and evidence

Use actual teaching materials and latest teacher requirements as primary sources, together with user notes. Check access, completeness, and parseability; do not claim unread materials were reviewed. Record the read scope.

Maintain an internal inventory and chapter → knowledge → source → destination mapping to track omissions, repetitions, conflicts, and updates. Extract text with available tools; revisit original figures for formulas, diagrams, hierarchy, and scans. Text conversion is not proof of accurate understanding or preserved layout. Read materials relevant to the current stage; extraction may be cached, but recheck affected content after input changes.

Judge importance using explicit teacher priorities, exam scope, course objectives, and knowledge dependencies—not length or frequency alone. Distinguish stated priorities from compiler predictions. Do not invent teacher intentions, likelihood percentages, or official answers. Do not transfer a particular course's five questions, twenty marks each, no calculations, or two-method requirements to other courses.

For missing/conflicting materials or ambiguous key symbols, explain the concrete issue in conversation and ask how to proceed. Do not silently guess or leave unresolved “to verify” markers in the final document. Continue unaffected sections.

## Writing and organization

After confirming modes, read [Content and question writing](references/content.md) and execute only selected modes.

Organize by course chapter or explicit priority modules. Name headings accurately and group related definitions, principles, conditions, formulas, examples, and comparisons. Preserve connections required for understanding and solving problems; do not reduce the material to conclusion-only outlines or substitute slide-by-slide copying for organization.

Write professionally, coherently, and directly. Use paragraphs for conceptual answers, numbering for genuinely ordered steps, and tables for suitable comparisons. Bold key concepts, conditions, and conclusions selectively; do not bold entire paragraphs or number every sentence.

Do not repeatedly say “the slides say,” “the teacher covered,” or “compiled from the materials.” Do not add source pages to each item by default. Exclude unrelated disclaimers, prediction reminders, editing notes, production-process text, and revision slogans. Retain real applicability conditions, assumptions, errors, and limitations.

Consolidate necessary external references at the end where appropriate, retaining specific citations when needed. Do not confuse external supplements with taught content. Keep source mappings internal. Add source-page navigation only when explicitly requested.

## Layout and output

When typesetting, read [Layout and export](references/layout.md) and [Fixed examples and shared template](references/style-examples.md). Inspect the selected mode's fixed PDF and content source, then implement the shared styles. References travel with the skill; do not depend on chat history or private file paths. User templates and approved samples take priority; otherwise use the single-column default. Use two columns only on explicit request.

Deliver the requested format, not every format automatically. Preserve the original and save clearly named updates unless overwriting is authorized. Synchronize content and versions when multiple formats are requested.

## Content verification and optional collaboration

For coverage review, question-based checks, computational verification, or splitting long materials, follow [Quality checks and optional collaboration](references/quality.md). Findings support revision and internal tracking, not changes to purpose, content permissions, or layout. Subagents are optional.

## Deliverable checks

- Compare with materials and confirmed scope for coverage, facts, notation, conditions, formulas, and examples. Remove repetition without removing useful knowledge.
- Check question/answer correspondence, depth relative to marks, calculations, and answer uniqueness in multiple-choice questions. Do not call answers official or questions certain to appear without evidence.
- Check hierarchy, numbering, contents, printed pages, cross-references, and keyword lookup.
- Whenever possible, actually render Word/PDF to inspect fonts, mathematical indices, tables, images, pagination, and whitespace. Source settings alone are insufficient.
- Verify final delivered files, not just temporary versions. After edits, recheck affected pages and contents; global reflow requires a full-document check.
- Distinguish static review, actual rendering, and content verification. Report unavailable checks in delivery notes, not the document body; never claim they were completed.

Deliver files and a brief verification summary. Do not publish externally unless explicitly requested. The skill does not depend on another chat, private paths, a model, or a particular tool; operate within actual environment capabilities.
