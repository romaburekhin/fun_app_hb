# Website Design Recreation

Recreate website designs from reference images using Tailwind CSS with iterative screenshot comparison.

## Quick Start

1. User provides reference image + optional CSS notes
2. Generate `index.html` with Tailwind CDN
3. Screenshot with Puppeteer → Compare → Fix → Repeat
4. Iterate until within ~2-3px match

## Rules

Organized in `rules/`:

- **[workflow.md](rules/workflow.md)** - 6-step iterative process
- **[technical-defaults.md](rules/technical-defaults.md)** - Tech stack (Tailwind CDN, placeholders, responsive)
- **[matching-rules.md](rules/matching-rules.md)** - Design matching guidelines (no improvements, exact matching)
- **[comparison-checklist.md](rules/comparison-checklist.md)** - What to check when comparing screenshots

## Key Principles

- Match reference exactly — do not add features or "improve" design
- Minimum 2 comparison rounds — do not stop after first pass
- Measure precisely — report specific px differences
- Iterate until user approves or no differences remain
