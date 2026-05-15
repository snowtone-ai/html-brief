# Archetype: Review

## Purpose

Use Review when the user needs to understand or critique a code change, PR, diff, architecture change, or generated implementation. The artifact should make the change legible, identify risks, and export actionable review comments.

## Constitution articles implemented

- Article 1: Findings summary and change map reduce review time.
- Article 2: Severity badges, annotated diff blocks, and module maps encode meaning.
- Article 3: Copy as Review Comments is mandatory.
- Article 4: The review opens as one standalone HTML file.
- Article 5: Findings must include uncertainty and test coverage gaps.
- Article 6: Review depth adapts to the codebase and change type.
- Article 7: Use Review only when visual diff and annotation add value.

## Exact HTML structure

```html
<body data-brief-archetype="review">
  <header class="hero">
    <p class="eyebrow">Review Brief</p>
    <h1><!-- PR/change title --></h1>
    <p class="hero-summary"><!-- why this change matters and verdict --></p>
    <div class="finding-counts"><!-- blocker/high/medium/low counts --></div>
  </header>

  <main>
    <section id="motivation" class="panel">
      <h2>Motivation</h2>
      <div class="before-after">
        <article><h3>Before</h3><p><!-- old behavior --></p></article>
        <article><h3>After</h3><p><!-- new behavior --></p></article>
      </div>
    </section>

    <section id="change-map" class="panel wide">
      <h2>Change map</h2>
      <svg role="img" aria-labelledby="change-map-title"><!-- modules/files --></svg>
    </section>

    <section id="findings" class="panel">
      <h2>Findings</h2>
      <article class="finding" data-severity="high">
        <h3><!-- finding title --></h3>
        <p><!-- impact --></p>
        <pre><code><!-- relevant diff or code --></code></pre>
        <p class="recommendation"><!-- fix recommendation --></p>
      </article>
    </section>

    <section id="files" class="panel">
      <h2>File-by-file notes</h2>
      <details>
        <summary><!-- file path + finding count --></summary>
        <pre class="diff"><code><!-- annotated diff --></code></pre>
      </details>
    </section>

    <section id="tests" class="panel">
      <h2>Test plan coverage</h2>
      <table><!-- covered / missing / recommended --></table>
    </section>

    <section id="exports" class="export-bar">
      <button data-copy="review-comments">Copy as Review Comments</button>
      <button data-copy="prompt">Copy as Prompt</button>
      <button data-copy="json">Copy as JSON</button>
      <button data-copy="markdown">Copy as Markdown</button>
    </section>
  </main>

  <script type="application/json" id="brief-state">{...}</script>
</body>
```

## CSS patterns

- Severity classes: `blocker`, `high`, `medium`, `low`, `info`; each has color plus text label.
- Diff lines use `.add`, `.remove`, `.context`, and `.note`.
- Use monospace only for code, not body content.
- `.before-after` uses two columns on desktop and one column on mobile.
- Keep code blocks scrollable and preserve whitespace.

## JS patterns

Review needs JS for copy exports only. Do not implement an editor unless the user asked for annotation editing. Review comments should be produced from the state object's findings array.

## Anti-patterns

- "Looks good" with no evidence.
- A review that only summarizes files but does not identify risks.
- Severity labels without actionable next steps.
- Diffs without line context.
- Copy as Review Comments that exports generic prose instead of PR-ready Markdown.

## Export Bridge manifestation

- Copy as Review Comments: Markdown grouped by severity. Each item includes file, line if known, issue, impact, suggestion.
- Copy as Prompt: ask the AI to apply or evaluate the review comments.
- Copy as JSON: state with findings, files, test coverage, verdict.
- Copy as Markdown: review brief summary with findings and test plan.
