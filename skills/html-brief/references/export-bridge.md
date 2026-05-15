# Export Bridge Reference

Export Bridge implements Article 3: Communication Is a Loop. It converts a human's reading, selection, or edits into formats that can be pasted back into an AI or stored in a repository. It must be plain vanilla JavaScript and must not require a framework.

## Required state model

Every artifact that includes export buttons must embed a JSON state block:

```html
<script type="application/json" id="brief-state">
{
  "version": "1.0",
  "archetype": "plan",
  "createdAt": "2026-05-15T00:00:00.000Z",
  "userIntent": "Create a migration plan",
  "state": {},
  "initialState": null
}
</script>
```

Editor artifacts must use `brief-initial-state` and gather current state from controls:

```html
<script type="application/json" id="brief-initial-state">{ "version": "1.0", "archetype": "editor", "state": {}, "initialState": {} }</script>
```

## Copy as Prompt exact output format

### Plan

```text
The user reviewed this html-brief Plan.

User intent:
<userIntent>

Plan summary:
<title>
<summary>

State JSON:
<pretty JSON>

Please continue from this plan. Preserve the goals, non-goals, decisions, phases, risks, and validation gates unless I explicitly change them.
```

### Compare

```text
The user reviewed this html-brief Compare decision.

Decision question:
<question>

Selected option:
<option name>

Rationale:
<rationale>

Full decision state:
<pretty JSON>

Please apply this decision and call out any implementation consequences.
```

### Review

```text
The user reviewed this html-brief PR/code review.

Verdict:
<verdict>

Findings:
<severity-grouped findings>

Full review state:
<pretty JSON>

Please address the findings, starting with blocker and high severity items.
```

### Report

```text
The user reviewed this html-brief Report.

Report title:
<title>

Executive conclusions:
<bullets>

Evidence and assumptions:
<evidence summary>

Full report state:
<pretty JSON>

Please use this report as context for the next answer.
```

### Editor

```text
The user edited the following data in an HTML brief.

User intent:
<userIntent>

Initial state:
<pretty JSON>

Current state:
<pretty JSON>

Changed keys:
<list>

Validation notes:
<list>

Please apply these changes.
```

## Copy as JSON validation rules

- Output must be valid JSON, not JavaScript.
- Output must include `version`, `archetype`, `createdAt`, `userIntent`, `state`, and `initialState`.
- `version` must be `"1.0"`.
- `archetype` must be one of `plan`, `compare`, `review`, `report`, `editor`.
- `state` must match the archetype schema.
- `initialState` must be `null` for static artifacts unless the artifact tracks edits.
- Editor JSON must include both initial and current state.

## Copy as Markdown conversion logic

Generate Markdown from state, never by scraping visual HTML.

### Plan Markdown

```markdown
# <title>

Status: <status>
Confidence: <confidence>

## Summary
<summary>

## Goals
- <goal>

## Non-goals
- <non-goal>

## Key Decisions
| Decision | Choice | Rationale |
|---|---|---|

## Phases
### <phase>
Gate: <gate>
Tasks:
- <task>
Validation:
- <validation>

## Risks
| Severity | Risk | Mitigation |
|---|---|---|
```

### Compare Markdown

```markdown
# Decision: <question>

## Recommended option
<option> — <rationale>

## Options
### <option>
Optimizes for: <value>
Pros:
- ...
Cons:
- ...

## Tradeoff Matrix
| Criteria | Option A | Option B |
|---|---|---|

## Consequences
- ...
```

### Review Markdown

```markdown
# Review: <title>

Verdict: <verdict>

## Findings
### <severity>: <title>
File: <file>
Impact: <impact>
Suggestion: <suggestion>

## Test Coverage
- Covered: ...
- Missing: ...
```

### Report Markdown

```markdown
# <title>

## Executive Summary
1. ...

## Key Findings
### <finding>
Evidence: <evidence label>
Implication: <implication>

## Actions
| Action | Owner | Status |
|---|---|---|

## Sources and Methodology
- ...
```

### Editor Markdown

```markdown
# Edited State: <title>

## Changed Keys
- `<path>`: `<before>` → `<after>`

## Current State Summary
- ...

## Validation Notes
- ...
```

## Copy as Review Comments

Review archetype only. Output GitHub PR-compatible Markdown grouped by severity:

```markdown
## html-brief review comments

### Blocker
- **`src/path/file.ts:42`** — <issue>
  - Impact: <impact>
  - Suggestion: <suggestion>

### High
- ...

### Medium
- ...

### Low
- ...
```

Do not include the entire review brief. Include only actionable comments.

## Vanilla JavaScript implementation pattern

```html
<script>
(function () {
  function readStaticState() {
    var node = document.getElementById('brief-state');
    if (!node) return null;
    return JSON.parse(node.textContent);
  }

  function showToast(message) {
    var toast = document.getElementById('copy-toast');
    if (!toast) {
      toast = document.createElement('div');
      toast.id = 'copy-toast';
      toast.setAttribute('role', 'status');
      toast.style.position = 'fixed';
      toast.style.right = '1rem';
      toast.style.bottom = '1rem';
      toast.style.padding = '.75rem 1rem';
      toast.style.border = '1px solid var(--border, #ddd)';
      toast.style.background = 'var(--surface, #fff)';
      toast.style.borderRadius = '12px';
      document.body.appendChild(toast);
    }
    toast.textContent = message;
    clearTimeout(window.__briefToastTimer);
    window.__briefToastTimer = setTimeout(function () { toast.textContent = ''; }, 2200);
  }

  function copyText(text, label) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () {
        showToast('Copied ' + label);
      }).catch(function () {
        fallbackCopy(text, label);
      });
    } else {
      fallbackCopy(text, label);
    }
  }

  function fallbackCopy(text, label) {
    var area = document.createElement('textarea');
    area.value = text;
    area.setAttribute('readonly', '');
    area.style.position = 'fixed';
    area.style.left = '-9999px';
    document.body.appendChild(area);
    area.select();
    document.execCommand('copy');
    document.body.removeChild(area);
    showToast('Copied ' + label);
  }

  function toMarkdown(envelope) {
    var s = envelope.state || {};
    if (envelope.archetype === 'plan') {
      return '# ' + s.title + '\n\n## Summary\n' + s.summary + '\n';
    }
    return '# ' + (s.title || envelope.archetype + ' brief') + '\n\n```json\n' + JSON.stringify(envelope, null, 2) + '\n```\n';
  }

  function toPrompt(envelope) {
    return [
      'The user reviewed this html-brief artifact.',
      '',
      'Archetype: ' + envelope.archetype,
      'User intent: ' + (envelope.userIntent || ''),
      '',
      'State JSON:',
      JSON.stringify(envelope, null, 2),
      '',
      'Please continue using this state.'
    ].join('\n');
  }

  document.addEventListener('click', function (event) {
    var button = event.target.closest('[data-copy]');
    if (!button) return;
    var envelope = window.gatherBriefEnvelope ? window.gatherBriefEnvelope() : readStaticState();
    if (!envelope) return showToast('No brief state found');
    var mode = button.getAttribute('data-copy');
    if (mode === 'json') copyText(JSON.stringify(envelope, null, 2), 'JSON');
    if (mode === 'markdown') copyText(toMarkdown(envelope), 'Markdown');
    if (mode === 'prompt') copyText(toPrompt(envelope), 'Prompt');
    if (mode === 'review-comments') copyText(window.toReviewComments(envelope), 'review comments');
  });
})();
</script>
```

## Failure conditions

- Button opens a modal instead of copying.
- Export contains full HTML.
- Export cannot be pasted into a clean AI session and understood.
- JSON is invalid or missing archetype.
- Editor export omits initial state.
