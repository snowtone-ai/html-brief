#!/usr/bin/env python3
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

REQUIRED_FILES = [
    "AGENTS.md",
    "CHANGELOG.md",
    "CODEX_EXECUTION_SEQUENCE.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "README.md",
    "REPOSITORY_STRUCTURE.md",
    "scripts/validate.py",
    "skills/html-brief/SKILL.md",
    "skills/html-brief/references/archetype-plan.md",
    "skills/html-brief/references/archetype-compare.md",
    "skills/html-brief/references/archetype-review.md",
    "skills/html-brief/references/archetype-report.md",
    "skills/html-brief/references/archetype-editor.md",
    "skills/html-brief/references/export-bridge.md",
    "skills/html-brief/references/gotchas.md",
    "skills/html-brief/references/design-tokens.md",
    "skills/html-brief/schemas/brief.schema.json",
    "skills/html-brief/schemas/plan.schema.json",
    "skills/html-brief/schemas/compare.schema.json",
    "skills/html-brief/schemas/review.schema.json",
    "skills/html-brief/schemas/report.schema.json",
    "skills/html-brief/schemas/editor.schema.json",
    "skills/html-brief/examples/plan-db-migration/before.md",
    "skills/html-brief/examples/plan-db-migration/output.html",
    "skills/html-brief/examples/plan-db-migration/round-trip.json",
    "skills/html-brief/examples/review-streaming-pr/before.md",
    "skills/html-brief/examples/review-streaming-pr/output.html",
    "skills/html-brief/examples/review-streaming-pr/round-trip.json",
    "skills/html-brief/examples/edit-feature-flags/before.md",
    "skills/html-brief/examples/edit-feature-flags/output.html",
    "skills/html-brief/examples/edit-feature-flags/round-trip.json",
]

CONSTITUTION = [
    "The Reader's Time Is Sacred",
    "Form Follows Information",
    "Communication Is a Loop",
    "Universality",
    "Honesty Over Impression",
    "Adaptability Within Principles",
    "Restraint",
]

EXTERNAL_MARKERS = ["http://", "https://", "cdn.", '<link rel="stylesheet"', "import "]


def fail(message):
    errors.append(message)


def read(path):
    return path.read_text(encoding="utf-8")


for rel in REQUIRED_FILES:
    if not (ROOT / rel).exists():
        fail(f"Missing required file: {rel}")

license_path = ROOT / "LICENSE"
if license_path.exists() and "MIT License" not in read(license_path):
    fail("LICENSE must contain MIT License")

readme_path = ROOT / "README.md"
if readme_path.exists():
    head = "\n".join(read(readme_path).splitlines()[:30]).lower()
    if "what this is not" not in head:
        fail("README must state What this is NOT near the top")

skill_words = []
skill_path = ROOT / "skills/html-brief/SKILL.md"
if skill_path.exists():
    skill = read(skill_path)
    body = re.sub(r"^---\n.*?\n---\n", "", skill, flags=re.S)
    skill_words = re.findall(r"\b[\w'-]+\b", body)
    if not (1500 <= len(skill_words) <= 2000):
        fail(f"SKILL.md body word count outside 1500-2000: {len(skill_words)}")
    for title in CONSTITUTION:
        if title not in skill:
            fail(f"SKILL.md missing Constitution article: {title}")
    if "license: MIT" not in skill:
        fail("SKILL.md frontmatter must declare license: MIT")

schema_dir = ROOT / "skills/html-brief/schemas"
for path in sorted(schema_dir.glob("*.schema.json")):
    try:
        schema = json.loads(read(path))
    except Exception as exc:
        fail(f"Invalid JSON schema {path.relative_to(ROOT)}: {exc}")
        continue
    if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        fail(f"Schema must use draft 2020-12: {path.relative_to(ROOT)}")
    if not schema.get("$id"):
        fail(f"Schema missing $id: {path.relative_to(ROOT)}")
    if schema.get("type") != "object":
        fail(f"Schema root type must be object: {path.relative_to(ROOT)}")
    if schema.get("additionalProperties") is not False:
        fail(f"Schema root must set additionalProperties false: {path.relative_to(ROOT)}")

    def check_properties(node, loc):
        if not isinstance(node, dict):
            return
        props = node.get("properties")
        if isinstance(props, dict):
            for name, prop in props.items():
                if not isinstance(prop, dict):
                    fail(f"Property is not an object at {loc}.{name}")
                    continue
                if not any(k in prop for k in ("type", "$ref", "anyOf", "oneOf")):
                    fail(f"Property missing type/ref/combinator at {loc}.{name}")
                if "description" not in prop:
                    fail(f"Property missing description at {loc}.{name}")
                check_properties(prop, f"{loc}.{name}")
        for key in ("items", "additionalProperties"):
            if isinstance(node.get(key), dict):
                check_properties(node[key], f"{loc}.{key}")
        for key in ("anyOf", "oneOf", "allOf"):
            values = node.get(key, [])
            if isinstance(values, list):
                for item in values:
                    check_properties(item, f"{loc}.{key}")

    check_properties(schema, path.name)

for path in sorted((ROOT / "skills/html-brief/examples").glob("*/round-trip.json")):
    try:
        json.loads(read(path))
    except Exception as exc:
        fail(f"Invalid example JSON {path.relative_to(ROOT)}: {exc}")

for path in sorted((ROOT / "skills/html-brief/examples").glob("*/output.html")):
    html = read(path)
    lower = html.lower()
    rel = path.relative_to(ROOT)
    for marker in ["<!doctype html>", '<html lang="en"', "<style>", "<script"]:
        if marker not in lower:
            fail(f"Missing {marker}: {rel}")
    for label in ["Copy as Prompt", "Copy as JSON", "Copy as Markdown"]:
        if label not in html:
            fail(f"Missing {label}: {rel}")
    if "brief-initial-state" not in html and "brief-state" not in html:
        fail(f"Missing embedded state script: {rel}")
    if re.search(r"@media\s*\(\s*prefers-color-scheme\s*:\s*dark\s*\)", html) is None:
        fail(f"Missing dark mode media query: {rel}")
    if "@media print" not in html:
        fail(f"Missing print media query: {rel}")
    for marker in EXTERNAL_MARKERS:
        if marker in lower:
            fail(f"External dependency marker {marker!r} in {rel}")

review_html = ROOT / "skills/html-brief/examples/review-streaming-pr/output.html"
if review_html.exists() and "Copy as Review Comments" not in read(review_html):
    fail("Review example must include Copy as Review Comments")

editor_html = ROOT / "skills/html-brief/examples/edit-feature-flags/output.html"
if editor_html.exists() and "Reset" not in read(editor_html):
    fail("Editor example must include Reset")

if errors:
    print("Validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("Validation passed.")
print(f"SKILL.md body word count: {len(skill_words)}")
