# Course Exam Review

[English](README.md) | [简体中文](README.zh-CN.md)

Create professional exam-review materials from courseware, class notes, teacher priorities, and exam requirements. Combine knowledge organization, focused core-topic review, and predicted questions with reference answers as requested, with clear hierarchy and support for understanding and lookup. Deliver Markdown, Word, or PDF as requested.

## Usage

Install the complete `course-exam-review` folder in a skill directory supported by your agent, preserving `SKILL.md`, `references/`, `assets/`, and `scripts/` relationships. Discovery and invocation depend on the host; the skill does not require a specific model or private path.

Provide course materials and specify modes, scope, exam information, and output requirements. For example:

> Use course-exam-review to combine focused core-topic review and short-answer reference answers from the attachments into one PDF. Follow teacher-designated priorities and use one column.

The agent must ask about unresolved key requirements. It must not select every mode automatically or assume another course's question types, marks, or exam structure. Retain existing examples within scope. New explanatory examples in knowledge/core modes require a user request or agreement. Compact two-column layout requires explicit selection.

## Consistent output style

Default to black-and-white A4, one column, and compact continuous layout. Contents is separate with right-aligned page numbers. Use clear hierarchy, paragraphs for concepts, and numbering only for actual steps. No question-range headers. Shared settings unify fonts, spacing, tables, and formulas; professional math layout leaves clearance for indices and fractions.

Three fixed examples in `assets/examples/` each include a PDF and editable JSON source. They demonstrate style, not required subjects, counts, marks, or page lengths. Reading order, template usage, and acceptance are in `references/style-examples.md`.

`assets/templates/compact-review.json` holds shared styles; `scripts/render_review.py` is an optional single-column PDF renderer. It requires Python 3, reportlab, svglib, and, for math blocks, Node and mathjax-full 3.x. Fonts come from local configuration; fonts and third-party runtimes are not distributed here. Equivalent tools may generate Word, Markdown, or PDF, but must implement the sample style and actual verification.

## Quality and boundaries

Gap classification, existing-question coverage checks, computational verification, concrete acceptance checks, and optional collaboration improve reliability. They do not authorize expansion, automatic prediction, or course-scope changes. Check accuracy, completeness, and actual rendering separately. User templates and explicit requirements take priority.

Fixed samples use newly written algorithm material without private user data. Fonts, engines, and environments may change line breaks and pagination; verify actual output rather than promising pixel-identical cross-platform results. English instructions do not require English deliverables; follow user language requirements and course materials.
