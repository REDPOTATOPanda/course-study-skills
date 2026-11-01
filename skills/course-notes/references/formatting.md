# Files and Markdown Formatting

## Default directory structure

```text
project/
└── 笔记/
    ├── 第X章 章节标题.md
    └── 配图/
        └── 第X章 章节标题/
            └── p018-结构图.png
```

- Name files with full chapter titles, preserving original numbering. Handle illegal filename characters only; do not arbitrarily add version numbers.
- Save multiple chapters separately by default; merge when requested. Ask if ownership or delivery organization is unclear.
- Group figures by chapter. Filenames may contain source pages and semantic names for internal tracing; add short source identifiers to prevent collisions. Do not expose page numbers as captions.
- Use relative image paths; enclose paths containing spaces in angle brackets, e.g. `![结构示意](<配图/第X章 章节标题/p018-结构图.png>)`.
- Capture complete semantic regions when figures depend on arrows, legends, or grouped objects. Crop irrelevant presentation UI without losing conditions. Preserve aspect ratios; enlargement is not high-resolution recovery.
- Keep conversion/extraction/coverage records and debugging files in the workspace, not final figure directories.
- Read the original before local edits. Update in place when explicitly asked to update existing chapter notes. If only courseware is supplied and a same-named file exists, preserve it first; if needed, save “章节标题-整理稿.md” and explain.
- Do not move or delete historical images without authorization. After authorized moves, check every reference.
- Save files when possible. Provide Markdown in chat when requested. If writing is unavailable, provide copyable content and explain the limitation.

## Headings and text

Prefer the user's template or existing notes. Otherwise:

```markdown
# 第X章 章节标题
## 一、一级主题
### 1.1 知识点
#### 1.1.1 必要细分
```

Determine actual topic ownership before numbering; do not mechanically follow digits or create empty headings. Original chapter numbering is acceptable; remain consistent throughout. Begin with a short chapter knowledge thread, not provenance or process notes.

Bold concepts, key conditions, and conclusions selectively. Short comprehension notes may use blockquotes. Use tables for comparisons, not narrow cells for long derivations. Label code-fence languages; comments explain key operations rather than translating each line. Use `<br>` for necessary table-cell breaks and blank lines between blocks.

## Formulas and compatibility

- Prefer `$...$` and `$$...$$`; use LaTeX for indices, e.g. `R_1` and `x^2`.
- Only when Typora is explicitly the target may ordinary text use `~subscript~` and `^superscript^` extensions; check settings and preview. Do not assume other readers support them.
- Convert non-example tables to editable tables when appropriate and keep formulas editable where possible. Apply the selected treatment to examples; do not duplicate readable screenshot content.
- Do not proactively add forced page breaks, publication font settings, or Word/PDF workflows. Implement format-specific tools, settings, and actual checks when export is requested. Markdown alone does not prove final font sizes or pagination.

## Everyday note presentation baseline

Output MD only by default, without a proactive PDF preview. Use chapter → topic → concept → necessary subdivisions. Keep the opening thread short, explain related concepts together, bold key phrases, compare in tables, and retain original figures. Use blockquotes for genuinely useful explanations or rules; do not turn the whole file into cards. Preserve existing headings, image paths, and annotations. Do not insert publication settings into everyday notes. Two-column layout is relevant only to requested print exports; ask before using it, without changing the continuous Markdown source structure.
