# Course Notes

[English](README.md) | [简体中文](README.zh-CN.md)

Turn courseware and supplementary materials into complete, understandable Chinese Markdown notes following the teaching sequence and using original figures. Defaults to Typora for everyday coursework, chapter review, and long-term accumulation.

## Suitable tasks

- Organize one or more PPT, PPTX, or PDF chapters into readable notes.
- Add new material to existing notes or edit specified passages only.
- Preserve definitions, conditions, formulas, algorithms, and useful figures while consolidating repetition.

Use the other collection skills for textbook-style restructuring or exam prediction.

## Defaults

Preserve topics, sequence, hierarchy, and all knowledge, including material that was not emphasized. Explain concisely without removing necessary connections and derivations. Select representative examples without omitting unique methods or conditions; retain every example if explicitly requested.

Output Markdown only by default. Add PDF, Word, or previews only on explicit request. Do not proactively create exercise, teacher-review, predicted-topic, or new explanatory-example modules. Retain useful source examples according to the agreed treatment.

Default examples use clear screenshots of original questions and existing answers without additional solution reasoning. Request editable organization or enhanced explanation explicitly. Ask about important source gaps or questionable answers; do not change questions or guess answers.

Prefer original figures, usually under `笔记/配图/章节标题/`, referenced relatively. Editable Markdown does not guarantee identical rendering across readers; use Typora extensions only for that target.

## Examples

> Use course-notes for this chapter. Retain the teaching sequence, all knowledge, and useful original figures. Apply default example treatment and save in the course's notes directory.

> Update existing notes with only the new attachment content; retain other text, annotations, and figures.

> Organize these two chapters as separate Markdown files. Convert examples into editable text/math; ask before adding new solution explanations.

## Efficiency

- Record confirmed course preferences without turning temporary requirements into permanent defaults.
- Validate extraction caches against content and parsing settings, not filenames alone.
- Separate structure recognition, writing, figure/format work, and review without a mandatory sample-approval gate.
- Use available tools such as MarkItDown if suitable; check important formulas and diagrams against original pages.

## Automated checks

With Python 3:

```bash
python3 scripts/check_notes.py "/path/to/chapter.md"
```

Accepts multiple notes. JSON output flags common image-path issues, heading jumps, unclosed fences, placeholders, and conflicting image basenames. Exit 0 means no warnings; exit 1 means review needed, not necessarily an error.

The script is read-only, does not render images/math, and does not verify knowledge or answers. It supports common inline/reference/HTML images; inspect complex Markdown manually. Previously tested with five constructed input groups, not all Markdown dialects or complete course workflows.

## Files

- [SKILL.md](SKILL.md): Entry workflow and boundaries.
- [writing-guide.md](references/writing-guide.md): Explanations, examples, and text/figure integration.
- [formatting.md](references/formatting.md): Paths, filenames, and Markdown conventions.
- [workflow.md](references/workflow.md): Configuration, caching, and efficiency.
- [quality.md](references/quality.md): Five internal quality measures.
- [check_notes.py](scripts/check_notes.py): Read-only checks.

## Installation and boundaries

Install this complete directory with relative paths intact, not just the README. Host tools define installation paths and invocation; [SKILL.md](SKILL.md) is the entrypoint.

Parsing, reading, and export capabilities come from the environment. State unavailable checks honestly; static checks are not actual rendering validation. Gap classification, question-based checks, computation, acceptance checks, and optional subagents must not change purpose, default format, or editing permissions. Question-based checks are conditional and do not automatically generate exercises.

English instructions do not change the Chinese-note default or override an explicit request for another output language.
