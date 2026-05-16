# Project AGENTS.md -- pm-zero v9.4

## Language
- Completion reports, error reports, and manual confirmation requests: Japanese.
- Code identifiers and command names: English.
- When 3+ HIGH assumptions accumulate, ask immediately.

## Source of Truth
- Product intent: docs/vision.md
- Execution tasks: tasks.md
- Current state: docs/state.md
- Decisions: docs/decisions.md
- Failures: docs/issues.md
- Repository map: docs/repo-map.md
- Report: HANDOFF-JA.md

When product files disagree, use this product order:

1. skills/html-brief/SKILL.md
2. skills/html-brief/references/export-bridge.md
3. skills/html-brief/references/archetype-*.md
4. skills/html-brief/schemas/*.schema.json
5. skills/html-brief/examples/*/output.html
6. README.md

Artifact Constitution > Archetype reference > Export Bridge > Schemas > Examples > README.

## Startup Read
- Read this file.
- Read docs/state.md.
- Read docs/decisions.md.
- Read docs/repo-map.md Summary.

## Repository Navigation
- Read detailed repo-map sections only when target files are unclear.
- Update docs/repo-map.md after structural changes.
- Use rg before broad manual browsing.

## Task Ledger Rule
- Planning output goes to tasks.md.
- Implementation starts from tasks marked ready.
- Each ready task includes owner, dependencies, write scope, acceptance, verification, and evidence.
- Coordinator updates tasks.md.
- Worker agents report results to the coordinator.

## Scope Lock Rule
- One coordinator owns tasks.md and docs/state.md.
- Workers edit only their assigned write scope.
- Parallel work requires disjoint Write Scopes or isolated worktrees.
- Tasks touching the same file are serialized.

## Product Rules
- Keep the repository small and obvious.
- Preserve single-file artifact universality: examples must work when opened directly in a browser.
- Protect the Export Bridge and exported decision shape.
- Treat schemas as contracts.
- Make visual design carry information.
- Optimize for readers, not screenshots.

## Commands
- validate: python scripts/validate.py
- verify: node scripts/verify.mjs
- setup: node scripts/setup.mjs

Use only commands that exist in this repository.

## Execution Boundaries
- Use PowerShell.
- Use standard push with branch tracking.
- Keep safe values only in output.
- Do not add framework, bundler, package manager setup, or external dependency unless correctness requires it.
- Product code changes require an explicit task in tasks.md.
