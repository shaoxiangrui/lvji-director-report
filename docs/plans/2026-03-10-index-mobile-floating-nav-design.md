# Index Mobile Floating Navigation Design

**Goal:** Fix the mobile navigation in `/Users/wenjiayan/PycharmProjects/驴迹AI/index.html` so it no longer occupies the first screen. The nav should shrink into a floating atlas control that stays available without covering the report content.

**Problem**

The current responsive layout collapses `.atlas-shell` to one column below `1080px`, but leaves `.atlas-nav` as a full document block before `<main>`. On phones this causes the first viewport to be dominated by the navigation card, pushing the actual report below the fold. The sticky behavior also keeps the nav visually heavy instead of acting like a compact aid.

**Constraints**

- Desktop and tablet layouts should remain visually unchanged.
- Mobile navigation must still expose all section anchors.
- The control must not permanently obscure report content.
- Touch targets and focus behavior must remain usable in mobile browsers, including embedded browsers like WeChat.

**Chosen Approach**

Use a compact floating atlas on small screens (`<= 760px`) instead of a full-width stacked navigation block.

- Keep the existing `<aside>` and anchor list so document structure and active-link logic remain intact.
- Add a dedicated mobile toggle button inside the nav header.
- In the mobile breakpoint, move the nav out of the normal flow with `position: fixed` and anchor it near the bottom-right safe area.
- Default state is collapsed:
  - shows a small badge-like control
  - displays the current section label
  - takes minimal visual space
- Expanded state opens an internal panel with the full chapter list.
- When a nav link is tapped on mobile, the panel closes automatically after the hash navigation is triggered.

**Why This Approach**

- It directly solves the first-screen blockage instead of merely shrinking padding.
- It preserves the “Boardroom Atlas” design language better than a generic top bar or bottom tab bar.
- It minimizes HTML churn by reusing the current nav structure and active-state JS.
- It keeps the report feeling like a presentation artifact, not an app shell.

**Visual Direction**

- Retain the existing warm paper palette and soft glassmorphism card treatment.
- Mobile nav becomes a miniature floating card rather than a hard system sheet.
- Use real responsive sizing with `clamp()` and breakpoint-specific spacing instead of `transform: scale()`, which would blur text and reduce usable tap targets.

**Interaction Model**

- Mobile toggle button opens and closes the floating panel.
- Nav has two mobile states:
  - collapsed: compact chip/card
  - expanded: full mini-panel with scrollable list
- Clicking outside the nav closes it.
- Pressing `Escape` closes it when supported.
- Selecting a section closes the nav and preserves the current active-link highlighting.

**Accessibility**

- Use a native `<button>` for the mobile toggle.
- Toggle exposes `aria-expanded` and `aria-controls`.
- Focus styles remain visible.
- Minimum touch target size should stay at or above 44px.
- The aside retains `aria-label="章节导航"`.

**Implementation Scope**

- Modify `/Users/wenjiayan/PycharmProjects/驴迹AI/index.html`
  - HTML: add mobile toggle affordance and current-section summary node
  - CSS: add mobile floating/collapsed/expanded nav styles
  - JS: add mobile open/close state management and auto-close on link selection

**Verification**

- Preview on a phone-sized viewport.
- Confirm the first screen shows the hero content instead of a full navigation slab.
- Confirm the floating nav does not cover critical report content by default.
- Confirm nav can open, navigate, highlight active section, and close correctly.
