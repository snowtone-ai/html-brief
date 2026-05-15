<p align="center">
  <img src="docs/assets/logo.svg" alt="html-brief" width="120" />
</p>

<h1 align="center">html-brief</h1>

<p align="center">
  <strong>AI output you can actually read, decide on, and send back.</strong>
</p>

<p align="center">
  <a href="#install"><img src="https://img.shields.io/badge/install-30s-blue" alt="Install in 30s" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License" /></a>
  <a href="#works-with"><img src="https://img.shields.io/badge/agents-Claude_Code_%7C_Codex_%7C_Cursor_%7C_Gemini-8A2BE2" alt="Multi-agent" /></a>
</p>

<p align="center">
  <a href="#install">Install</a> · <a href="#quickstart">Quickstart</a> · <a href="#archetypes">Archetypes</a> · <a href="#examples">Examples</a> · <a href="#round-trip">Round-trip</a> · <a href="CONTRIBUTING.md">Contribute</a>
</p>

---

AI agents write 400-line plans nobody reads.

**html-brief** turns that into a single HTML file you open in a browser — with a summary you scan in 5 seconds, diagrams you understand at a glance, and a "Copy as Prompt" button that sends your decisions back to the agent.

## What This Is Not

This is not a frontend framework, a website generator, or a design polish plugin. It does not replace Markdown for short answers. It is for the moment when AI output becomes too complex to read, compare, or act on as plain text.

<!-- 📸 REPLACE THIS with a real Before/After GIF or screenshot
     See docs/SCREENSHOT-GUIDE.md for how to capture it.
-->
<p align="center">
  <img src="docs/assets/before-after.gif" alt="Before: 400-line Markdown → After: scannable HTML brief" width="720" />
</p>

## Install

```bash
git clone https://github.com/YOUR_USERNAME/html-brief.git
cd html-brief
```

Pick your agent:

```bash
# Claude Code
mkdir -p ~/.claude/skills && ln -sf "$(pwd)/skills/html-brief" ~/.claude/skills/html-brief

# Codex CLI
mkdir -p ~/.codex/skills && ln -sf "$(pwd)/skills/html-brief" ~/.codex/skills/html-brief

# Gemini CLI
mkdir -p ~/.gemini/skills && ln -sf "$(pwd)/skills/html-brief" ~/.gemini/skills/html-brief

# Cursor (current project)
mkdir -p .cursor/skills && ln -sf "$(pwd)/skills/html-brief" .cursor/skills/html-brief
```

Done. No dependencies. No build step. No config.

## Quickstart

```bash
/html-brief Create an implementation plan for a zero-downtime Postgres migration.
```

The skill picks the right archetype, generates a self-contained `.html` file, and you open it in any browser.

Other things you can say:

```
"Compare JWT vs session cookies vs OAuth proxy — make it an html-brief."
"Review this PR as an html-brief. Focus on the streaming logic."
"Create a feature-flag editor I can tune and copy back as JSON."
"Summarize this week's incident into a shareable html-brief report."
```

## The Problem

AI agents are getting better at thinking. They are not getting better at communicating.

A 400-line Markdown plan may be correct, but you have to scroll, hold dependencies in your head, compare options mentally, and copy pieces by hand. In practice, most people skim the first 20 lines and guess the rest.

html-brief uses HTML because HTML can do what Markdown cannot: hierarchy with progressive disclosure, tables with color-coded severity, SVG architecture diagrams, interactive controls, and copy/export buttons — all in one file you open locally or share as a link.

> Inspired by [Thariq Shihipar's article](https://thariqs.github.io/html-effectiveness/) on the unreasonable effectiveness of HTML for AI-human communication.

## Archetypes

The skill routes your request to the best-fit archetype:

| Archetype | When to use | What you get |
|:---|:---|:---|
| **Plan** | Implementation specs, migrations, rollouts, RFCs | Hero summary → architecture SVG → phased timeline → risks → validation gates |
| **Compare** | Choosing between options, tradeoff analysis | Recommendation banner → side-by-side cards → criteria matrix → decision memo export |
| **Review** | PR reviews, code understanding, diff explainers | Motivation → change map → annotated diff → findings by severity → copyable review comments |
| **Report** | Incident reports, research, status updates, explainers | Executive summary → key findings → evidence with confidence labels → progressive detail |
| **Editor** | Feature flags, prompt tuning, ticket sorting, settings | Interactive controls → live preview → validation → Copy as JSON / Prompt / Markdown |

You don't need to choose. Say `/html-brief` and describe what you need. The skill decides.

## Examples

<!-- 📸 REPLACE each placeholder with a real screenshot.
     Take screenshots of the example HTML files opened in a browser.
     Recommended size: 720px wide. Use a clean browser window.
-->

<table>
<tr>
<td width="33%" align="center">
<a href="skills/html-brief/examples/plan-db-migration/output.html">
<img src="docs/assets/example-plan.png" alt="Plan example" width="220" /><br/>
<strong>Plan</strong><br/>
<sub>Zero-downtime DB migration</sub>
</a>
</td>
<td width="33%" align="center">
<a href="skills/html-brief/examples/review-streaming-pr/output.html">
<img src="docs/assets/example-review.png" alt="Review example" width="220" /><br/>
<strong>Review</strong><br/>
<sub>Streaming PR explainer</sub>
</a>
</td>
<td width="33%" align="center">
<a href="skills/html-brief/examples/edit-feature-flags/output.html">
<img src="docs/assets/example-editor.png" alt="Editor example" width="220" /><br/>
<strong>Editor</strong><br/>
<sub>Feature flag tuner</sub>
</a>
</td>
</tr>
</table>

Each example is a single `.html` file — inline CSS, vanilla JS, zero dependencies. Open it in any browser.

## Round-trip

html-brief is not a one-way export. Every brief includes an **Export Bridge**:

```
┌─────────┐      ┌─────────────┐      ┌─────────┐
│ AI Agent │ ───▶ │ HTML Brief  │ ───▶ │ AI Agent │
│          │      │             │      │          │
│ generate │      │ read/edit/  │      │ continue │
│          │      │ decide      │      │          │
└─────────┘      └──────┬──────┘      └─────────┘
                        │
              Copy as Prompt
              Copy as JSON
              Copy as Markdown
```

You read the brief. You make decisions. You click "Copy as Prompt." You paste it into your next agent session. The loop closes.

## Works With

| Agent | Install method | Invocation |
|:---|:---|:---|
| **Claude Code** | `~/.claude/skills/` symlink | `/html-brief <request>` |
| **Codex CLI** | `~/.codex/skills/` symlink | `/html-brief <request>` |
| **Gemini CLI** | `~/.gemini/skills/` symlink | `/html-brief <request>` |
| **Cursor** | `.cursor/skills/` symlink | Reference skill in prompt |
| **GitHub Desktop** | Open this repo as a local repository | Use `File > Open local repository` |

The skill files are agent-agnostic Markdown. Any agent that reads `SKILL.md` can use them.

## Manual-Only Mode

By default, the skill can be auto-selected when the request matches. To require explicit invocation:

Add to `skills/html-brief/SKILL.md` frontmatter:

```yaml
disable-model-invocation: true
```

Then always invoke with `/html-brief <request>`.

## Validation

```bash
python3 scripts/validate.py
```

Checks HTML self-containment, Export Bridge presence, schema validity, and SKILL.md structure.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

New archetype ideas, example briefs, agent compatibility reports, and design token improvements are all welcome.

## License

[MIT](LICENSE)

---

<p align="center">
  If html-brief saves you from skimming a 400-line Markdown wall,<br/>consider giving it a ⭐ so others can find it too.
</p>
