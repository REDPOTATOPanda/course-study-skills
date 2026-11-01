# Layout and Export

## Priority order

Explicit user requirements > user templates or approved samples > this skill's fixed examples and shared styles > other defaults here. See [Fixed examples and shared template](style-examples.md) for examples and implementation. Default to A4 portrait, single-column, balancing continuous reading and printed lookup; use two columns only on explicit request. Ask when unspecified options such as landscape, a cover, or chapter page breaks materially change the result; do not copy special designs from other documents automatically.

Keep the contents separate from the body, targeting one page with right-aligned page numbers. Use tab stops, contents fields, or layout tools—not manually typed spaces. If too long, remove unnecessary displayed levels first; if still unreadable, ask whether multiple pages are acceptable. Do not force it into tiny type. Generate page numbers from final output rather than estimating from length.

Keep sections continuous within chapters; do not force every question, section, or knowledge point onto a new page. Allow natural page flow. Keep headings with a modest amount of following text; do not make entire long answers or tables unbreakable and create large gaps. Follow the user's chapter-break instructions; confirm if unspecified and materially consequential.

## Default style scheme

This is a conventional textbook-like review scheme, not a national universal standard. Establish named styles using available fonts and briefly describe them at delivery, not in the document body.

| Role | Chinese font | Western text/digits | Size and weight |
|---|---|---|---|
| Document title | Hei/sans-serif family | Matching family | 20 pt, bold |
| Chapter/module | Hei/sans-serif family | Matching family | 16 pt, bold |
| Section/full question | Hei/sans-serif family | Matching family | 12 pt, bold |
| Subsection | Hei/sans-serif family | Matching family | 11 pt, bold |
| Body/answer | Song/serif family | Times New Roman or equivalent serif | 11 pt, regular |
| Figure/table caption | Song/serif family | Same Western body family | 9.5 pt, regular |
| Footnote/page number | Song/serif family | Same Western body family | 9 pt, regular |
| Mathematics | Cambria Math or available math font | Mathematical glyphs | Main size about 11 pt; indices follow math rules |

Specify Chinese and Western fonts separately to avoid arbitrary fallback. Songti or Source Han Serif with corresponding sans-serif headings are possible Chinese choices. Check character coverage and actual weight after substitution. Use real bold or reliable weights for body emphasis, not larger text as a substitute.

Start with margins around 18–22 mm, body leading about 1.3–1.4 times the font size, and 3–5 pt after paragraphs; adjust for formula density. Do not save paper through tiny body type or fixed leading that clips indices. Display long formulas separately and allow extra height for fractions and multi-line derivations.

Preserve image aspect ratios; do not stretch or call simple enlargement high-resolution restoration. Prefer originals or verifiable vector redraws. Identify the model/object in captions with concise useful explanation. Give tables clear headers; allow long tables to split with repeated headers.

If a cover is requested, use restrained professional design with the actual course name and document type. Do not invent institution, teacher, or author information. Define and verify numbering for cover, contents, and body.

## Implement by format

- **Word:** Use native paragraph, heading, caption, and editable math styles/objects. Check fractions, matrices, and indices after converting source notation. Use updateable contents and page fields; avoid unnecessary external file links.
- **PDF:** Keep text searchable and fonts displaying correctly and embedded where possible; use contents links and chapter bookmarks where supported. Check actual pages, font substitution, formula overflow, and clipping.
- **Markdown:** Preserve semantic headings and math source, with fonts/styles/pagination settings appropriate to the export tool. Without export and rendering, do not claim final sizes or pagination or invent page numbers.

When possible, render and inspect each page and separately check extracted-text coverage. Successful rendering does not prove no omissions; file existence does not mean layout acceptance. Updated multi-format outputs must share the same content version.

## Visual baseline for review materials

Maintain black-and-white, single-column, compact, connected reading. Group contents by chapter and use clear body hierarchy. Distinguish questions from reference-answer labels; answers primarily use paragraphs, with numbering only for real steps. Keep headers, page numbers, and separator rules restrained and consistent. Let related knowledge flow naturally; do not repeatedly break pages for module symmetry. Knowledge mode uses chapter → section → necessary subdivision; core-topic mode develops themes; question mode groups questions/answers by chapter. Sample wording, undersized type, special page numbering, or two-column layout are not universal requirements.

When the user emphasizes paper-saving printing, ask whether they prefer continuous single-column or compact two-column layout. Default to single-column until selected. In two columns, retain readable text and math; span or rearrange complex tables and wide formulas rather than squash them. Deep-blue accents and designed covers are not this skill's defaults.

Fixed samples retain a compact black-and-white style. Headers must not show question ranges such as “Questions X–Y.” Improve formula clearance, heading spacing, and table readability. Shared settings are in `../assets/templates/compact-review.json`; sample page counts do not constrain real documents.
