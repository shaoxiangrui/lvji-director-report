# Index Mobile Floating Navigation Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Convert the mobile navigation in `/Users/wenjiayan/PycharmProjects/驴迹AI/index.html` into a compact floating atlas that preserves navigation access without blocking the report content.

**Architecture:** Keep the existing aside/list anchor structure and active-section observer, then layer a mobile-only collapsed/expanded interaction model on top. CSS handles the responsive floating shell and panel states; a small JS state machine controls open/close behavior and keeps the current section label in sync.

**Tech Stack:** Single-file HTML, CSS, vanilla JavaScript

---

### Task 1: Add mobile navigation structure hooks

**Files:**
- Modify: `/Users/wenjiayan/PycharmProjects/驴迹AI/index.html`

**Step 1: Add a mobile nav status row**

- Insert a compact status region inside `.atlas-nav` that can display the current active section on mobile.
- Add a real `<button>` toggle with stable selectors for JS control.

**Step 2: Keep desktop structure intact**

- Ensure the new elements do not change the desktop navigation layout.
- Reuse current text labels instead of duplicating content in JS where possible.

### Task 2: Implement the mobile floating navigation styling

**Files:**
- Modify: `/Users/wenjiayan/PycharmProjects/驴迹AI/index.html`

**Step 1: Define mobile-only collapsed state**

- At `@media (max-width: 760px)`, move `.atlas-nav` to a fixed floating position.
- Reduce width, padding, and visual density while preserving the existing visual language.

**Step 2: Define mobile-only expanded state**

- Add styles for an expanded nav panel using an `.is-open` class.
- Make the section list internally scrollable if needed.

**Step 3: Protect readability and touch ergonomics**

- Keep minimum touch targets >= 44px.
- Make sure the collapsed control does not obscure the hero title or central content.

### Task 3: Implement JS state management

**Files:**
- Modify: `/Users/wenjiayan/PycharmProjects/驴迹AI/index.html`

**Step 1: Wire toggle behavior**

- Query the new toggle button and current-section label node.
- Add open/close helpers that synchronize CSS classes and `aria-expanded`.

**Step 2: Sync current section label**

- Reuse active-link detection to update the mobile summary label with the current section text.

**Step 3: Add close triggers**

- Close on nav link click for mobile.
- Close on outside click.
- Close on `Escape`.
- Ensure desktop behavior is unaffected.

### Task 4: Verify the mobile experience

**Files:**
- Verify: `/Users/wenjiayan/PycharmProjects/驴迹AI/index.html`

**Step 1: Load the page locally in a mobile-sized browser**

Run a local server or open the file in a browser.

**Step 2: Validate the first screen**

- The first viewport should show the report hero, not a full navigation slab.
- The floating nav should appear as a compact overlay near the bottom-right.

**Step 3: Validate interactions**

- Toggle opens and closes cleanly.
- Tapping a section navigates and collapses the panel.
- Active section state still updates during scroll.

**Step 4: Capture evidence**

- Take mobile screenshots before/after if needed.
- Record any residual overlap risks near the viewport safe area.
