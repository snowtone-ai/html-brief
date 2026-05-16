# Design Tokens

These tokens implement Article 2: Form Follows Information. They follow Google's Material Design 3 system with a human-centered, clean, functional style. They are a reference block to paste into examples or generated artifacts and adapt only when the user has a strong style requirement.

## Token system

The token system uses the Material Design 3 naming convention with `--md-` prefix. All colors use Google's product palette.

```css
:root {
  /* Primary (Google Blue) */
  --md-primary: #1a73e8;
  --md-on-primary: #fff;
  --md-primary-container: #d2e3fc;
  --md-on-primary-container: #062e6f;

  /* Neutral surfaces */
  --md-surface: #fff;
  --md-surface-dim: #f8f9fa;
  --md-surface-container: #f1f3f4;
  --md-surface-container-high: #e8eaed;
  --md-on-surface: #202124;
  --md-on-surface-variant: #5f6368;
  --md-outline: #dadce0;
  --md-outline-variant: #e8eaed;
  --md-background: #fff;

  /* Semantic: error (red) */
  --md-error: #d93025;
  --md-error-container: #fce8e6;
  --md-on-error-container: #5c0a02;

  /* Semantic: success (green) */
  --md-success: #1e8e3e;
  --md-success-container: #e6f4ea;
  --md-on-success-container: #0d652d;

  /* Semantic: warning (amber) */
  --md-warning: #e37400;
  --md-warning-container: #fef7e0;
  --md-on-warning-container: #5e3700;

  /* Semantic: info (blue, same as primary) */
  --md-info: #1a73e8;
  --md-info-container: #e8f0fe;
  --md-on-info-container: #062e6f;

  /* Typography — sans-serif throughout */
  --md-font: 'Google Sans', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
  --md-font-mono: 'Google Sans Mono', 'Roboto Mono', ui-monospace, SFMono-Regular, Consolas, monospace;

  /* Material shape scale */
  --md-shape-xs: 4px;
  --md-shape-sm: 8px;
  --md-shape-md: 12px;
  --md-shape-lg: 16px;
  --md-shape-xl: 28px;
  --md-shape-full: 9999px;

  /* Material elevation (box-shadow levels) */
  --md-elevation-0: none;
  --md-elevation-1: 0 1px 2px 0 rgba(60,64,67,.3), 0 1px 3px 1px rgba(60,64,67,.15);
  --md-elevation-2: 0 1px 2px 0 rgba(60,64,67,.3), 0 2px 6px 2px rgba(60,64,67,.15);
  --md-elevation-3: 0 4px 8px 3px rgba(60,64,67,.15), 0 1px 3px rgba(60,64,67,.3);

  /* Layout */
  --md-content-width: 960px;
}

@media (prefers-color-scheme: dark) {
  :root {
    --md-primary: #8ab4f8;
    --md-on-primary: #062e6f;
    --md-primary-container: #185abc;
    --md-on-primary-container: #d2e3fc;

    --md-surface: #202124;
    --md-surface-dim: #17181a;
    --md-surface-container: #292a2d;
    --md-surface-container-high: #35363a;
    --md-on-surface: #e8eaed;
    --md-on-surface-variant: #9aa0a6;
    --md-outline: #5f6368;
    --md-outline-variant: #3c4043;
    --md-background: #17181a;

    --md-error: #f28b82;
    --md-error-container: #5c0a02;
    --md-on-error-container: #fce8e6;
    --md-success: #81c995;
    --md-success-container: #0d652d;
    --md-on-success-container: #e6f4ea;
    --md-warning: #fdd663;
    --md-warning-container: #5e3700;
    --md-on-warning-container: #fef7e0;
    --md-info: #8ab4f8;
    --md-info-container: #062e6f;
    --md-on-info-container: #e8f0fe;

    --md-elevation-1: 0 1px 3px 1px rgba(0,0,0,.5), 0 1px 2px rgba(0,0,0,.6);
    --md-elevation-2: 0 2px 6px 2px rgba(0,0,0,.5), 0 1px 2px rgba(0,0,0,.6);
    --md-elevation-3: 0 4px 8px 3px rgba(0,0,0,.4), 0 1px 3px rgba(0,0,0,.5);
  }
}

body {
  margin: 0;
  font-family: var(--md-font);
  font-size: 14px;
  line-height: 1.5;
  background: var(--md-background);
  color: var(--md-on-surface);
  -webkit-font-smoothing: antialiased;
}

.hero, main, .export-bar {
  max-width: var(--md-content-width);
  margin-inline: auto;
  padding-inline: 24px;
}

.card {
  background: var(--md-surface);
  border-radius: var(--md-shape-md);
  box-shadow: var(--md-elevation-1);
  padding: 24px;
}

/* Material tonal chip for metadata */
.meta-chip[data-tone="success"] { background: var(--md-success-container); color: var(--md-on-success-container); }
.meta-chip[data-tone="warning"] { background: var(--md-warning-container); color: var(--md-on-warning-container); }
.meta-chip[data-tone="error"]   { background: var(--md-error-container);   color: var(--md-on-error-container); }
.meta-chip[data-tone="info"]    { background: var(--md-info-container);    color: var(--md-on-info-container); }

/* Material buttons */
.btn-tonal {
  height: 40px;
  padding: 0 24px;
  border: none;
  border-radius: var(--md-shape-full);
  background: var(--md-primary-container);
  color: var(--md-on-primary-container);
  font-family: var(--md-font);
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
}
.btn-outlined {
  height: 40px;
  padding: 0 24px;
  border: 1px solid var(--md-outline);
  border-radius: var(--md-shape-full);
  background: transparent;
  color: var(--md-primary);
  font-family: var(--md-font);
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
}

@media (max-width: 680px) {
  .hero, main, .export-bar { padding-inline: 16px; }
  .card { padding: 16px; }
}

@media print {
  .export-bar, nav, button { display: none !important; }
  details { display: block; }
  details > * { display: block; }
  body { background: white; color: #202124; }
  .card { box-shadow: none; border: 1px solid #dadce0; }
}
```

## Typography

Sans-serif is used throughout the artifact for a clean, digital-product feel. Do not use serif fonts for body text. Monospace is reserved strictly for code blocks and inline code.

| Element | Font | Weight | Size |
|---|---|---|---|
| Page title (h1) | --md-font | 400 | 36px |
| Section heading (h2) | --md-font | 400 | 22px |
| Subsection heading (h3) | --md-font | 600 | 14px |
| Body text | --md-font | 400 | 14px |
| Labels / metadata | --md-font | 500 | 12px |
| Code | --md-font-mono | 400 | 13px |
| Buttons | --md-font | 500 | 14px |

## Semantic color rules

- Green/success means recommended, safe, complete, or healthy.
- Amber/warning means uncertainty, partial completion, or watch area.
- Red/error means blocker, defect, risk, or broken invariant.
- Blue/info means neutral context, note, or explanation.
- Gray (on-surface-variant) means metadata, secondary, or low emphasis.

Colors always use the container/on-container pattern from Material Design 3: the container provides a tinted background, and on-container provides readable text on that background.

## Shape scale

Use the Material Design 3 shape scale consistently:

| Element | Radius |
|---|---|
| Small chips, code blocks | --md-shape-sm (8px) |
| Cards, panels | --md-shape-md (12px) |
| Large containers | --md-shape-lg (16px) |
| Buttons, pills | --md-shape-full (9999px) |

## Elevation

Use elevation (box-shadow) instead of borders for cards and panels. This creates a cleaner, more layered appearance consistent with Material Design:

| Level | Use |
|---|---|
| elevation-0 | Flat content within a card |
| elevation-1 | Cards, panels, sections |
| elevation-2 | Hover states, elevated cards |
| elevation-3 | Toasts, snackbars, overlays |

## Anti-patterns

- Do not use serif body fonts (Georgia, Times).
- Do not use warm stone grays (#fafaf9, #1c1917).
- Do not use 999px pill-radius on navigation links.
- Do not use backdrop-filter blur on navigation.
- Do not use border-only cards without elevation.
- Do not use 14px or 16px corner radius uniformly; follow the shape scale.
