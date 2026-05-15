# Archetype: Editor

## Purpose

Use Editor when the user needs to manipulate structured information: tune settings, reorder tickets, adjust feature flags, classify rows, edit prompts, triage tasks, or choose parameters. Editor is the clearest expression of html-brief as a two-way AI-human communication loop.

## Constitution articles implemented

- Article 1: The interface starts with a clear task and state indicator.
- Article 2: Controls, grouping, warnings, and layout encode relationships and constraints.
- Article 3: Export Bridge and reset are mandatory; without them the editor fails.
- Article 4: The editor is one self-contained HTML file with vanilla JS.
- Article 5: Validation warnings and conflicts are visible.
- Article 6: The control type adapts to the data: form, table, kanban, split pane, or picker.
- Article 7: Use Editor only when user manipulation is the point.

## Exact HTML structure

```html
<body data-brief-archetype="editor">
  <header class="hero">
    <p class="eyebrow">Editor Brief</p>
    <h1>Editor: <!-- edited thing --></h1>
    <p class="hero-summary"><!-- one-line operation instruction --></p>
    <div class="state-indicator">
      <span id="change-count">0 changes</span>
      <span id="warning-count">0 warnings</span>
    </div>
  </header>

  <main>
    <section id="editor-area" class="editor-layout">
      <form id="editor-form">
        <fieldset>
          <legend><!-- group name --></legend>
          <label><!-- control label --><input></label>
        </fieldset>
      </form>

      <aside id="live-preview" class="preview-panel">
        <h2>Live Preview</h2>
        <!-- rendered current state -->
      </aside>
    </section>

    <section id="validation" class="panel" aria-live="polite">
      <h2>Validation Warnings</h2>
      <ul id="warnings"></ul>
    </section>
  </main>

  <section id="exports" class="export-bar sticky" aria-label="Export Bridge">
    <button data-copy="prompt">Copy as Prompt</button>
    <button data-copy="json">Copy as JSON</button>
    <button data-copy="markdown">Copy as Markdown</button>
    <button data-action="reset">Reset</button>
  </section>

  <script type="application/json" id="brief-initial-state">{...}</script>
  <script><!-- gatherCurrentState, validate, render, export, reset --></script>
</body>
```

## CSS patterns

- `.editor-layout` uses two columns on desktop: controls and preview.
- `.export-bar.sticky` is fixed or sticky at the bottom with enough bottom padding on the page.
- Warning states use danger or warning colors plus text labels.
- Use form fieldsets to group related controls.
- For drag-and-drop editors, also provide move buttons for keyboard users.

## JS patterns

Required functions:

```js
const initialState = JSON.parse(document.getElementById('brief-initial-state').textContent);

function gatherCurrentState() {
  // Read DOM controls and return schema-compliant state.
}

function validateState(state) {
  // Return warnings and errors as arrays. Do not block export; make issues visible.
}

function renderPreview(state) {
  // Update preview and state indicators.
}

function copyAsPrompt() {
  const current = gatherCurrentState();
  const prompt = [
    'The user edited the following data in an HTML brief.',
    '',
    'Initial state:',
    JSON.stringify(initialState, null, 2),
    '',
    'Current state:',
    JSON.stringify(current, null, 2),
    '',
    'Please apply these changes.'
  ].join('\n');
  navigator.clipboard.writeText(prompt);
}

function resetEditor() {
  // Restore controls from initialState.
}
```

## Anti-patterns

- A form without live preview.
- Export that omits initialState, making diffs impossible.
- Reset missing.
- Validation hidden until export.
- Drag-and-drop without keyboard alternative.
- Exporting the full HTML instead of state and intent.

## Export Bridge manifestation

- Copy as Prompt: initial state, current state, changed keys, validation notes, and an instruction to apply changes.
- Copy as JSON: envelope with `initialState` and current `state`.
- Copy as Markdown: human-readable changelog of edited fields.
- Reset: restore the original embedded state exactly.
