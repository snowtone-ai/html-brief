# Repository Structure

This file explains the purpose of each top-level directory and important file so Codex CLI can navigate the repository without guessing.

## Top Level

- `README.md`
  - Public-facing introduction, concept, install instructions, quickstart, and onboarding.
  - Keep this focused on what html-brief is, what it is not, and how to use it.

- `LICENSE`
  - MIT License.
  - Do not add implementation notes here.

- `AGENTS.md`
  - Short repository guidance for AI agents.
  - Points agents to `skills/html-brief/SKILL.md` as the source of behavior.

- `CONTRIBUTING.md`
  - Contribution rules and expectations.
  - Use this for repo maintenance conventions, not skill behavior.

- `CHANGELOG.md`
  - Release history.
  - Update when cutting a new version.

- `CODEX_EXECUTION_SEQUENCE.md`
  - Step-by-step implementation and validation order for Codex CLI.
  - Use this when rebuilding the repository from scratch or checking completeness.

## `skills/html-brief/`

The actual installable skill directory.

- `skills/html-brief/SKILL.md`
  - Main skill instruction file.
  - Contains frontmatter, activation description, Artifact Constitution, routing table, universal output rules, quality gate, and ON/OFF invocation instructions.
  - This is the primary source of truth for agent behavior.

## `skills/html-brief/references/`

Detailed reference documents loaded when a specific archetype or protocol is needed.

- `references/archetype-plan.md`
  - Structure, CSS, JS, anti-patterns, and Export Bridge rules for implementation plans, migration plans, roadmaps, and RFC-like briefs.

- `references/archetype-compare.md`
  - Structure, CSS, JS, anti-patterns, and Export Bridge rules for side-by-side option comparison and decision briefs.

- `references/archetype-review.md`
  - Structure, CSS, JS, anti-patterns, and Export Bridge rules for PR reviews, code explainers, diffs, findings, and review comments.

- `references/archetype-report.md`
  - Structure, CSS, JS, anti-patterns, and Export Bridge rules for research reports, incident reports, status reports, and executive summaries.

- `references/archetype-editor.md`
  - Structure, CSS, JS, anti-patterns, and Export Bridge rules for interactive editors such as feature flags, prioritization boards, prompt tuners, and structured config editors.

- `references/export-bridge.md`
  - Canonical protocol for Copy as Prompt, Copy as JSON, Copy as Markdown, Copy as Review Comments, and vanilla JavaScript clipboard behavior.
  - Use this before editing export logic in examples.

- `references/gotchas.md`
  - Anti-pattern library.
  - Includes default-AI aesthetic patterns to avoid, structure mistakes, round-trip mistakes, and the single acceptable sharing note.

- `references/design-tokens.md`
  - CSS variables and semantic styling rules.
  - Use this to keep examples visually consistent without turning the project into a frontend UI framework.

## `skills/html-brief/schemas/`

JSON Schema draft 2020-12 files for validating exported state.

- `schemas/brief.schema.json`
  - Common envelope used by every archetype.
  - Defines shared fields such as version, archetype, title, userIntent, createdAt, state, and initialState.

- `schemas/plan.schema.json`
  - State schema for Plan artifacts.

- `schemas/compare.schema.json`
  - State schema for Compare artifacts.

- `schemas/review.schema.json`
  - State schema for Review artifacts.

- `schemas/report.schema.json`
  - State schema for Report artifacts.

- `schemas/editor.schema.json`
  - State schema for Editor artifacts.

## `skills/html-brief/examples/`

Self-contained browser-openable HTML examples.

- `examples/plan-db-migration/output.html`
  - Zero-downtime Postgres migration plan.
  - Demonstrates Plan structure, risk honesty, SVG timeline/flow, and Export Bridge.

- `examples/review-streaming-pr/output.html`
  - Streaming/backpressure PR review.
  - Demonstrates Review structure, annotated diff, findings, test plan, and Copy as Review Comments.

- `examples/edit-feature-flags/output.html`
  - Interactive feature flag editor.
  - Demonstrates Editor structure, state changes, validation warnings, reset, and full round-trip export.

## `scripts/`

Repository validation and maintenance scripts.

- `scripts/validate.py`
  - Checks required files, validates JSON syntax, checks schema metadata, checks SKILL.md body word count, and verifies basic example requirements.
  - Run before committing.

## Recommended Validation Commands

```bash
python3 scripts/validate.py
git status --short
```

## Editing Rules for Codex CLI

1. Treat `skills/html-brief/SKILL.md` as the highest-priority behavior source.
2. Treat `references/export-bridge.md` as the source of truth for export behavior.
3. Treat `schemas/*.schema.json` as the source of truth for JSON output shape.
4. Keep examples self-contained: no external CSS, JavaScript, fonts, images, or CDNs.
5. Do not add competitor comparisons to README or docs.
6. Do not add security gates or advisory layers. Only keep the short sharing note in `gotchas.md`.
7. Do not add time estimates to roadmap or execution docs.
8. Run `python3 scripts/validate.py` before finalizing changes.
