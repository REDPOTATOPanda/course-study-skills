# Layout and Format Implementation

Read when designing styles or typesetting exports. Preserve these cover, contents, pagination, emphasis, and format-specific rules; current user instructions override conflicting defaults.

## Fonts, sizes, and layout

Create a complete style sheet first and apply it consistently. User templates or publication samples take precedence. Otherwise use the following **A4 portrait single-column starting point**, adjusting for content, measured fonts, and printing needs. This is an optional scheme, not a national universal standard. Reassess legibility for other paper sizes, two columns, or landscape rather than inheriting fixed values.

| Role | Chinese font | Western/digits | Size and weight | Paragraph guidance |
|---|---|---|---|---|
| Chapter | Hei/sans-serif | Times New Roman | 18 pt, bold | 12 pt before, 8 after; keep with following content |
| Section | Hei/sans-serif | Times New Roman | 14 pt, bold | 9 before, 4 after; keep with following content |
| Subsection | Hei/sans-serif | Times New Roman | 12 pt, bold | 6 before, 3 after |
| Body/example body | Song/serif | Times New Roman | 11 pt, regular | About 1.35× leading, 3 pt after |
| Body emphasis | Same body family | Same body family | Same size, actual corresponding bold weight | Same paragraph settings; necessary phrases only |
| Table body | Song/serif | Times New Roman | 10.5–11 pt, regular; bold header | Automatic height |
| Figure/table caption | Song/serif | Times New Roman | 9.5 pt, regular | Adjacent; 3–4 pt spacing |
| Necessary academic footnote | Song/serif | Times New Roman | 9 pt, regular | Automatic height, no clipping |
| Header/page/index aids | Song/serif | Times New Roman | 9 pt, regular | Consistent position and baseline |
| Mathematics | Body font for Chinese explanation | Cambria Math or compatible math font | Main symbols about 11 pt; italic variables, upright operators | Height-aware leading and appropriate clearance |

Choose actually available Chinese fonts such as Songti/Songti SC/Source Han Serif and Heiti/Heiti SC/Source Han Sans, then use them consistently. If unavailable, select and record an embeddable substitute; do not rely on silent substitution. Check that emphasis renders as the intended weight and hierarchy remains clear. Do not switch size or mix arbitrary fonts for emphasis. Bold math may denote vectors/matrices; never change symbol weight merely for visual emphasis. Check actual weights and Chinese/Western glyph fonts. TTC collections may default to a bold subfont; filenames alone do not prove regular body weight. Do not squeeze pages by reducing body text below 10.5 pt by default; reassess and explain genuinely special layouts.

Start A4 margins around 18–20 mm, increasing the inner edge for binding if needed. Provide a restrained separate course cover by default unless unwanted or already specified. Choose consistent indentation, alignment, header placement, and figure/table numbering. Combining modules requires identical heading sizes, baselines, positions, and body start points—not only margins. Joining existing PDFs alone is not unified typesetting.

### Course cover

- Full handouts follow cover → separate one-page contents → chapters. Do not add duplicate covers to local revisions without reason.
- Use the course name as main title, usually with a “Course Handout” subtitle; use “Open-Book Exam Course Handout” when explicitly intended. Take the course name from user instructions or unambiguous material titles; ask if uncertain rather than guessing. Render these labels naturally in the requested output language (e.g. “课程讲义”).
- Institution, department, teacher, term, compiler, and edition appear only when supplied and appropriate. Do not fill from historical identity information, fabricate, or leave blank/to-fill fields. Course name plus subtitle is a complete cover when other information is absent.
- Use moderate design rather than only a centered title and rule. Options include layered title areas, restrained coordinated colors, lines/bands, and course-related vector elements; no single motif or English subtitle is mandatory. Keep professional, coordinated with body fonts/colors, balanced in whitespace, and free of piled decorations, slogans, or unrelated explanations. Do not invent crests or institutional logos. Prefer supplied cover templates.
- For A4, start main titles at 24–28 pt sans-serif bold, subtitle about 14 pt, and necessary secondary information about 11 pt. Record actual choices in cover styles. Wrap long titles naturally; do not compress horizontally or enlarge arbitrarily to fill the page.
- No page number on the cover. Contents may use Roman numerals; body starts at 1 and continues. Contents entries refer to printed body pages; align PDF page labels where possible. Keep a separate cover without inserting blank recto/verso pairing pages.
- Check actual course/secondary information, fonts, and long-title fit. Contents and chapter 1 begin on subsequent pages. Cover whitespace is a composition choice, not permission for large gaps inside chapters.

### Pagination and formula rules

- Separate one-page contents; every chapter begins on a new page, chapter 1 after contents. Do not force odd-page starts or insert pairing blanks. Sections/subsections/concepts flow naturally within chapters; do not force each part onto its own page.
- Contents/chapter-start breaks do not apply within chapters. Allow automatic flow. Do not mark entire chapters, long tables/examples, or runs of paragraphs as keep-together. Do not chain keep-with-next or use large paragraph spacing to manufacture gaps.
- Keep a heading with the minimum following text needed to avoid an orphan. Short formulas, captions, and examples may stay together locally; longer content may split, wrap, or cross pages sensibly.
- For indexed expressions, fractions, and matrices, use automatic/minimum line heights, not clipping fixed heights. Check spacing inside formulas too; body leading cannot be blindly applied to multi-line math.
- Scale images proportionally. Coordinate diagram fonts, arrows, and spacing. Rearrange/split overly wide content meaningfully rather than squash it. Locally landscape pages can serve exceptionally wide tables without causing repeated breaks for ordinary sections.
- Save paper through removing redundant whitespace, sensible image scaling, and continuous flow—not sacrificing body legibility or necessary content.

## Implement by output format

No single format/tool is mandatory. Use available document/PDF/presentation skills for parsing, generation, and verification as appropriate; otherwise choose suitable tools under this guidance.

- **Word:** Native heading/body/caption/table styles and preferably editable native equations. Break after contents and before chapter headings; do not enable page-break-before for sections/subsections. Use right-aligned tabs or automatic contents. Check fixed leading, page/section breaks, and keep-with-next chains. Update contents/pages, avoid unnecessary external-link fields, and preserve necessary internal contents/page fields.
- **PDF:** Searchable text, correct fonts embedded where possible, clear math, undistorted figures. Verify separate one-page contents, aligned numbers, and chapter starts. Update contents pages, links, and bookmarks. If existing PDFs cannot be unified simply, re-typeset content; adding uniform headers alone does not establish consistency.
- **Markdown:** Real heading hierarchy, math syntax, stable image paths. Provide explicit export CSS/styles or renderer configuration and font requirements, including separate contents, chapter breaks, and no forced section/subsection breaks. Implement right-aligned printed contents numbers; anchor-only Markdown contents is not a substitute. Source/styles alone do not establish final fonts, sizes, or pagination. Generally do not keep entire section/article containers unbreakable; intra-chapter headings must not force breaks.
- For requested multi-format delivery, generate from consistent source or verify item by item. Synchronize all requested outputs after changes; do not leave mismatched Word/PDF content versions.

## Modern textbook style: default visual scheme

Without a user template, adopt modern textbook styling while retaining the complete style roles and chapter-break rules above. A4 portrait, one column, Song/serif body at 11 pt with compatible Western serif text; sans-serif chapter headings 18–19 pt, sections 13–14 pt, subsections 11–12 pt. Black body, low-saturation deep-blue headings and a few rules (e.g. #183D59), supported by pale gray-blue (e.g. #EDF3F6). Colors are adjustable starting points and must remain distinguishable in grayscale. Use about 1.4–1.5× body leading and 3–5 pt after paragraphs, adjusted to actual fonts; do not shrink body type to squeeze pages.

Express hierarchy through size, weight, and measured spacing. Put necessary captions next to figures/tables. Tables use clear headers and thin horizontal rules with fewer vertical/heavy borders. Do not make the whole handout into cards. Covers may combine layered titles, restrained color blocks, and course-related vector elements rather than only a centered title/rule. Use only actual supplied course information.

### Professional mathematical typography

Complex formulas must use a mathematical typesetting engine. Prefer XeLaTeX/LuaLaTeX suited to Chinese PDFs; with an existing HTML route or no TeX environment, MathJax may render LaTeX as vectors. Do not replace an otherwise usable workflow just for a tool name or force large dependencies on users. Use editable native OMML equations for Word and preserve LaTeX math source in Markdown. Do not simulate fractions, sums, matrices, or extensible delimiters with plain text and manual indices.

Unify inline/display math fonts and about 11–12 pt main size. Italicize variables; keep function names and explanatory subscripts upright. Set vector/matrix weights by meaning, not decoration. Check height, baseline, spacing, line breaks, and clearance for fractions/indices. Vector paths may be clear but not searchable/copyable; retain editable source and state this honestly rather than calling vectors editable equations. Report the actual engine; do not call MathJax XeLaTeX.

Compact two-column layout is optional for printing: ask first, keeping one column if unselected. Actual rendering, contents, and pagination checks remain required; listing style parameters alone is insufficient.
