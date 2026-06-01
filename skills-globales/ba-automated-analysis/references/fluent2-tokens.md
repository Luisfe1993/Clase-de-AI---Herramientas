# Fluent 2 Dashboard Tokens

Design tokens for generating HTML dashboards. The AI generates the full dashboard HTML dynamically -- there is no template file to populate.

## Color Palette

| Token | Hex | Usage |
|---|---|---|
| Background | `#f5f5f5` | Page background |
| Surface | `#ffffff` | Cards, header, footer |
| Text primary | `#242424` | KPI values, body text |
| Text secondary | `#616161` | Labels, metadata |
| Brand | `#0f6cbd` | Headers, accent, insight numbering |
| Stroke | `#d1d1d1` | Card borders, table borders |
| Positive | `#0e7a0d` | Positive deltas |
| Negative | `#b10e1c` | Negative deltas |

## Chart Palette (6 colors, in order)

`#0f6cbd` (blue), `#c239b3` (magenta), `#f7630c` (orange), `#00b7c3` (teal), `#8764b8` (purple), `#e3008c` (pink)

Use `cc` suffix for 80% opacity fills (e.g., `#0f6cbdcc`). Use `1a` suffix for light area fills.

## Typography & Spacing

- **Font:** `'Segoe UI Variable', 'Segoe UI', sans-serif`
- **Border radius:** `8px` on all cards
- **Spacing grid:** 4px base (8, 16, 24, 32, 48)
- **Max width:** `1280px`, centered

## Dashboard Structure

Generate a self-contained HTML file with Chart.js 4.x from CDN. Include these sections in order:

1. **Header** -- analysis title, snapshot date, model name
2. **KPI strip** -- 3-4 cards (label, value, delta with up/down triangle)
3. **Charts** -- responsive grid, adapt chart count to analysis needs (not fixed at 2)
4. **Data table** -- sortable, right-aligned numerics, bold primary metric column
5. **Key insights** -- numbered list, 3-6 findings, bold the so-what
6. **Methodology footer** -- tests used, data scope, caveats

## Key Rules

- Self-contained: all CSS inline, Chart.js from CDN
- Responsive: 2-column charts at 768px+, single column below
- Print-friendly: white background, no shadows, `break-inside: avoid`
- Accessible: semantic HTML, `role="img"` on canvas, WCAG AA contrast
- KPI deltas: `&#9650;` (up), `&#9660;` (down), `&#9644;` (flat)
