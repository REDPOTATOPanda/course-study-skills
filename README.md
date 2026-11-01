# Course Study Skills

[English](README.md) | [简体中文](README.zh-CN.md)

Agent skills for everyday course notes, coherent textbook-style handouts, and exam review. Build maintainable notes, systematic explanations, or focused review materials from actual courseware, class notes, and course requirements.

**[Latest release](https://github.com/REDPOTATOPanda/course-study-skills/raw/refs/heads/main/downloads/course-study-skills.zip)** · **[All releases](https://github.com/REDPOTATOPanda/course-study-skills/releases)**

## Choose a skill

| Skill | Suitable use | Goal | Output |
|---|---|---|---|
| [course-notes](skills/course-notes/README.md) | Everyday learning and chapter updates | Preserve the teaching sequence, knowledge, and original figures | Markdown only by default; Typora-oriented |
| [course-textbook-builder](skills/course-textbook-builder/README.md) | No suitable textbook, or teaching differs from it | Compile scattered materials into a coherent, independently readable handout | Word, PDF, or Markdown as requested |
| [course-exam-review](skills/course-exam-review/README.md) | Review based on actual scope, priorities, and exam requirements | Organize knowledge, focus priorities, or create predicted questions and reference answers | Word, PDF, or Markdown as requested |

Skills work independently or together; there is no required sequence.

### Everyday notes

Organize chapters, supplement notes, or edit specified passages. Retain course order, hierarchy, definitions, conditions, formulas, algorithms, and useful figures while consolidating repetition. Default examples preserve original questions and existing answers, preferably as readable screenshots. Editable treatment or extra explanation requires the corresponding request. New explanatory examples require a user request or agreement. Do not automatically create course-exercise or teacher-review modules.

Course-level preferences, extraction caches, and a read-only Markdown checker support continuing updates. No unsolicited PDF preview is generated.

### Textbook-style handouts

Rebuild knowledge relationships from scattered course materials. Explain concepts, principles, methods, applicability, and necessary derivations in connected prose. Unify covers, contents, headings, formulas, figures, tables, and pagination for learning and long-term reference.

Default modern textbook styling includes restrained color, professional math, a separate cover and contents, new-page chapter starts, and continuous sections. This is not the default appearance of the other two skills.

### Exam-review materials

Select one or more modes:

- **Knowledge organization:** Chapter-based structure with knowledge needed for understanding and application.
- **Focused core-topic review:** Explain explicit priorities with meaningful hierarchy and connected concepts/methods.
- **Predicted questions and reference answers:** Use actual exam constraints for short-answer, calculation, multiple-choice, fill-in, and other question types.

Ask about modes before work if unspecified. Do not invent question types, counts, marks, or another course's exam structure. Three fixed samples, editable sources, shared styles, and an optional PDF renderer support consistent compact black-and-white output. Upper-right headers do not show question ranges. Ask before compact two-column layout.

## Download and install

Current packages are maintained in [downloads/](downloads/README.md) and match this repository snapshot. Releases retain previously published historical versions.


Get [current download packages](https://github.com/REDPOTATOPanda/course-study-skills/raw/refs/heads/main/downloads/course-study-skills.zip):

| Archive | Contents |
|---|---|
| [course-notes.zip](https://github.com/REDPOTATOPanda/course-study-skills/raw/refs/heads/main/downloads/course-notes.zip) | Course notes skill |
| [course-textbook-builder.zip](https://github.com/REDPOTATOPanda/course-study-skills/raw/refs/heads/main/downloads/course-textbook-builder.zip) | Textbook-style handout skill |
| [course-exam-review.zip](https://github.com/REDPOTATOPanda/course-study-skills/raw/refs/heads/main/downloads/course-exam-review.zip) | Exam-review skill |
| [course-study-skills.zip](https://github.com/REDPOTATOPanda/course-study-skills/raw/refs/heads/main/downloads/course-study-skills.zip) | All three skills |

Install complete skill folders using the host's supported directory or import mechanism. Single-skill archives contain a same-named folder; the collection keeps all three under `skills/`.

Alternatively, download repository source or clone:

```bash
git clone https://github.com/REDPOTATOPanda/course-study-skills.git
```

Skill roots are `skills/course-notes`, `skills/course-textbook-builder`, and `skills/course-exam-review`. If your host supports GitHub subdirectory installation, use those paths. Preserve `SKILL.md` and all referenced resources and relative paths. Copying only the README or entrypoint may omit required resources. Installation paths, invocation syntax, and discovery depend on the host.

## Usage examples

> Use course-notes for this chapter. Preserve the teaching sequence, all knowledge, and useful original figures. Keep original questions and existing answers as readable screenshots.

> Use course-textbook-builder to compile these slides and class notes into a systematic handout with necessary principles and examples. Deliver Word and PDF. Ask about substantive ambiguities.

> Use course-exam-review for this course. First ask which modes I need, allowing multiple selections, and confirm scope, question types, and delivery requirements.

> Use course-notes to add only the attachment's new material to existing notes, preserving unrelated content, annotations, and images.

## Design principles

**Actual teaching is primary.** Preserve notation, assumptions, and applicability from courseware, notes, and explicit teacher requirements. External supplements must be accurate and moderate, not presented as taught content.

**Retain understanding and application.** Remove repetition, not definitions, principles, conditions, formulas, necessary reasoning, or relevant source examples. Avoid conclusion-only lists.

**Confirm important ambiguities.** Ask about source gaps/conflicts and requirements affecting scope or output. Reuse already confirmed instructions without repeated questions.

**Professional, coherent presentation.** Explain knowledge directly without repetitive source tags or process commentary. Use paragraphs for concepts, numbering for ordered steps, suitable comparison tables, and selective bolding.

**Distinct purposes and styles.** Notes prioritize editability and continuing use; textbook handouts prioritize structure and systematic explanation; review materials balance reading, lookup, and printing. User templates and instructions take priority. Two-column printing is optional and must be selected.

## Efficiency and quality

Read only relevant chapters, passages, and detailed references. Cache extraction with source-content and parsing-setting checks; process affected parts for local updates while checking dependencies and pagination. Select parsers by input type and revisit original pages for unreliable recognition, formulas, and complex figures/tables.

All three skills include gap classification, conditional coverage checks against existing questions, computational verification, concrete acceptance checks, and optional subagents. These internal measures do not expand scope, authorize new exercises, or change output defaults. The main agent remains responsible for integration and verification.

The notes checker runs with Python 3 and checks common image references, heading jumps, fences, and placeholders. Mechanical checks do not prove semantic correctness. Source parsing, static review, content verification, and actual rendering are distinct; report only checks actually performed.

## Languages and environment

Executable instructions and references are maintained in English; each README has English and Simplified Chinese versions. Instruction language does not dictate deliverable language. Follow user language requirements and course materials; course-notes retains its Chinese-note default unless another language is requested. Chinese fixed review samples remain unchanged as visual references.

The collection does not bundle models, OCR services, fonts, or typesetting engines. Required capabilities depend on the task:

| Work | Capability |
|---|---|
| Read slides/documents | Relevant format parsers |
| Scans or complex figures | OCR, visual reading, or page rendering |
| Textbook/reference research | Web search |
| Word/PDF generation | Document generation, math layout, and export |
| Final visual inspection | Rendering/preview |
| Notes checker | Python 3 |

The optional review renderer uses Python/reportlab/svglib and Node/mathjax-full 3.x for mathematical blocks. Equivalent tools may implement the same style. MarkItDown can support extraction but does not replace checks. Complete cross-host workflows and English/Chinese behavioral equivalence are not universally verified.

## Repository structure

```text
.
├── README.md
├── README.zh-CN.md
├── LICENSE
├── downloads/
└── skills/
    ├── course-notes/
    │   ├── SKILL.md
    │   ├── README.md
    │   ├── README.zh-CN.md
    │   ├── agents/
    │   ├── references/
    │   └── scripts/
    ├── course-textbook-builder/
    │   ├── SKILL.md
    │   ├── README.md
    │   ├── README.zh-CN.md
    │   └── references/
    └── course-exam-review/
        ├── SKILL.md
        ├── README.md
        ├── README.zh-CN.md
        ├── references/
        ├── assets/
        └── scripts/
```

READMEs serve users; `SKILL.md` is the executable entrypoint. References disclose detailed rules as needed; scripts support repeatable checks or rendering; assets contain samples and templates; agents metadata is host-specific. Resources remain within their skill so each installs independently.

## Feedback and license

Use [Issues](https://github.com/REDPOTATOPanda/course-study-skills/issues) for organization, parsing, math, layout, or compatibility feedback. Include the skill, environment, expected/actual behavior, and a minimal reproduction or screenshot. Remove unnecessary personal information and share only materials you may distribute. Distinguish general rules from course-specific requests.

[MIT License](LICENSE). Courseware, textbooks, fonts, images, and other third-party resources retain their respective licensing requirements.
