# Efficiency and Course Configuration

## Course-level configuration

Record confirmed preferences in the course project's `work/course-notes/config.md`. Reuse an equivalent existing configuration rather than creating another. New records contain only explicit user requirements and adopted skill defaults, distinguishing the two. Do not include private accounts, other-course habits, or inferred requirements.

Useful fields: course and material scope, output location, separate or merged chapters, terminology and symbols, heading style, example treatment, depth of added explanation, figure paths, target reader, and confirmation date. Ask about unresolved substantive requirements; a configuration file must not decide them for the user.

Read relevant configuration at the start of each task. Current explicit requirements take priority. Temporary exceptions affect only the current task; update course defaults only when the user explicitly requests ongoing use. Confirm conflicts between configuration and current materials or requests. Configuration records preferences; it does not authorize uploads, deletions, or other external actions.

Do not put configuration in the notes. Without persistence, record it in the current conversation and explain that it cannot be reused across tasks.

## Staged work

1. Inventory materials and recognize structure, chapter and topic ownership, figures/tables, and example locations; record coverage mappings.
2. Write using the confirmed structure, preserving conditions, derivations, and necessary explanations while controlling repetition.
3. Extract or crop relevant original figures and implement formulas, tables, and image references. Obtain figures needed for understanding earlier if necessary; this is not the first permitted point to inspect images.
4. Check coverage and facts, run mechanical checks, inspect presentation, and verify the actual delivered files.

Stages reduce rework, not establish approval gates. Do not require a sample approval before proceeding; ask only about genuine ambiguities affecting the result.

## Extraction caches and incremental updates

Store extracted text, page mappings, necessary original figures, and manifests in `work/course-notes/cache/` or a usable persistent temporary workspace, separate from final figure directories. Read chapters or page ranges as needed instead of repeatedly loading all materials into context.

The manifest must at least record source content fingerprints (e.g. SHA-256), converter and version, result-affecting options, output-file inventory, and page mappings. Filename, path, or modification time alone is insufficient to establish reuse. Re-extract if caches are missing, corrupt, or fingerprint-mismatched; do not treat old extraction as current source material.

After a file changes, re-extract and recheck affected content if changed pages can be reliably located; otherwise re-extract the whole source file. Page shifts, chapter restructuring, or notation changes may affect later references; expand verification accordingly. Never overwrite handwritten annotations or existing notes with cached output.

Caches are not factual authorities; verify against sources. Return to the original page when a crop cannot express complete conditions. Do not promise fixed token-saving or speedup percentages.

## Optional parsers and text/figure choices

Use available text extraction or conversion tools such as MarkItDown. Check availability first and parse only needed materials. MarkItDown is a Microsoft tool, but a third-party skill wrapping it is not automatically an official Microsoft skill. No plugin installation is mandatory for this workflow.

Text conversion supports search, coverage checking, and initial organization; it does not prove formulas, complex tables, or reading order correct. Check important diagrams, temporal relationships, matrices, subscripts/superscripts, and OCR results against original pages. Follow environment permissions and user authorization before network OCR or external services; do not upload by default.

Keep prose, simple tables, and mathematical expressions editable where possible. Preserve readable screenshots for complex structural diagrams, timing diagrams, and original questions according to confirmed policies. Avoid screenshotting everything and then fully transcribing the same material, but retain short explanations needed to interpret figures. Do not change the agreed example treatment for tool convenience.

## Limits of automated checks

`check_notes.py` checks local paths for common Markdown inline images, reference-style images, and HTML images; flags remote images as unverified; and checks heading jumps, fence closure, common placeholders, and identical basenames across different image paths. It does not render Markdown, inspect image pixels, or verify derivations, semantic hierarchy, answers, or coverage.

Complex Markdown extensions may trigger false positives. Keep reports in work records or delivery notes, not the note body. Fix confirmed problems specifically; do not automatically rewrite headings or delete content.
