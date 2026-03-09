# LVJI Navigation Active-State Consistency Design

## Context

`lvji-director-report.html` already uses one shared navigation state machine:

- `setActiveLink(id)` toggles `.is-active` on all `.atlas-link` entries.
- `syncActiveLinkWithViewport()` keeps the active entry aligned with scroll position.
- Click, hash-change, resize, and intersection events all route through the same logic.

The inconsistency is visual, not behavioral. The `execution` item has its own active-state CSS, so one navigation entry renders differently even though every entry is activated by the same logic.

## Approaches Considered

### 1. Remove the `execution` special-case styles

Delete the selectors that target `.atlas-link[data-nav-target="execution"].is-active` and keep the shared `.atlas-link:hover, .atlas-link.is-active` rule as the only active-state styling.

Trade-off:
- Smallest change and lowest regression risk.
- Keeps behavior untouched.
- Matches the requirement exactly: all navigation items share one active style.

### 2. Promote the `execution` style into a shared active-state theme

Move the stronger gradient/border treatment into the common active-state rule so every item uses the current `execution` look.

Trade-off:
- Still consistent, but changes the visual system more broadly.
- Higher risk of unintended layout or readability changes.

### 3. Introduce active-state design tokens first, then refactor

Create dedicated CSS variables for active border, background, and pill styling before removing the one-off selector.

Trade-off:
- Better for larger future refactors.
- Too heavy for a one-file consistency fix.

## Approved Design

Use approach 1.

- Keep the current navigation logic unchanged.
- Remove the `execution`-only active-state selectors.
- Leave the shared `.atlas-link:hover, .atlas-link.is-active` rule as the single source of truth for nav highlighting.
- Preserve all existing labels, anchors, and viewport-sync behavior.

## Verification Strategy

Because this is a standalone HTML file without an automated UI test harness, verification is source-based:

- Confirm the shared `.atlas-link.is-active` rule still exists.
- Confirm no `execution`-specific active-state selectors remain.
- Review the resulting diff to ensure only the intended CSS was removed.
