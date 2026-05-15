# Archetype: Compare

## Purpose

Use Compare when the user must choose between options. The artifact should make tradeoffs visible, prevent false equivalence, and produce a decision that can be pasted back into an AI or stored as a record.

## Constitution articles implemented

- Article 1: A recommendation banner and side-by-side cards support fast scanning.
- Article 2: Color and layout encode option status, score, and tradeoff meaning.
- Article 3: Export Bridge captures the selected option and rationale.
- Article 4: The comparison is a single self-contained HTML file.
- Article 5: Every option must include a downside; "all options are good" is invalid.
- Article 6: Criteria and scoring may adapt to the domain.
- Article 7: Use Compare only when spatial comparison improves understanding.

## Exact HTML structure

```html
<body data-brief-archetype="compare">
  <header class="hero">
    <p class="eyebrow">Decision Brief</p>
    <h1><!-- decision question --></h1>
    <p class="hero-summary"><!-- recommended direction and reason --></p>
    <aside class="recommendation" data-confidence="medium">
      <strong>Recommended:</strong> <!-- option name -->
      <span><!-- confidence and caveat --></span>
    </aside>
  </header>

  <main>
    <section id="options" class="option-grid" aria-label="Options">
      <article class="option-card" data-option-id="">
        <h2><!-- option name --></h2>
        <p class="optimizes-for">Optimizes for: <!-- value --></p>
        <ul class="pros"><!-- max 3 --></ul>
        <ul class="cons"><!-- max 3 --></ul>
        <label><input type="radio" name="selectedOption"> Select this option</label>
      </article>
    </section>

    <section id="matrix" class="panel">
      <h2>Tradeoff matrix</h2>
      <table>
        <thead><tr><th>Criteria</th><!-- option headings --></tr></thead>
        <tbody><!-- ✓ / ~ / ✗ with text labels --></tbody>
      </table>
    </section>

    <section id="decision" class="panel">
      <h2>Decision context</h2>
      <details open><summary>Why this recommendation is reasonable</summary><!-- explanation --></details>
      <details><summary>When to choose another option</summary><!-- fallback conditions --></details>
    </section>

    <section id="exports" class="export-bar">
      <button data-copy="prompt">Copy as Prompt</button>
      <button data-copy="json">Copy as JSON</button>
      <button data-copy="markdown">Copy as Markdown</button>
    </section>
  </main>

  <script type="application/json" id="brief-state">{...}</script>
</body>
```

## CSS patterns

- `.option-grid` uses `grid-template-columns: repeat(auto-fit, minmax(240px, 1fr))`.
- `.option-card[data-recommended="true"]` uses a semantic success border and a visible "Recommended" label.
- Matrix cells use `data-rating="good|mixed|bad"` with icons or labels plus color.
- On mobile, cards stack before the matrix; the matrix scrolls horizontally inside a container if needed.

## JS patterns

Use JS to update the selected option in state, recompute the export payload, and show a toast. Weighted scoring is allowed only if the scoring model is visible; hidden scoring is an anti-pattern.

## Anti-patterns

- A giant prose list where options cannot be compared side-by-side.
- A score table with no explanation of criteria.
- Every option receiving the same rating.
- Color-only ratings without text.
- Recommendation hidden after long methodology.

## Export Bridge manifestation

- Copy as Prompt: selected option, rationale, unresolved risks, and a request to apply the decision.
- Copy as JSON: selected option plus all options and criteria.
- Copy as Markdown: ADR-like record with Context, Options, Decision, Consequences.
