# Index Navigation and Analysis Action Design

**Goal:** Fix the navigation active-state mismatch in `/Users/wenjiayan/PycharmProjects/驴迹AI/index.html` and redesign the `定位分析` / `返回报告` actions so they read as obvious interactive buttons on both desktop and mobile.

**Problem**

Two interaction issues remain:

1. When a user taps a navigation item such as `01 战略定位`, the floating atlas can briefly revert to `00 概览` even though the user clearly chose another chapter.
2. The `定位分析` trigger and the modal close action are visually too close to decorative pills, so users do not immediately recognize them as buttons.

**Root Cause**

- Navigation currently has two competing sources of truth:
  - click intent sets the active link immediately
  - viewport sync recalculates active state from the current scroll position
- During smooth anchor navigation, viewport sync runs before the scroll reaches the new section, so the previous section still wins the calculation.
- The analysis actions rely on soft pill styling with secondary labels like `Focus` / `Exit`, but they lack stronger affordance cues such as hierarchical text, directional iconography, and a denser “action surface” treatment.

**Chosen Approach**

### Navigation

Introduce a short-lived pending navigation target.

- When a user clicks a chapter link, store the clicked target as the preferred active section.
- While the page is still transitioning toward that chapter, the atlas keeps showing the user’s chosen target instead of falling back to the old viewport section.
- Once the target reaches a stable visible position, clear the pending state and return control to viewport-based syncing.

### Analysis Actions

Upgrade both actions into clearly intentional buttons.

- `定位分析` becomes a stronger primary editorial action:
  - visible two-line copy
  - secondary cue: `点击查看`
  - directional icon on the right
- `返回报告` becomes a clear return action:
  - leading back arrow
  - stronger button surface
  - optional secondary hint reinforcing that it closes the analysis layer and returns to the report

**Visual Direction**

Stay inside the existing boardroom-paper system, but make these controls feel like “decision tools” rather than labels:

- warmer layered paper surfaces
- clearer inner border and contrast separation
- stronger hover lift
- directional icon chips
- compact editorial typography hierarchy

**Accessibility**

- Keep native `<button>` elements.
- Ensure visible text remains the accessible name source.
- Preserve current focus ring behavior and modal focus restoration.
- Decorative icon spans remain `aria-hidden="true"`.

**Implementation Scope**

- Modify `/Users/wenjiayan/PycharmProjects/驴迹AI/index.html`
  - JS: pending-target navigation state
  - HTML: richer button content structure
  - CSS: shared desktop/mobile button redesign

**Verification**

- Reproduce the click path to `01 战略定位` and confirm the atlas does not immediately fall back to `00 概览`.
- Visually inspect the strategy trigger and the modal close action to confirm both are unmistakably buttons.
