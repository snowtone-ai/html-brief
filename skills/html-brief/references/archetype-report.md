# Archetype: Report

## Purpose

Use Report when the user needs a research synthesis, incident report, weekly update, status update, explainer, or stakeholder-facing brief. A Report is not a long essay; it is an evidence-forward briefing that starts with conclusions.

## Constitution articles implemented

- Article 1: Executive summary and key finding cards support quick understanding.
- Article 2: Metric cards, timelines, and evidence chips encode information.
- Article 3: Export Bridge enables sharing as Markdown, JSON, or prompt.
- Article 4: The report is a standalone HTML file.
- Article 5: Findings must distinguish evidence, inference, assumption, and uncertainty.
- Article 6: Sections adapt to research, incident, or status context.
- Article 7: Use Report when visual hierarchy or evidence grouping improves comprehension.

## Exact HTML structure

```html
<body data-brief-archetype="report">
  <header class="hero">
    <p class="eyebrow">Report Brief</p>
    <h1><!-- report title --></h1>
    <p class="hero-summary"><!-- conclusion, not topic description --></p>
    <div class="metric-strip"><!-- 1-4 key metrics --></div>
  </header>

  <main>
    <section id="executive-summary" class="panel">
      <h2>Executive Summary</h2>
      <ol class="summary-list"><!-- exactly 3-5 conclusion bullets --></ol>
      <aside class="action-callout"><!-- what the reader should do --></aside>
    </section>

    <section id="key-findings" class="finding-grid">
      <article class="finding-card" data-evidence="source-backed">
        <h3><!-- finding --></h3>
        <p><!-- evidence and implication --></p>
        <span class="evidence-chip"><!-- Source-backed / Inferred / Assumption --></span>
      </article>
    </section>

    <section id="timeline" class="panel wide">
      <h2>Timeline</h2>
      <svg role="img" aria-labelledby="timeline-title"><!-- optional incident/research timeline --></svg>
    </section>

    <section id="analysis" class="panel">
      <h2>Detailed Analysis</h2>
      <details><summary><!-- topic conclusion --></summary><!-- detail --></details>
    </section>

    <section id="actions" class="panel">
      <h2>Action Items</h2>
      <table><!-- action, owner, status, evidence, due/gate if known --></table>
    </section>

    <section id="sources" class="panel">
      <details>
        <summary>Sources and methodology</summary>
        <ul><!-- sources, input limitations, assumptions --></ul>
      </details>
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

- `.metric-strip` should visually elevate only the metrics that matter.
- `.finding-grid` allows varying card size based on importance.
- Evidence chips are neutral and text-labeled.
- Methodology belongs near the end unless the methodology itself is the central topic.
- Timelines use a simple line, labeled events, and cause/effect notes.

## JS patterns

Report is usually static. JS is for exports and optional filtering by evidence type or action status. Do not create dashboard-like controls unless the user needs them.

## Anti-patterns

- Executive Summary that says "This report covers..." instead of stating conclusions.
- Methodology first.
- More than six key finding cards.
- Findings without evidence labels.
- Beautiful charts with no interpretation.

## Export Bridge manifestation

- Copy as Prompt: report conclusions, evidence model, assumptions, and requested next action.
- Copy as JSON: report state with findings, actions, sources, confidence.
- Copy as Markdown: stakeholder-readable report with summary, findings, details, actions, sources.
