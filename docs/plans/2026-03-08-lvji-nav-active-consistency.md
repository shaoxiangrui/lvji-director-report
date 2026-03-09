# LVJI Navigation Active-State Consistency Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Make every navigation item in `lvji-director-report.html` use the same active-state styling while keeping the current click and scroll-sync behavior unchanged.

**Architecture:** This is a CSS-only change in a standalone HTML file. Navigation state already flows through `setActiveLink()` and `syncActiveLinkWithViewport()`, so implementation only removes the `execution`-specific active selectors and relies on the existing shared `.atlas-link.is-active` rule.

**Tech Stack:** Static HTML, CSS, vanilla JavaScript

---

### Task 1: Remove the `execution` active-state special case

**Files:**
- Modify: `lvji-director-report.html`
- Reference: `docs/plans/2026-03-08-lvji-nav-active-consistency-design.md`

**Step 1: Confirm the current special-case selectors**

Run:

```bash
rg -n 'data-nav-target="execution".*is-active|execution"].is-active .nav-index|execution"].is-active .priority-pill' lvji-director-report.html
```

Expected:
- Three matches that define the `execution`-only active-state styling.

**Step 2: Remove the special-case CSS**

Delete these selectors from `lvji-director-report.html`:

```css
.atlas-link[data-nav-target="execution"].is-active
.atlas-link[data-nav-target="execution"].is-active .nav-index
.atlas-link[data-nav-target="execution"].is-active .priority-pill
```

Keep the shared rule:

```css
.atlas-link:hover,
.atlas-link.is-active
```

**Step 3: Verify the special-case selectors are gone**

Run:

```bash
rg -n 'data-nav-target="execution".*is-active|execution"].is-active .nav-index|execution"].is-active .priority-pill' lvji-director-report.html
```

Expected:
- No matches.

**Step 4: Verify the shared active-state rule still exists**

Run:

```bash
rg -n '\.atlas-link:hover|\.atlas-link\.is-active' lvji-director-report.html
```

Expected:
- The shared hover/active rule is still present.

**Step 5: Review the diff**

Run:

```bash
git diff -- docs/plans/2026-03-08-lvji-nav-active-consistency-design.md docs/plans/2026-03-08-lvji-nav-active-consistency.md lvji-director-report.html
```

Expected:
- Two new plan documents.
- One CSS-only change removing the `execution` active-style override.
