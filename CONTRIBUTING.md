# Contributing

html-brief is an information architecture skill, not a frontend component project.

## Contribution principles

- Preserve the Artifact Constitution.
- Keep examples self-contained.
- Use vanilla JavaScript only inside examples.
- Do not add external dependencies to example HTML.
- Use semantic color only.
- Add or update schemas when export state changes.
- Keep Export Bridge outputs paste-back-to-AI friendly.

## Adding an archetype reference

1. Explain which Constitution articles it implements.
2. Define exact HTML structure.
3. Define CSS patterns.
4. Define JS patterns only when interactive.
5. Define anti-patterns.
6. Define Export Bridge behavior.
7. Add or update a JSON Schema.

## Adding an example

1. Add `before.md`.
2. Add `output.html`.
3. Add `round-trip.json`.
4. Run `python3 scripts/validate.py`.
5. Open the HTML directly in a browser.
6. Check mobile width around 380px.
7. Check print preview.
