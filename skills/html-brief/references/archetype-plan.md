# Archetype: Plan

## Purpose

Use Plan when the user's next action is to build, migrate, roll out, refactor, launch, or coordinate work. A Plan brief is a decision-ready implementation document: it should let engineers understand the sequence, PMs understand scope and risks, and vibe coders understand what to do next.

## Constitution articles implemented

- Article 1: Hero summary, section navigation, timeline, and details keep the reader inside the 2–5 minute budget.
- Article 2: Diagrams, timelines, status badges, and risk colors encode information rather than decoration.
- Article 3: Export Bridge converts the plan into JSON, Markdown, and a paste-back prompt.
- Article 4: The output is one browser-openable HTML file with inline CSS/JS only.
- Article 5: Risks, non-goals, assumptions, and confidence are explicit.
- Article 6: Sections may be removed if they do not fit the task, but the conclusion and risk treatment remain mandatory.
- Article 7: Use Plan only when a Markdown list would hide sequencing, dependency, or risk information.

## Exact HTML structure

```html
<body data-brief-archetype="plan">
  <header class="hero">
    <p class="eyebrow">Plan Brief</p>
    <h1><!-- plan title --></h1>
    <p class="hero-summary"><!-- conclusion in 1-2 sentences --></p>
    <dl class="meta-grid">
      <div><dt>Status</dt><dd><!-- proposed/ready/blocked --></dd></div>
      <div><dt>Confidence</dt><dd><!-- high/medium/low + reason --></dd></div>
      <div><dt>Primary risk</dt><dd><!-- risk headline --></dd></div>
    </dl>
  </header>

  <nav class="section-nav" aria-label="Plan sections">
    <a href="#overview">Overview</a>
    <a href="#architecture">Architecture</a>
    <a href="#phases">Phases</a>
    <a href="#risks">Risks</a>
    <a href="#exports">Export</a>
  </nav>

  <main>
    <section id="overview" class="panel">
      <h2>Overview</h2>
      <div class="two-column">
        <article>
          <h3>Goal</h3>
          <ul><!-- goals, max 5 --></ul>
        </article>
        <article>
          <h3>Non-goals</h3>
          <ul><!-- non-goals, max 5 --></ul>
        </article>
      </div>
      <table class="decision-table"><!-- key decisions --></table>
    </section>

    <section id="architecture" class="panel wide">
      <h2>Architecture / Flow</h2>
      <figure>
        <svg role="img" aria-labelledby="architecture-title"><!-- flow diagram --></svg>
        <figcaption><!-- plain-language interpretation --></figcaption>
      </figure>
    </section>

    <section id="phases" class="panel">
      <h2>Phased Plan</h2>
      <ol class="timeline">
        <li><!-- phase name, gate, tasks, validation --></li>
      </ol>
    </section>

    <section id="risks" class="panel">
      <h2>Risks and mitigations</h2>
      <table class="risk-table"><!-- risk, severity, signal, mitigation, owner --></table>
    </section>

    <section id="exports" class="export-bar" aria-label="Export Bridge">
      <button data-copy="prompt">Copy as Prompt</button>
      <button data-copy="json">Copy as JSON</button>
      <button data-copy="markdown">Copy as Markdown</button>
    </section>
  </main>

  <script type="application/json" id="brief-state">{...}</script>
  <script><!-- vanilla Export Bridge --></script>
</body>
```

## CSS patterns

- `.hero` uses the strongest visual weight and no decorative background.
- `.meta-grid` is a responsive definition-list grid.
- `.decision-table` uses semantic table markup and a sticky first column only if the table is wide.
- `.timeline` uses a vertical list on mobile and may use an SVG or connected line on desktop.
- `.risk-table [data-severity="high"]` uses danger color plus a text label.
- `.wide` can exceed the reading column only for diagrams and tables.

## JS patterns

Plan is usually read-only. Use JavaScript only for copy buttons, optional section tabs, and optional filtering by phase or risk severity. The state object is static unless the plan includes checkboxes for selected phases. Copy functions must read from `#brief-state`, not scrape visible text.

## Anti-patterns

- A numbered list of tasks with no dependencies, gates, validation, or risks.
- A diagram that repeats the text without adding spatial understanding.
- A "risk-free" plan.
- A plan that hides the actual recommendation until the end.
- Exporting the entire HTML instead of plan state.

## Export Bridge manifestation

- Copy as Prompt: "Implement or revise this plan" plus state JSON and key assumptions.
- Copy as JSON: `brief.schema.json` envelope with `archetype: "plan"` and `state` matching `plan.schema.json`.
- Copy as Markdown: RFC-style plan with headings: Summary, Goals, Non-goals, Decisions, Architecture, Phases, Risks, Validation.
