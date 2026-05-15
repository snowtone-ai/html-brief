# AGENTS.md — html-brief Repository Instructions

## Purpose

This repository ships `html-brief`: a reusable AI agent skill that turns long AI output into structured, readable, decision-ready, round-trippable HTML briefs.

This is an AI-human communication protocol, not a frontend UI framework.

## Environment

- Primary shell: PowerShell on Windows.
- Repository path: `C:\Users\chidj\project\html-brief`.
- GitHub remote: `https://github.com/snowtone-ai/html-brief`.
- Use Windows paths and PowerShell syntax.
- Run safe file, git, validation, and local browser-open operations autonomously.

## Source of Truth

When files disagree, use this order:

1. `skills/html-brief/SKILL.md`
2. `skills/html-brief/references/export-bridge.md`
3. `skills/html-brief/references/archetype-*.md`
4. `skills/html-brief/schemas/*.schema.json`
5. `skills/html-brief/examples/*/output.html`
6. `README.md`

The product rule is:

```text
Artifact Constitution > Archetype reference > Export Bridge > Schemas > Examples > README
```

## Project Constitution

Apply these engineering rules in every change.

### 1. Keep the repository small and obvious

Use plain Markdown, JSON Schema, Python standard library validation, and self-contained HTML examples. Add no framework, bundler, package manager setup, or external dependency unless the repository cannot remain correct without it.

### 2. Preserve single-file artifact universality

Every example HTML file must work when opened directly in a browser. Use inline CSS, inline vanilla JavaScript, embedded JSON state, and no external CSS, fonts, images, scripts, or CDNs.

### 3. Protect the Export Bridge

Interactive artifacts must export human decisions back to AI. Do not change example state shape, copy buttons, or export logic without checking `references/export-bridge.md` and the relevant schema.

### 4. Treat schemas as contracts

All `schemas/*.schema.json` files use JSON Schema draft 2020-12. Every property must include a type and description. Keep examples and schemas aligned.

### 5. Make visual design carry information

Use semantic color, hierarchy, spacing, and typography to encode meaning. Avoid default AI aesthetics: purple gradients, glassmorphism, decorative emoji headings, meaningless icons, equal-weight card grids, and generic rounded-card clutter.

### 6. Optimize for readers, not screenshots

A brief succeeds when a reader can understand the point, make a decision, and send the result back to AI. Do not add decoration that does not improve comprehension.

### 7. Verify before completion

Run validation before claiming completion:

```powershell
python scripts\validate.py
```

If `python` is unavailable, try:

```powershell
py scripts\validate.py
```

Report only commands actually run.

## File Responsibilities

- `skills/html-brief/SKILL.md`
  - Main skill behavior, trigger description, Artifact Constitution, routing, quality gate, invocation controls.

- `skills/html-brief/references/archetype-*.md`
  - Exact structures and rules for Plan, Compare, Review, Report, and Editor.

- `skills/html-brief/references/export-bridge.md`
  - Canonical round-trip protocol and vanilla JS patterns.

- `skills/html-brief/references/gotchas.md`
  - Anti-pattern library.

- `skills/html-brief/references/design-tokens.md`
  - Shared CSS token guidance.

- `skills/html-brief/schemas/*.schema.json`
  - JSON contracts for exported state.

- `skills/html-brief/examples/*/output.html`
  - Self-contained reference examples proving the skill.

- `scripts/validate.py`
  - Required validation entry point.

- `README.md`
  - Public explanation and onboarding. It must not redefine the skill.

## Required Validation Scope

Before commit or push, check:

- Required files exist.
- JSON schemas parse.
- Example JSON files parse.
- `SKILL.md` body word count is 1500–2000 words.
- The seven Constitution article titles are present.
- Example HTML files contain inline CSS, inline JS, and Export Bridge buttons.
- Review example contains Copy as Review Comments.
- Editor example contains Reset.
- LICENSE is MIT.
- README clearly states what this is not near the top.

## Git Workflow

Use standard git operations.

```powershell
git status --short
git diff --stat
git add .
git commit -m "Initial html-brief v1.0"
git push -u origin main
git tag -a v1.0.0 -m "html-brief v1.0.0"
git push origin v1.0.0
```

Use a different commit message only when it is more accurate.

## Completion Report

Final responses to the user must be in Japanese and concise. Include:

- What changed
- Major changed files
- Validation commands and results
- Commit hash
- Pushed branch
- Pushed tag
- Remaining risks

Do not paste large logs, full diffs, or full file contents in the final response.
