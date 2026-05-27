# Legibility Standards for ISEF Posters

Used by `scripts/check_legibility.py` to validate the produced poster.

## Font size minimums (at print size, not screen)

| Element | Minimum | Recommended | Rationale |
|---|---|---|---|
| Title | 80 pt | 100-120 pt | Readable from 3 m (judges walking the aisle) |
| Subtitle / authors | 36 pt | 44 pt | Readable from 2 m |
| Section heading | 48 pt | 60 pt | Readable from 1.5 m |
| Body text | 24 pt | 28-32 pt | Readable from 1 m (typical interview distance) |
| Figure caption | 18 pt | 24 pt | Readable when judge leans in (50 cm) |
| References | 14 pt | 18 pt | Smaller is acceptable for the footer |

**Common mistake:** designing on a laptop screen at 100% zoom and not realizing how small
your "body text" looks at full A0 print size. Always preview at print size before printing.

## Color contrast (WCAG 2.1 AA)

| Text type | Min contrast ratio | Why |
|---|---|---|
| Body text on background | 4.5:1 | Color-deficient judges (8% of male population) need it |
| Headings (≥18 pt bold or ≥24 pt regular) | 3:1 | Larger text is more forgiving |
| Decorative / non-essential | — | OK to use lower contrast |

Check with any contrast tool (e.g., webaim.org/resources/contrastchecker).

**Don't:** use light gray text on white. Don't use yellow on white. Don't use red on green
(red-green colorblind judges).

## Image resolution

| Print size | Min DPI | Recommended DPI |
|---|---|---|
| Full-bleed image (covering 30%+ of poster) | 200 | 300 |
| Standard figure (10-25% of poster) | 200 | 300 |
| Inset / detail | 300 | 300 |
| Vector graphics | n/a | use PDF/SVG, never raster |

If your figure is a screenshot, it's almost certainly too low-DPI for poster print. Re-render
from source (matplotlib `dpi=300`; Photoshop "Image Size > Resample"; etc.).

## Layout density

| Region | % of poster real estate |
|---|---|
| Banner (title area) | 8-12% |
| Body text (all sections combined) | 30-40% |
| Figures | 35-45% |
| Whitespace / margins | 10-20% (NEVER zero) |
| References / footer | 5-8% |

**Don't pack to 100%.** Whitespace is what makes a poster scannable. A poster with no
whitespace looks busy and judges won't read it carefully.

## Color palette guidance

ISEF doesn't mandate colors. Sensible defaults:

- 2-3 primary colors max (a brand color + one accent + a neutral)
- One color for headings, one for body, one for highlights (avoid using 5+ colors)
- High-contrast (use the contrast-ratio rule above)
- Category-aligned palettes if you want: PHYS = navy + accent; BIOL = green; CHEM = orange; ROBO = grey
- AVOID rainbow palettes for data unless data is genuinely categorical with no order — use sequential (viridis, magma) for ordinal data

## Title-writing guidance

The title is the most-read element. Rules:

- ≤ 12 words
- States the main finding or the main question, not just the topic area
- "MCMC Sampling of Origami and Linkages" is a *topic*; "Origami Configurations as Statistical Ensembles: A Free-Energy Analysis" is a *finding-as-title*
- Avoid colon-stacking ("X: Y: Z")
- Avoid clickbait phrasing ("How I Discovered...")

## What the validator checks

`scripts/check_legibility.py` runs these automated checks and flags failures:

1. Body font measured ≥ 24 pt at print size — FAIL if smaller
2. Title font measured ≥ 80 pt at print size — FAIL if smaller
3. Margins ≥ 2 cm on all sides — FAIL if smaller (printers eat margin)
4. Image DPI ≥ 200 — WARN if 200-299; FAIL if <200
5. Total file size — INFO (large files take longer to print)
6. Font embedding — FAIL if fonts aren't embedded in PDF (printer may substitute)
7. Color profile — INFO (CMYK preferred for print; RGB will work but may shift)

These are necessary-not-sufficient: passing the validator doesn't mean the poster is good, only
that it won't fail on print-readability grounds.
