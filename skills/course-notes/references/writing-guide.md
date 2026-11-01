# Writing and Example Guidelines

These are shared writing conventions. Subject matter in examples illustrates writing only; it is not mandatory content for every course. Choose a suitable approach for the knowledge type rather than forcing every section into a fixed labeled checklist.

## Standalone presentation and concise openings

The result must read as standalone course notes. Begin each chapter with a short knowledge thread, not source details, total page counts, processing scope, screenshot policies, or pagination explanations. Explain concepts and conclusions directly. Avoid navigation phrases such as “on slide X” or “the courseware mentions.” Captions and alt text describe content only. State necessary conditions directly as assumptions of the problem or method. Small external supplements must not masquerade as taught material; briefly identify them as supplements where relevant and retain necessary attribution without repetitive source reminders. Keep source mappings in the temporary workspace, not the notes.

For Chinese output, an opening may read “本章主线：函数依赖 → 范式 → 模式分解” without slide counts or editing explanations. Label an example “例：模式分解” and its answer “答案,” not “original slide question/answer (pXX).” Use corresponding natural labels for other requested output languages.

## Recover structure from subheadings

Courseware can have clear organization without an explicit contents page. For `6.1.1 Basic methods of instruction scheduling` and `6.1.2 Loop unrolling`, use context to determine whether both belong to chapter 6, section 1. If the latter slide also contains `1. Loop unrolling`, first determine whether it is a local item or a deeper topic. Do not create new sections solely from numbers or font size. Do not invent a missing parent title from numbering alone.

## Concepts: intuition and precision

Explain the problem addressed, precise meaning, and necessary small examples as needed for understanding; do not force all concepts into the same template. Intuition must not broaden a definition's scope. Concision reduces repetition, not necessary connections. Ask before adding extensive remedial teaching.

For a database view, for example, start with saving and naming a frequently used query rule, then explain that an ordinary view usually stores a query definition and retrieves data from underlying tables at query time, rather than freezing a previous result.

Add a short connection when concepts depend on each other. Preserve qualifications such as “usually,” “under this algorithm,” and “when these assumptions hold”; do not drop conditions for brevity.

## Syntax and operations

Use general syntax → concrete example with comments → explanation and pitfalls. Comments explain key operations rather than repeating every line literally. Identify required environments or implementation differences. Do not claim code passed tests if it was not run.

If asked only to annotate code, handle that code directly. If asked to write it into notes, read the original file and update locally.

## Formulas and theorems

State notation, assumptions, and conclusions. A formal statement / intuitive explanation table can help comparison; place long derivations in connected prose or display equations rather than narrow table cells.

Distinguish sufficient from necessary conditions, sample observations from general conclusions, and algorithm guarantees from properties that happen to hold for one input.

## Example-treatment options

By default, preserve original questions and existing answers, preferring clear screenshots; do not independently add solution reasoning. This is a configurable default, not a capability limit. The user may select:

- **Preserve originals:** Clear screenshots of the original question and answer, including existing steps; avoid duplicate transcription.
- **Editable organization:** When requested, convert to text, mathematical formulas, tables, or code while preserving question numbers, data, conditions, and meaning.
- **Enhanced explanation:** When requested, add reasoning, derivations, and answer explanations. Distinguish independent derivation from existing answers and do not claim the materials supplied it.

Use the default unless another treatment is requested. Confirm ambiguous requirements that affect the result. Never replace original questions with invented ones. If all examples are explicitly requested, retain each instead of applying representative selection.

## Algorithms and worked examples

Retain algorithm inputs, outputs, conditions, and original steps; preserve correspondence with original numbering. Briefly explain key meanings, without automatically creating additional walkthroughs.

Prefer clear screenshots of courseware questions followed by their answers, retaining original answer steps. Do not additionally write solution strategies, step-by-step calculations, intermediate states, or pitfalls by default. Expand when explicitly requested; when explaining a special branch, use an example that actually exercises it.

Select examples for the same concept by method and important cases:

- Of three routine questions differing only in numbers, retain the clearest one.
- Also retain a question using a different method or showing a boundary condition.
- If an omitted question contains a unique warning, integrate the warning into the text or retain that question.

Let coverage determine the count; do not enforce one or three examples per section. Put shared data before the questions. Usually place an example immediately after its concept, introduced by bold text rather than its own subsection. If screenshots are clear, add only a short question number or topic, not duplicate transcription. Re-typeset from the original question and answer only when screenshots remain unreadable after reasonable processing; retain question numbers, data, and conditions. If answers are missing or doubtful, ask whether to retain the question, add a solution, or handle it differently. Do not choose unilaterally or insert “answer unavailable” into the text by default. Keep a short missing-content marker only with user agreement. Continue unaffected work while awaiting answers.

## Integrate figures and prose

Provide the definitions or conditions needed to read a figure, then the original figure and an adjacent caption or explanation. Put example data tables before the question. Briefly explain instructional figures rather than stacking full-slide screenshots as a substitute for organization. Apply screenshot-first treatment to questions and answers without adding solution explanations.

## Consistency in updates

Read existing chapter notes and relevant references first; do not redesign the entire style. Temporary user adjustments apply only to their specified scope unless explicitly requested as future defaults.
