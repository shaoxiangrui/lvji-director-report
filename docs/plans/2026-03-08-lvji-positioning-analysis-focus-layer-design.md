# LVJI Positioning Analysis Focus Layer Design

## Context

`lvji-director-report.html` already contains a `定位分析` entry point and basic dialog wiring:

- `data-modal-open` opens the layer
- `data-modal-close` closes it
- `data-modal-overlay` closes on backdrop click
- `Escape` closes the dialog
- focus returns to the triggering button

What is missing is a strong visual treatment and a content structure that matches the rest of the boardroom-style report. The current implementation reads like a plain modal stub: weak hierarchy, no fixed reading frame, and no clear full-screen focus state.

## Design Direction

Use a full-screen focus layer that feels like a separate boardroom briefing sheet placed above the report.

The visual direction stays within the existing design system:

- paper-toned surfaces instead of pure white
- ink green as the dominant signal color
- brass/gold as the decision highlight
- soft blur and atmospheric gradients instead of flat overlays
- serif headings and mono labels to preserve the editorial boardroom voice

The memorable element is the shift from “utility modal” to “strategic memo layer”: when opened, the background report falls away and the positioning analysis becomes the single focal artifact on screen.

## Information Architecture

The focus layer has three fixed bands:

1. Top bar
- section label
- long-form title
- short framing paragraph
- close action

2. Scrollable analysis body
- a summary board with the headline conclusion and three condensed decision signals
- a two-column grid of dimension cards
- each card contains:
  - dimension heading
  - preferred direction
  - alternative direction
  - annual verdict

3. Bottom verdict strip
- one-line board-level recommendation
- supporting note that this is a sequencing decision, not a permanent exclusion

## Interaction Model

- Clicking `定位分析` opens the focus layer.
- Background scroll is locked while the layer is open.
- The underlying report visually softens with blur and reduced opacity.
- Focus lands on the close button when opened.
- `Escape` closes the layer.
- Backdrop click closes the layer.
- `Tab` navigation is trapped inside the layer while open.
- Closing restores focus to the original trigger.
- The scrollable body resets to the top when reopened.

## Layout Behavior

Desktop:

- dialog fills most of the viewport with comfortable outer margins
- top bar and footer remain fixed inside the dialog shell
- only the content zone scrolls
- summary board uses an asymmetric two-column composition
- analysis cards render in a two-column grid

Mobile:

- dialog becomes a true edge-to-edge full-screen layer
- outer padding collapses
- top bar stacks vertically
- summary board and cards collapse to one column
- the close action remains visible without requiring a long upward scroll

## Visual Components

### Trigger Button

Upgrade the `定位分析` button so it visually belongs with the rest of the boardroom system:

- pill shape
- subtle gradient wash
- hover lift
- clearer focus ring

### Focus Layer Shell

- full-screen fixed container
- multi-layer atmospheric overlay
- large rounded dialog on desktop
- flush full-height shell on small screens
- entry animation: fade + slight upward settle

### Summary Board

- one lead card with the central recommendation
- three compact signal cards summarizing why the preferred direction wins

### Analysis Cards

- each dimension becomes a self-contained card
- preferred and alternative paths are visually separated by tint
- verdict block uses the strongest accent treatment

## Validation

The implementation is correct when:

- the focus layer is visually distinct and cohesive with the existing page
- the layer behaves as a full-screen reading surface, not as a small popup
- all open/close paths work
- focus is managed predictably
- the static HTML test suite reflects the new structure and passes
