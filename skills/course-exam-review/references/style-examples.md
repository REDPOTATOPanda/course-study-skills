# Fixed Examples and Shared Template

The skill's purpose is professional exam-review materials in user-selected modes. A fixed style stabilizes presentation; it does not authorize expansion, mode changes, fixed question counts, or changes to exam structure. Examples are newly written, distributable content—not a real teacher's exam scope or a requirement to write about algorithms.

## When to read and precedence

Confirm modes and content requirements first. At typesetting time, read this file and `layout.md`, then inspect representative PDF pages and content sources for the selected modes. Do not claim to have consulted a sample from its filename alone. User templates and explicit instructions take priority, followed by fixed examples/shared styles. Samples constrain presentation, not exact sentences, heading numbering, or paragraph counts. Combined modes share styles and follow the user's merged/separate delivery choice without redundant contents pages.

| Mode | Required sample, relative to skill root | What to observe |
|---|---|---|
| Knowledge organization | `assets/examples/knowledge-outline.pdf` and matching `.json` | Chapter/section hierarchy; adjacent definitions, conditions, formulas, comparisons |
| Focused core-topic review | `assets/examples/core-focus.pdf` and matching `.json` | Hierarchy beneath priorities; problems, principles, conditions, distinctions—not flat lists |
| Predicted questions and answers | `assets/examples/questions-answers.pdf` and matching `.json` | Chapter-grouped contents; complete questions and reference answers; paragraphs versus numbered procedures |

Samples do not add explanatory examples. Add such examples in knowledge/core modes only when requested or accepted; preserve existing examples according to editing permissions. Four questions, their wording, and algorithm topics in the sample are not defaults; marks follow real requirements. Use two columns only when explicitly selected. This template is single-column.

## Fixed style and variable content

- Black-and-white A4, single-column, about 19 mm margins. Song/serif body at 11 pt, about 15.8 pt leading, 3 pt after paragraphs; adjust for actual fonts and formula height.
- Title 20 pt; modules 15–16 pt; sections/full questions 12 pt; necessary subsections 11 pt. Hei/sans-serif headings and selective bold phrases. Do not elevate procedures or local lists into modules.
- Separate contents page, right-aligned numbers generated and checked from final pagination. Body flows naturally; do not force each chapter, question, or concept onto a new page. Follow user chapter-break requirements. Handle long contents as in layout.md.
- Headers contain only necessary document identification, with a thin gray rule and consistent page numbers. A standalone question-prediction document uses “course name + question predictions” (Chinese example: “算法基础题目预测”), not a long “short-answer questions and reference answers” header. The main title may retain the full name. Name combined-mode headers according to user requirements. **Do not show question ranges in the upper-right corner**, in single or combined modes.
- Tables use light-gray headers, thin horizontal rules, and adequate cell padding. Use professional math layout with height-aware spacing, not text characters imitating fractions or sums. Align inline math with body baselines. Vector paths are not editable/searchable math text; retain LaTeX in the source.
- Do not introduce slide-attribution phrases, source-page tags, process notes, or disclaimers into the body. Retain actual applicability conditions and limitations.
- These are short samples; whitespace on their contents pages does not justify similar gaps in the body. Do not remove content, shrink fonts, or force breaks to reproduce their page counts.

## Reusable implementation

`assets/templates/compact-review.json` contains readable shared style parameters. `scripts/render_review.py` is an optional reference renderer for single-column PDFs, not a mandatory tool for all formats or a requirement to install identical dependencies elsewhere. Equivalent tools must preserve styles and sample appearance; changing engines need not change style.

The renderer requires Python 3, reportlab, and svglib; math blocks additionally require Node and mathjax-full 3.x. Prefer capabilities already available. Font files are selected through a local configuration, not author-machine paths. Each font needs `path`; TTC files also need an explicit `index`. Check glyph coverage, actual weight, and licensing. Font files are not distributed with this skill.

```json
{
  "regular": {"path": "/path/to/serif-regular.ttf"},
  "bold": {"path": "/path/to/serif-bold.ttf"},
  "heading": {"path": "/path/to/sans-bold.ttf"},
  "western": {"path": "/path/to/western-serif.ttf"},
  "western_italic": {"path": "/path/to/western-serif-italic.ttf"}
}
```

Write content from actual materials, not by importing sample knowledge into a new course. Follow matching sample JSON structure: `title` and `blocks`, with optional `running_title` for a short header. Blocks are heading (level 1–3), p, label, math (tex), and table (rows, optional widths). Text supports ReportLab paragraph markup such as `<b>` and `<br/>`; escape XML-special characters in ordinary prose. Inline Western text may use configured font tags. For complex inline LaTeX, use another route that supports inline mathematics, not raw source pasted into a p block. Rewrite or break wide formulas; the renderer will not squash them. Styles need not be edited inside the script.

```sh
python3 scripts/render_review.py content.json review.pdf \
  --fonts fonts.json --node node \
  --mathjax /path/to/node_modules/mathjax-full
```

Use native heading/body/caption/table styles and OMML equations in Word to implement the same style. Markdown retains semantic hierarchy, LaTeX, and export settings. Sample PDFs do not verify those other implementations or establish identical pagination across formats.

## Acceptance against samples

First verify content against confirmed scope, then compare hierarchy, compactness, fonts and weights, math spacing, tables, and headers with the sample. Check a separate contents page, correct final page numbers and links, no upper-right question range, and no concept-level forced page breaks. Let long content split naturally; check orphan headings, clipped math, table overflow, and abnormal gaps. Record actual rendering and content checks separately in delivery notes or internal records, not the review document body.
