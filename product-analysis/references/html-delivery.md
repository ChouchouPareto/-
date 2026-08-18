# HTML Delivery

Read this reference whenever the deliverable creates or edits HTML.

## Required Skill

Load `ui-ux-pro-max` before taking HTML design actions. Tell the user why it is being used. Follow its current instructions for accessibility, responsive behavior, typography, color, interaction, and final checks.

## Report Design

- Prefer a self-contained HTML file with no mandatory network dependencies.
- Follow the user’s visual direction. If none is given, use a high-contrast evidence-workbench style suitable for dense tables and diagrams.
- Carry forward explicit visual feedback within the same product-analysis project. For example, if the user says a prior report is too white, do not silently revert to a white-first visual direction in the next report.
- Use semantic color tokens. Never rely on color alone: pair status colors with visible labels.
- Provide a skip link, logical headings, keyboard-visible focus, semantic buttons, and reduced-motion support.
- Keep pointer targets usable and copy buttons at least 44px high.
- Make navigation sticky only when it does not obscure focused content.
- Make large tables and code/diagram sources horizontally scrollable without breaking the viewport.
- Preserve readable body size on mobile and use responsive grids.

## Evidence Navigation

- Link every screenshot/page ID to the local evidence file when available.
- Use relative links inside portable report folders; use absolute links only in the final chat response.
- Add a scope/evidence index and keep conflict labels visible near affected claims.
- Do not embed sensitive data or inaccessible private URLs.

## Diagrams

- Provide accessible text/table alternatives for critical diagrams.
- Mermaid source may be included directly for portability; do not require a remote CDN merely to read the report.
- Label line semantics and add legends.
- For architecture panoramas, show components, key data/state flow, and current failure points—not components alone.

## Validation

Run the included validator:

```bash
python3 scripts/validate_html_report.py report.html
```

Then manually verify:

- Required stage sections and ordering
- Correct evidence labels and links
- No duplicate IDs or missing anchors
- No unfinished placeholders or TODOs
- JavaScript syntax when scripts are present
- CSS brace balance
- Responsive layouts at narrow and wide widths when a renderer is available
- Print behavior when the report is expected to be printed
- The final response names the exact absolute output path and provides a clickable local-file link
