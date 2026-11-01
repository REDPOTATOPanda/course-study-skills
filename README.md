# Course Study Skills

[English](README.md) | [简体中文](README.zh-CN.md)

**Scattered slides, a textbook that does not match your course, or exam materials you have no time to organize? Turn classroom materials into resources you can understand, revise from, and find your way around.**

Course Study Skills provides three independent Agent Skills for turning slides, class notes, and supplementary handouts into course notes, textbook-style handouts, or exam-review materials.

**[Download all skills](https://github.com/REDPOTATOPanda/course-study-skills/raw/refs/heads/main/downloads/course-study-skills.zip)** · **[Choose a skill](#choose-a-skill)** · **[View examples](#exam-review-examples)**

## Sound familiar?

### Your instructor shares slides, but the ideas still do not connect

A definition is on one slide, its formula on another, and important conditions are buried in a diagram. You can follow individual pages without seeing how the topic fits together.

Use **Course Notes** to organize concepts, principles, formulas, and original figures in the teaching sequence, retaining necessary explanations in Markdown notes you can keep updating.

### There is a textbook, but it does not match what is actually taught

Knowledge is scattered across slides, class notes, and supplementary materials. No single reference really corresponds to the course.

Use **Course Textbook Builder** to compile those materials into a coherent handout, explaining relationships between topics for systematic study and long-term reference.

### Exams are approaching, and your materials are hard to navigate

The slides are lengthy, priorities are scattered, and a rushed summary can lose the reasoning. Even in an open-book exam, having all the files does not make the right information easy to find.

Use **Course Exam Review** to organize knowledge, develop core priorities, or prepare predicted questions with reference answers around your actual exam scope and requirements.

### You already have useful notes and do not want to start over

New slides, supplementary explanations, and personal annotations keep accumulating. Regenerating everything can overwrite work you want to keep.

All three skills support updates within a defined scope, preserving unrelated text, annotations, and images so your materials can grow with the course.

## Why choose Course Study Skills?

### Support learning throughout the course

Everyday notes, systematic handouts, and exam-review materials serve different purposes. The three skills preserve the teaching sequence, build a knowledge structure, or organize around exam requirements. Use them independently or together as your needs change.

### Retain the reasoning, not just the conclusions

Definitions and formulas retain necessary assumptions, variable meanings, conceptual connections, and derivations. Look up results quickly while understanding why a method works, when it applies, and how it differs from related concepts.

### Ground the material in your actual course

Prioritize courseware, class notes, and instructor requirements, preserving the course's terminology and symbols. Ask about missing or conflicting materials and unclear requirements before proceeding, helping keep general knowledge aligned with what is taught.

### Organize the content and its presentation together

Arrange headings, contents, formulas, figures, tables, and examples for the intended use. The exam-review skill includes fixed examples for three modes and shared styles to support clear, consistent results for continuous reading and open-book lookup.

### Keep improving the work you already have

Organize chapter by chapter, add new materials, or revise selected passages while preserving unrelated content, annotations, and figures. Build on your work as the course progresses instead of regenerating everything each time.

### Produce editable, checkable resources worth keeping

Request Markdown, Word, or PDF. Check content separately from layout, including appropriate checks of formulas, figures, references, and final pagination, so materials are easier to edit, print, and archive.

## Choose a skill

| Your goal | Skill | Main result |
|---|---|---|
| Follow the course and turn slides into complete notes | [course-notes](skills/course-notes/README.md) | Markdown notes retaining the teaching sequence, knowledge details, and original figures |
| Compile scattered materials into a systematic standalone handout | [course-textbook-builder](skills/course-textbook-builder/README.md) | A coherent, fully structured, consistently typeset handout |
| Prepare review and open-book lookup materials around exam scope | [course-exam-review](skills/course-exam-review/README.md) | Organized knowledge, focused priorities, or questions with reference answers |

Use just the skill you need now, or take notes during the term, build a handout when needed, and prepare review materials before exams. There is no required sequence.

### Course Notes

For everyday coursework, chapter-by-chapter organization, and continuing updates.

Follow the course's teaching sequence and knowledge structure. Preserve definitions, principles, conditions, formulas, and useful original figures; consolidate repetition and add short connections needed for understanding. Retain existing questions and answers as requested, optionally converting them to editable content.

Default output is Markdown intended for Typora. Export Word or PDF only when explicitly requested.

### Course Textbook Builder

For courses without a suitable textbook, or where the textbook has little connection to actual teaching.

Organize scattered slides, notes, and knowledge into chapters, sections, and subsections. Explain conceptual relationships and retain necessary principles, derivations, applicability conditions, and examples to make the handout independently readable.

Unify the cover, contents, typography, formulas, figures, tables, and pagination. Deliver Word, PDF, or Markdown as requested.

### Course Exam Review

Choose one or more modes:

- **Knowledge organization:** Build a chapter-based knowledge structure with what is needed for understanding and application.
- **Focused core-topic review:** Develop explicit priorities with meaningful hierarchy, grouping concepts, principles, formulas, and method comparisons.
- **Predicted questions and reference answers:** Prepare questions and answers according to actual exam requirements, including short-answer, calculation, multiple-choice, and fill-in formats.

Confirm modes, scope, and output requirements before writing. Default to compact, clear single-column layout; choose two columns when appropriate for printing.

## Get started

### 1. Download and install

Get individual skills from the [download directory](downloads/README.md), or download the full collection.

Unzip and install complete skill folders in a location supported by your agent, or use its skill import feature. Preserve `SKILL.md`, `references/`, `assets/`, `scripts/`, and other supporting resources.

You can also clone the repository:

```bash
git clone https://github.com/REDPOTATOPanda/course-study-skills.git
```

The three skills are located in:

```text
skills/
├── course-notes/
├── course-textbook-builder/
└── course-exam-review/
```

Installation locations and invocation syntax depend on your tool.

### 2. Provide materials and describe the task

Share courseware, class notes, or an existing document, and describe the scope and result you want. The agent should ask about unresolved requirements before doing work that depends on them.

**Organize course notes**

> Use course-notes for chapter 3 in the attachment. Preserve the teaching sequence, all useful knowledge, and necessary original figures. Output Markdown. Retain original questions and existing answers without adding solution explanations.

**Build a textbook-style handout**

> Use course-textbook-builder to compile these slides and class notes into a coherent PDF handout. Explain connections between concepts and preserve necessary formulas, principles, and examples. Ask me about conflicting materials.

**Prepare exam-review materials**

> Use course-exam-review to combine focused core-topic review and predicted questions with reference answers into one PDF. Exam scope and instructor priorities are attached. Confirm unresolved requirements before starting.

**Update existing work**

> Update these notes with only the new courseware content. Preserve other text, annotations, and figures.

### 3. Review and refine

Request changes to specific chapters, explanation depth, example treatment, or layout. Existing documents support targeted updates without reorganizing everything.

For Word/PDF output, render and inspect formulas, figures, tables, and pagination when the environment supports it, checking content separately from appearance.

## Exam-review examples

These examples show organization and layout for the three modes:

| Example | What it demonstrates |
|---|---|
| [Knowledge organization](skills/course-exam-review/assets/examples/knowledge-outline.pdf) | Chapter hierarchy, conceptual explanations, formulas, and comparison tables |
| [Focused core-topic review](skills/course-exam-review/assets/examples/core-focus.pdf) | Hierarchical development of priorities and related knowledge grouped together |
| [Predicted questions and reference answers](skills/course-exam-review/assets/examples/questions-answers.pdf) | Chapter-grouped questions, reference answers, and procedural explanations |

The examples use introductory algorithm content. Actual materials follow your course, sources, and requirements; they are not limited to that subject, question count, or length.

## Environment and language

Use an agent environment that can load skill instructions, read your materials, and write files. Word/PDF generation, scanned documents, and external-reference research require the corresponding document, recognition, or web capabilities. See each skill's README for dependencies.

Executable instructions are in English; user guides are available in English and Simplified Chinese. **Deliverable language follows your requirements and course materials.** Course Notes defaults to a Chinese learning context.

## Feedback

Report issues or suggestions through [Issues](https://github.com/REDPOTATOPanda/course-study-skills/issues). Include the skill, environment, expected result, and a minimal reproduction or screenshot where possible.

## License

[MIT License](LICENSE). Courseware, textbooks, images, fonts, and other third-party materials retain their respective licensing requirements.
