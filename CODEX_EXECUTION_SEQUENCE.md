# Codex Execution Sequence

This file is the exact implementation order for Codex CLI. It starts at an empty directory and ends with a v1.0.0 git tag. Do not ask for human confirmation between files unless a command fails.

## Phase 0 窶・Repository scaffold

```bash
mkdir -p html-brief/{skills/html-brief/{references,schemas,examples/{plan-db-migration,review-streaming-pr,edit-feature-flags}},docs/adr,scripts,.github/workflows}
cd html-brief
git init
printf "node_modules/\n.DS_Store\n*.log\n" > .gitignore
```

Validation:

```bash
test -d skills/html-brief/references && test -d skills/html-brief/schemas && test -d skills/html-brief/examples
```

## Phase 1 窶・Core skill and references

Create files in this order:

1. `skills/html-brief/SKILL.md`
   - Exact content spec: YAML frontmatter, precise description, MIT license, full Artifact Constitution verbatim, archetype routing table, universal output rules, quality gate, ON/OFF instructions for `disable-model-invocation`.
   - Validation: `python3 scripts/validate.py` after `scripts/validate.py` exists; before that run `wc -w skills/html-brief/SKILL.md`.

2. `skills/html-brief/references/archetype-plan.md`
   - Exact content spec: Constitution mapping, HTML structure, CSS patterns, JS patterns, anti-patterns, Export Bridge behavior.
   - Validation: `grep -q "Exact HTML structure" skills/html-brief/references/archetype-plan.md`.

3. `skills/html-brief/references/archetype-compare.md`
   - Exact content spec: Decision-oriented structure with recommendation, option cards, matrix, selection export.
   - Validation: `grep -q "Tradeoff matrix" skills/html-brief/references/archetype-compare.md`.

4. `skills/html-brief/references/archetype-review.md`
   - Exact content spec: PR review layout, severity findings, annotated diff, Review Comments export.
   - Validation: `grep -q "Copy as Review Comments" skills/html-brief/references/archetype-review.md`.

5. `skills/html-brief/references/archetype-report.md`
   - Exact content spec: Executive summary, findings, evidence labels, actions, sources.
   - Validation: `grep -q "Executive Summary" skills/html-brief/references/archetype-report.md`.

6. `skills/html-brief/references/archetype-editor.md`
   - Exact content spec: editor layout, live preview, validation, sticky export bar, reset.
   - Validation: `grep -q "resetEditor" skills/html-brief/references/archetype-editor.md`.

7. `skills/html-brief/references/export-bridge.md`
   - Exact content spec: Copy as Prompt formats for all archetypes, Copy as JSON validation, Markdown conversion, Review Comments format, vanilla JS pattern.
   - Validation: `grep -q "vanilla JavaScript implementation pattern" skills/html-brief/references/export-bridge.md`.

8. `skills/html-brief/references/gotchas.md`
   - Exact content spec: default-AI aesthetic list, structure anti-patterns per archetype, round-trip anti-patterns, one acceptable security note.
   - Validation: `grep -q "The one acceptable security note" skills/html-brief/references/gotchas.md`.

9. `skills/html-brief/references/design-tokens.md`
   - Exact content spec: CSS variables, dark mode, print style, semantic color rules.
   - Validation: `grep -q "Semantic color rules" skills/html-brief/references/design-tokens.md`.

Commit:

```bash
git add skills/html-brief/SKILL.md skills/html-brief/references
git commit -m "Add core html-brief skill references"
```

## Phase 2 窶・JSON Schemas

Create files in this order:

10. `skills/html-brief/schemas/brief.schema.json`
    - Exact content spec: common envelope; `$schema`; `$id`; required version, archetype, createdAt, userIntent, state, initialState; descriptions on every property.
    - Validation: `python3 -m json.tool skills/html-brief/schemas/brief.schema.json >/dev/null`.

11. `skills/html-brief/schemas/plan.schema.json`
    - Exact content spec: complete Plan envelope with Plan state constraints.
    - Validation: `python3 -m json.tool skills/html-brief/schemas/plan.schema.json >/dev/null`.

12. `skills/html-brief/schemas/compare.schema.json`
    - Exact content spec: options, criteria, matrix, selected option.
    - Validation: `python3 -m json.tool skills/html-brief/schemas/compare.schema.json >/dev/null`.

13. `skills/html-brief/schemas/review.schema.json`
    - Exact content spec: verdict, findings, files, test coverage.
    - Validation: `python3 -m json.tool skills/html-brief/schemas/review.schema.json >/dev/null`.

14. `skills/html-brief/schemas/report.schema.json`
    - Exact content spec: report type, summary, metrics, findings, actions, sources.
    - Validation: `python3 -m json.tool skills/html-brief/schemas/report.schema.json >/dev/null`.

15. `skills/html-brief/schemas/editor.schema.json`
    - Exact content spec: editor type, items, changed keys, validation, initial state.
    - Validation: `python3 -m json.tool skills/html-brief/schemas/editor.schema.json >/dev/null`.

Commit:

```bash
git add skills/html-brief/schemas
git commit -m "Add html-brief JSON schemas"
```

## Phase 3 窶・Examples

Create files in this order:

16. `skills/html-brief/examples/plan-db-migration/before.md`
17. `skills/html-brief/examples/plan-db-migration/output.html`
18. `skills/html-brief/examples/plan-db-migration/round-trip.json`
    - Exact content spec: zero-downtime Postgres migration Plan; all seven articles; self-contained; Copy as Prompt/JSON/Markdown.
    - Validation: `python3 -m json.tool skills/html-brief/examples/plan-db-migration/round-trip.json >/dev/null && grep -q "navigator.clipboard" skills/html-brief/examples/plan-db-migration/output.html`.

19. `skills/html-brief/examples/review-streaming-pr/before.md`
20. `skills/html-brief/examples/review-streaming-pr/output.html`
21. `skills/html-brief/examples/review-streaming-pr/round-trip.json`
    - Exact content spec: streaming/backpressure PR review; severity findings; Copy as Review Comments.
    - Validation: `python3 -m json.tool skills/html-brief/examples/review-streaming-pr/round-trip.json >/dev/null && grep -q "Copy as Review Comments" skills/html-brief/examples/review-streaming-pr/output.html`.

22. `skills/html-brief/examples/edit-feature-flags/before.md`
23. `skills/html-brief/examples/edit-feature-flags/output.html`
24. `skills/html-brief/examples/edit-feature-flags/round-trip.json`
    - Exact content spec: feature flag editor; dependencies; warnings; live preview; reset; full round-trip export.
    - Validation: `python3 -m json.tool skills/html-brief/examples/edit-feature-flags/round-trip.json >/dev/null && grep -q "brief-initial-state" skills/html-brief/examples/edit-feature-flags/output.html`.

Commit:

```bash
git add skills/html-brief/examples
git commit -m "Add phase 2 html-brief examples"
```

## Phase 4 窶・Repository docs and validation

Create files in this order:

25. `README.md`
    - Exact content spec: tagline; concept; "What this is NOT" in first 30 lines; before/after; install snippets; quickstart; vibe-coder onboarding; no competitor comparisons.
    - Validation: `grep -n "What this is NOT" README.md && grep -q "For vibe coders" README.md`.

26. `AGENTS.md`
    - Exact content spec: repository navigation and install pointer.
    - Validation: `test -s AGENTS.md`.

27. `CONTRIBUTING.md`
    - Exact content spec: contribution principles and example checklist.
    - Validation: `test -s CONTRIBUTING.md`.

28. `CHANGELOG.md`
    - Exact content spec: v1.0.0 entry.
    - Validation: `grep -q "1.0.0" CHANGELOG.md`.

29. `LICENSE`
    - Exact content spec: MIT License text.
    - Validation: `grep -q "MIT License" LICENSE`.

30. `scripts/validate.py`
    - Exact content spec: standard-library validation for JSON syntax, SKILL word count, self-contained examples, Export Bridge checks.
    - Validation: `python3 scripts/validate.py`.

Commit:

```bash
git add README.md AGENTS.md CONTRIBUTING.md CHANGELOG.md LICENSE scripts/validate.py .gitignore
python3 scripts/validate.py
git commit -m "Add repository docs and validation"
```

## Phase 5 窶・Final release gate

Run all validation:

```bash
python3 scripts/validate.py
find skills/html-brief -type f | sort
git status --short
```

Expected:
- Validation passes.
- `git status --short` is empty.

Tag:

```bash
git tag -a v1.0.0 -m "html-brief v1.0.0"
```

Optional archive:

```bash
git archive --format=zip --output html-brief-v1.0.0.zip v1.0.0
```

