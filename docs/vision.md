# vision.md -- Product North Star

## Purpose
html-brief is a reusable AI agent skill that turns long AI output into structured,
readable, decision-ready, round-trippable HTML briefs.

## Target Users
- AI tool users who need to read, decide, and send structured decisions back to an agent.
- Agent authors who need a stable HTML artifact protocol.

## Success Criteria
- Examples are self-contained single HTML files.
- Exported state can be copied back to AI without losing user decisions.
- Validation catches broken schemas, missing files, and example regressions.

## Non-goals
- This is not a frontend framework, website generator, or design polish plugin.
- Do not add a dependency stack unless correctness requires it.

## Relationship to tasks.md
- This file defines product intent.
- tasks.md defines implementation tasks.
- Store task progress and evidence in tasks.md.
- Store only the current pointer in docs/state.md.
