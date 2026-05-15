---
name: html-brief
description: |
  Transform long AI output into structured, readable, decision-ready, round-trippable HTML briefs. Use for RFCs, implementation plans, PR reviews, code reviews, reports, comparisons, editors, dashboard-style briefs, "make it visual", "HTML brief", or any answer where spatial structure, diagrams, progressive disclosure, or human decisions should be exported back to AI. Supports engineers, PMs, and non-engineers. Do not use for short conversational replies, code-only outputs, normal terminal logs, ordinary frontend app/site/UI design, landing pages, or production UI components.
license: MIT
---

# html-brief

html-brief is an AI-human communication skill. It turns long or complex AI output into a self-contained HTML brief that a person can read, evaluate, operate, and send back to an AI. The output is an information artifact, not a product interface. It exists when Markdown becomes too flat for the job: plans need timelines and risk tables, comparisons need visible tradeoffs, reviews need findings grouped by severity, reports need evidence and conclusions, and editors need a round-trip state model.

Use this skill when the user asks for an RFC, implementation plan, migration plan, PR review, code review, research report, incident report, comparison, decision brief, structured editor, dashboard-style brief, visual summary, or explicit HTML brief. Also use it when the answer would exceed about 100 lines of Markdown and the reader would benefit from hierarchy, diagrams, progressive disclosure, semantic color, or export buttons.

Do not use this skill for short conversational replies, code-only answers, plain command output, logs, simple lists, or cases where Markdown is already the most efficient format. Do not treat it as a frontend design skill. If the user asks for a real app, website, landing page, dashboard product, or component library, build that directly instead of wrapping it as html-brief. If the user asks for decorative HTML, refuse the decoration-first framing and produce a brief only when there is real information architecture to express.

## Artifact Constitution

The Constitution has priority over templates, examples, and local taste. Every artifact must satisfy these seven articles.

### 1. The Reader's Time Is Sacred

A brief must earn attention immediately. The first screen should state the purpose, the conclusion or recommended action, and the shape of the document. A reader should know within five seconds why the artifact exists and within thirty seconds where to look next. Use a hero summary, compact metadata, navigation for three or more sections, and progressive disclosure for detail. Long blocks belong in tables, diagrams, lists, or details elements. Do not bury the decision behind background prose.

### 2. Form Follows Information

Visual form must encode meaning. Size should indicate importance. Proximity should indicate relationship. Color should indicate status, risk, confidence, or ownership. Typography should distinguish headings, labels, evidence, and code. Diagrams should clarify flows, dependencies, timelines, or scope boundaries. Avoid purple gradients, glassmorphism, decorative emoji headings, meaningless icons, and equal-weight card grids. If a visual element does not improve comprehension, remove it.

### 3. Communication Is a Loop

The artifact is not the end of the conversation. Interactive briefs must preserve a machine-readable state and export the human's decisions or edits back to AI. The minimum export bridge for interactive artifacts is Copy as Prompt, Copy as JSON, and Copy as Markdown. Review artifacts must also include Copy as Review Comments. Editor artifacts must preserve initialState, compute current state from the DOM, show changed fields, and include Reset.

### 4. Universality

Every example artifact must be a single HTML file that opens directly in a browser. Use inline CSS, inline vanilla JavaScript, and embedded JSON state. Do not use external fonts, images, CSS, scripts, CDNs, frameworks, or build output. The layout must work at 380px width, support dark mode with prefers-color-scheme, and include print rules. The file should remain useful when copied, archived, emailed, or opened offline.

### 5. Honesty Over Impression

A brief must be accurate before it is impressive. Summaries should contain conclusions, not topic labels. Risks, unknowns, assumptions, and confidence should be visible. Do not hide weak evidence behind confident styling. Do not use colors that imply certainty when the source is uncertain. Do not invent metrics, sources, or validation. If data is missing, say so and make the consequence clear.

### 6. Adaptability Within Principles

Archetypes are guides, not cages. Choose the closest archetype, then adapt the structure to the user's real task while preserving the Constitution. Remove sections that do not help. Add sections when the information requires them. If a request mixes archetypes, choose a primary one and borrow supporting regions from another. Do not force every artifact into the same card layout.

### 7. Restraint

The artifact should feel designed, but it should not feel decorated. Use a small token set, limited accents, and purposeful spacing. Prefer fewer, stronger visual decisions over many weak flourishes. Keep JavaScript small and understandable. Do not add animations unless they communicate state changes. Do not create security gates, login flows, telemetry, or infrastructure that the brief does not need.

## Archetype Routing

| User need | Archetype | Use when | Required reference |
| --- | --- | --- | --- |
| Sequence of work | Plan | The user needs a path, phases, risks, rollback, or implementation order. | eferences/archetype-plan.md |
| Decision between options | Compare | The user needs a recommendation, tradeoff matrix, scoring, or selected option export. | eferences/archetype-compare.md |
| Code or PR judgment | Review | The user needs findings, severity, file-by-file notes, tests, and review comments. | eferences/archetype-review.md |
| Evidence and conclusions | Report | The user needs analysis, methodology, findings, actions, and sources. | eferences/archetype-report.md |
| Human edits to structured state | Editor | The user needs toggles, fields, validation warnings, changed count, and reset/export. | eferences/archetype-editor.md |

When the user explicitly names an archetype, follow it unless it conflicts with the task. When the task is ambiguous, infer the archetype from the action the reader must take. If the reader must choose, use Compare. If the reader must execute, use Plan. If the reader must approve code, use Review. If the reader must understand evidence, use Report. If the reader must modify values, use Editor.

## Reference Loading Rules

Load only the references needed for the chosen artifact. Always load eferences/export-bridge.md for interactive artifacts, Review, and Editor. Load eferences/design-tokens.md when creating or modifying visual examples. Load eferences/gotchas.md when quality-checking or when the output risks looking like generic AI HTML. Load the relevant schema before changing round-trip JSON. Do not redefine protocol details in README or examples when the references already own them.

## Universal Output Rules

Every HTML brief should include semantic landmarks, a meaningful title, a hero with conclusion or decision context, clear section headings, and an export region when round-trip behavior is expected. Prefer native HTML controls, details elements, tables, and SVG diagrams over framework-like abstractions. Use CSS custom properties for semantic tokens: background, surface, text, muted text, border, accent, success, warning, danger, and neutral.

Each artifact with state must embed JSON in a script tag such as rief-initial-state or rief-state. Copy as JSON must serialize the envelope or current state clearly. Copy as Prompt must produce instructions that another AI session can act on without reading the page. Copy as Markdown must produce a readable text version. Clipboard behavior must include a fallback for browsers that block 
avigator.clipboard on local files. Toasts should confirm the copied format without interrupting reading.

HTML examples must remain self-contained. Inline CSS and JavaScript are acceptable because the brief is a portable artifact. External dependencies are not acceptable. Do not include http://, https://, CDN links, external font imports, module imports, or build-generated class noise in examples.

## Quality Gate

Before finalizing an artifact, check: the first screen explains the point; the structure matches the reader action; important sections are not equal weight; risks or uncertainty are visible; color has semantic meaning; the export bridge works for every required format; JSON state is valid; the artifact opens as a single file; mobile, dark mode, and print rules exist; no external dependencies are present; and no decorative element competes with comprehension.

For Review, ensure Copy as Review Comments exports concise PR-ready comments grouped by severity. For Editor, ensure Reset restores the embedded initial state exactly and that the changed count is derived from current controls. For Compare, ensure the recommendation is visible before the matrix. For Plan, ensure rollback and validation are not afterthoughts. For Report, ensure the executive summary states conclusions rather than merely describing the topic.

## Invocation Controls

To turn the skill off for a request, the user may say disable-model-invocation: true, do not use html-brief, or plain Markdown only. Respect that unless a higher-priority instruction requires an HTML artifact. To request the skill manually, the user may say use html-brief, make an HTML brief, make this visual, 	urn this into a round-trip brief, or name one of the archetypes.

If automatic invocation is uncertain, use the manual fallback: ask whether the user wants a normal answer or an html-brief only when producing the wrong form would be costly. Otherwise make a reasonable choice. The default bias is practical: use html-brief when the user must read, decide, review, compare, or edit; skip it when the user just needs a short answer or code.
