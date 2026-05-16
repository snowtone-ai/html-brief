# Gotchas and Anti-pattern Library

This file is the negative specification for html-brief. It exists so an agent knows what not to generate.

## Default-AI aesthetic list: avoid these patterns

Avoid the generic AI artifact look:

- Indigo, violet, or purple gradient backgrounds.
- Glass morphism cards using `backdrop-filter`, semi-transparent surfaces, and glow.
- A full-screen centered hero that delays the actual answer.
- Identical rounded cards in a grid when the content has different importance.
- Decorative icons that do not encode meaning.
- Emoji headers.
- Massive utility-class strings.
- Low-contrast gray text on gray surfaces.
- Four or more accent colors from the same blue-purple palette.
- "Beautiful dashboard" layout for a document that only needs a brief.
- Shadows on every card.
- Progress bars that do not represent measurable progress.
- Charts without interpretation.
- Code blocks styled as screenshots.
- Badges that say generic labels like "Important" without explaining why.

Prefer calm, document-first, information-rich design. The reader should notice the structure before the style.

## Legacy design system: do not use

The following patterns belong to a previous design system and must not appear in new artifacts:

- Warm stone grays (`#fafaf9`, `#f5f5f4`, `#1c1917`, Stone palette).
- Token names like `--bg`, `--surface`, `--text`, `--muted`, `--border`, `--accent`, `--danger`, `--neutral`.
- Serif body fonts (Georgia, Times New Roman).
- `999px` pill-radius on navigation links.
- `backdrop-filter: blur()` on navigation bars.
- Border-only cards without elevation (box-shadow).
- Uniform `14px` or `16px` border-radius on all elements; follow the Material shape scale.

Use the Material Design 3 tokens from `references/design-tokens.md` instead.

## Global structure anti-patterns

- The first screen explains the topic instead of stating the conclusion.
- The artifact begins with methodology before findings.
- There is no visible next action.
- Every section has equal weight.
- Long prose appears before a summary, map, table, or decision.
- Details are expanded by default even when the page is dense.
- The navigation contains more than seven top-level items.
- Tables have no headers.
- Color conveys state without text labels.
- The artifact requires external fonts, scripts, images, or build tools.
- The copy/export area appears only at the very bottom of a long interactive editor.

## Plan anti-patterns

- Roadmap is a numbered list with no gates, dependencies, or validation.
- Risks are absent or softened.
- Non-goals are omitted when scope is ambiguous.
- Architecture diagram is decorative and does not clarify flow.
- Phases are time estimates instead of dependency or completion gates.
- Validation commands are missing.
- "Do everything" appears as a phase.

## Compare anti-patterns

- Pros/cons list without side-by-side comparison.
- Recommendation is hidden after the matrix.
- Criteria are vague: "good", "easy", "nice".
- Scoring is used but weights are hidden.
- All options appear equally good.
- Option cards are sorted randomly.
- User selection is not captured in export.

## Review anti-patterns

- "LGTM" without evidence.
- Summary of files changed with no critique.
- Findings do not include severity.
- Findings do not include impact.
- Suggestions are not actionable.
- Code snippets lack context.
- Test plan only says "run tests".
- Copy as Review Comments exports the full page instead of concise PR comments.

## Report anti-patterns

- Executive Summary says "This report covers..." rather than stating findings.
- Methodology comes before conclusions.
- Findings lack evidence labels.
- Data limitations are hidden.
- Action items have no owner or status when those are known.
- The report overuses charts for simple facts.
- Sources appear as raw URLs without explanation.

## Editor anti-patterns

- Controls without labels.
- No live preview.
- No reset.
- No change count.
- No validation warnings.
- Validation blocks export instead of making issues visible.
- Drag-and-drop without keyboard alternative.
- Current state is gathered from text labels rather than actual controls.
- Export contains only changed fields when the receiving AI needs full context.
- Export contains only full state when the human needs a clear diff.

## Round-trip anti-patterns

- Export button opens a modal that the user must manually select and copy.
- Export includes the entire HTML file.
- Export JSON does not match schema.
- Export Markdown is scraped from DOM and loses selected state.
- Export prompt lacks user intent.
- Editor export omits `initialState`, making diffs impossible.
- Review comment export includes non-actionable background.
- Button says "Copied" without actually using clipboard or fallback copy.
- The artifact has interactive controls but no Export Bridge.

## The one acceptable security note

Public sharing note: if you publish or send the HTML file, check whether `<script id="brief-state">` or `<script id="brief-initial-state">` contains project-specific data. Remove sensitive project details before sharing publicly.
