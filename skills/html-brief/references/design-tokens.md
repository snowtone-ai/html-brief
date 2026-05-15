# Design Tokens

These tokens implement Article 2: Form Follows Information. They are a reference block to paste into examples or generated artifacts and adapt only when the user has a strong style requirement.

```css
:root {
  --font-body: Georgia, 'Times New Roman', serif;
  --font-heading: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --font-mono: ui-monospace, SFMono-Regular, Consolas, 'Liberation Mono', monospace;
  --font-ui: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;

  --bg: #fafaf9;
  --fg: #1c1917;
  --muted: #57534e;
  --surface: #ffffff;
  --surface-subtle: #f5f5f4;
  --border: #e7e5e4;

  --success: #047857;
  --success-bg: #ecfdf5;
  --warning: #b45309;
  --warning-bg: #fffbeb;
  --danger: #b91c1c;
  --danger-bg: #fef2f2;
  --info: #1d4ed8;
  --info-bg: #eff6ff;

  --radius: 14px;
  --space-1: .25rem;
  --space-2: .5rem;
  --space-3: .75rem;
  --space-4: 1rem;
  --space-6: 1.5rem;
  --space-8: 2rem;
  --content: 72ch;
  --wide: 1080px;
}

@media (prefers-color-scheme: dark) {
  :root {
    --bg: #0c0a09;
    --fg: #e7e5e4;
    --muted: #a8a29e;
    --surface: #1c1917;
    --surface-subtle: #292524;
    --border: #44403c;
    --success: #34d399;
    --success-bg: #064e3b;
    --warning: #fbbf24;
    --warning-bg: #451a03;
    --danger: #f87171;
    --danger-bg: #450a0a;
    --info: #60a5fa;
    --info-bg: #172554;
  }
}

body {
  margin: 0;
  font-family: var(--font-body);
  background: var(--bg);
  color: var(--fg);
  line-height: 1.6;
}

h1, h2, h3, nav, button, .eyebrow, .meta-grid {
  font-family: var(--font-heading);
}

.hero, main, .export-bar {
  width: min(var(--wide), calc(100% - 2rem));
  margin-inline: auto;
}

.panel, .option-card, .finding-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: var(--space-6);
}

.badge[data-tone="success"] { color: var(--success); background: var(--success-bg); }
.badge[data-tone="warning"] { color: var(--warning); background: var(--warning-bg); }
.badge[data-tone="danger"] { color: var(--danger); background: var(--danger-bg); }
.badge[data-tone="info"] { color: var(--info); background: var(--info-bg); }

@media (max-width: 520px) {
  .hero, main, .export-bar { width: min(100% - 1rem, var(--wide)); }
  .panel { padding: var(--space-4); }
}

@media print {
  .export-bar, nav, button { display: none !important; }
  details { display: block; }
  details > * { display: block; }
  body { background: white; color: black; }
}
```

## Typography rotation

Use body and heading typefaces to change document tone without becoming decorative. Do not depend on external fonts.

| Tone | Heading | Body |
|---|---|---|
| Technical | system-ui | Georgia |
| Executive | Avenir Next/system-ui | Georgia |
| Data-heavy | IBM Plex Sans fallback | system-ui |
| Casual | system-ui | Charter/Georgia |
| Code-heavy | system-ui | system-ui with monospace only for code |

## Semantic color rules

- Green/success means recommended, safe, complete, or healthy.
- Amber/warning means uncertainty, partial completion, or watch area.
- Red/danger means blocker, defect, risk, or broken invariant.
- Blue/info means neutral context, note, or explanation.
- Gray means metadata, background, unavailable, or low emphasis.
