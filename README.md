# html-brief

AI output you can read, decide on, and send back.

**html-brief** is an AI-human communication skill for turning long AI output into self-contained HTML briefs: plans, comparisons, reviews, reports, and small purpose-built editors with round-trip export.

## What this is NOT

This is not a frontend tool.

This is not a website generator.

This is not an app builder.

This is not a landing-page maker.

This is not a component library.

This is not a visual polish plugin.

This is not a dashboard template pack.

This is not a replacement for Markdown everywhere.

This is not a design system.

This is not a way to make every answer prettier.

This is not for production UI components.

This is not for short answers.

This is not for code-only output.

This is not for terminal logs.

This is not for marketing pages.

This is not for decorative HTML.

This is not an "AI output generator."

html-brief is for moments when Markdown becomes too flat: the user needs to understand structure, compare options, inspect a review, read a report, edit structured data, and then send the result back to an AI.

## Concept

A brief is a structured document designed for comprehension and decision-making. It does not have to be short. A 30-page migration plan can be a brief if the reader can understand the recommendation, inspect the risks, and act on it quickly.

html-brief uses HTML because HTML can combine text, hierarchy, tables, diagrams, forms, progressive disclosure, and copy/export actions in one browser-openable file. The goal is not to make AI output look like a website. The goal is to make AI output usable as an interface between human judgment and the next AI step.

## The three-stage Before / After

### 1. Before: long Markdown

A normal AI answer for a serious implementation plan often becomes a long Markdown file. It may be technically correct, but the reader must scroll, remember dependencies, compare tradeoffs mentally, and copy pieces by hand.

### 2. After: an HTML brief

The same plan becomes a single HTML file with a hero summary, semantic sections, an architecture diagram, a phased timeline, visible risks, validation gates, and progressive disclosure. The reader can scan the first screen, choose what to inspect, and understand what action is expected.

### 3. Round-trip: back to AI

The HTML brief is not the end. Copy as Prompt, Copy as JSON, Copy as Markdown, and Review-specific comment export turn the human's decisions or edits into structured input for the next AI session.

## Archetypes

| Archetype | Use it for | Output |
|---|---|---|
| Plan | RFCs, implementation plans, migrations, rollouts | Hero, architecture, phases, risks, validation |
| Compare | Options, tradeoffs, decisions | Recommendation, option cards, matrix, selected decision |
| Review | PRs, diffs, generated code, system changes | Change map, annotated findings, review comments |
| Report | Research, incidents, status, explainers | Executive summary, findings, evidence, actions |
| Editor | Feature flags, prompts, tickets, settings | Controls, validation, live preview, export/reset |

## Install

Clone the repository:

```bash
git clone https://github.com/<your-org>/html-brief.git
cd html-brief
```

Install for Claude Code:

```bash
mkdir -p ~/.claude/skills
ln -sf "$(pwd)/skills/html-brief" ~/.claude/skills/html-brief
```

Install for Codex CLI:

```bash
mkdir -p ~/.codex/skills
ln -sf "$(pwd)/skills/html-brief" ~/.codex/skills/html-brief
```

Install for Gemini CLI:

```bash
mkdir -p ~/.gemini/skills
ln -sf "$(pwd)/skills/html-brief" ~/.gemini/skills/html-brief
```

Install for Cursor in the current project:

```bash
mkdir -p .cursor/skills
ln -sf "$(pwd)/skills/html-brief" .cursor/skills/html-brief
```

## Quickstart

Single command to create the first output after installing for Claude Code:

```bash
claude "/html-brief Create an HTML implementation plan for a zero-downtime Postgres migration. Include architecture, phases, risks, validation gates, and Export Bridge."
```

For other agents, use the same natural-language instruction after installing the skill:

```text
/html-brief Create an HTML implementation plan for a zero-downtime Postgres migration. Include architecture, phases, risks, validation gates, and Export Bridge.
```

## For vibe coders

You do not need to know HTML.

Use html-brief when:
- Your AI answer is too long to read comfortably.
- You need to compare choices.
- You need a report that other people can actually read.
- You want to tune settings or flags and send the result back to AI.
- You want a visual plan instead of a wall of Markdown.

Say:
- "Make this an HTML brief."
- "Compare these options visually."
- "Turn this plan into html-brief."
- "Create an editor for these feature flags."
- "Review this PR as an HTML brief."

The skill chooses the right archetype and generates a browser-openable HTML file.

## Examples

- `skills/html-brief/examples/plan-db-migration/output.html`
- `skills/html-brief/examples/review-streaming-pr/output.html`
- `skills/html-brief/examples/edit-feature-flags/output.html`

Each example is a self-contained file with inline CSS and vanilla JS. Open it directly in a browser.

## Manual-only mode

By default, the skill can be automatically selected when the request matches the description. To require manual invocation only, add this field to `skills/html-brief/SKILL.md` frontmatter:

```yaml
disable-model-invocation: true
```

Then invoke with:

```text
/html-brief <your request>
```

## Validation

Run:

```bash
python3 scripts/validate.py
```

This checks:
- JSON schema files parse as JSON.
- `SKILL.md` body word count is within the expected range.
- Example HTML files are self-contained.
- Examples include Export Bridge state and copy buttons.

## License

MIT.

