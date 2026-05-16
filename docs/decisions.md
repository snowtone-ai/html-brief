# decisions.md

## D-001: pm-zero v9.4 Lean Task Ledger alignment

- Date: 2026-05-16
- Decision: Add pm-zero ledger, state, handoff, and repository map files while preserving the existing skill/source contract.
- Rationale: html-brief already has a strong product source-of-truth order; pm-zero adds execution state without redefining product behavior.
- Consequence: Product source precedence remains in AGENTS.md and validation remains scripts/validate.py.
