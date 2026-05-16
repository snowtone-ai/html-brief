# repo-map.md -- pm-zero v9.4 Repository Map

## Read Policy
- Session start: read Summary only.
- Before editing: read the section for the target area when target files are unclear.
- When navigation is unclear: read Entry Points and Directory Map.
- After structural changes: update only the affected section.

## Summary
- App type: AI agent skill repository.
- Main runtime: Markdown, JSON Schema, self-contained HTML, Python validation.
- Package manager: none.
- Primary source directory: skills/html-brief/.
- Primary test/validation entry: scripts/validate.py.
- Main entry points: skills/html-brief/SKILL.md, README.md.
- Verification command: node scripts/verify.mjs.

## Directory Map
| Path | Purpose | Edit Frequency | Notes |
|---|---|---|---|
| skills/html-brief/ | Skill implementation | high | Product source of truth. |
| skills/html-brief/references/ | Archetype and protocol references | high | Keep aligned with schemas and examples. |
| skills/html-brief/schemas/ | JSON Schema contracts | high | Draft 2020-12. |
| skills/html-brief/examples/ | Self-contained example briefs | medium | No external assets or CDNs. |
| docs/ | pm-zero project memory | medium | Vision, state, decisions, issues, repo map. |
| scripts/ | Validation and pm-zero helpers | medium | validate.py is product validation. |

## Entry Points
| Area | File | Purpose |
|---|---|---|
| Skill | skills/html-brief/SKILL.md | Main behavior and triggers. |
| Validation | scripts/validate.py | Required validation contract. |
| Public docs | README.md | User onboarding. |

## Common Workflows
| Workflow | Read First | Edit Usually | Verify |
|---|---|---|---|
| Archetype change | AGENTS.md, relevant reference | references/, schemas/, examples/ | python scripts/validate.py |
| Export protocol | references/export-bridge.md | references/, schemas/, examples/ | python scripts/validate.py |
| pm-zero docs | AGENTS.md | tasks.md, docs/, scripts/ | git diff --check |

## Generated / External Files
| Path | Rule |
|---|---|
| __pycache__/, .pytest_cache/ | Ignore. |
| *.tmp, *.log | Ignore. |
| .env, .env.* | Ignore secrets. |

## Update Rules
- Keep Summary under 20 lines.
- Keep each directory note concrete.
- Move rationale to docs/decisions.md.
