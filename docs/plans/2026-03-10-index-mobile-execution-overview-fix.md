# Index Mobile Execution and Overview Fix Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Apply a mobile-only CSS fix in `/Users/wenjiayan/PycharmProjects/驴迹AI/index.html` so `03 执行计划` always renders visibly on phones and `00 概览` gains proper right-side breathing room.

**Architecture:** Keep the existing HTML and JS intact. Solve both issues in the `@media (max-width: 760px)` block: override `.reveal` to remain visible on mobile, then tighten the overview hero copy geometry with small spacing adjustments.

**Tech Stack:** Single-file HTML, CSS

---

### Task 1: Document the mobile-only fix

**Files:**
- Create: `/Users/wenjiayan/PycharmProjects/驴迹AI/docs/plans/2026-03-10-index-mobile-execution-overview-fix-design.md`
- Create: `/Users/wenjiayan/PycharmProjects/驴迹AI/docs/plans/2026-03-10-index-mobile-execution-overview-fix.md`

**Step 1: Capture root cause**

- Note that `.reveal` hides sections until intersection-driven activation.
- Note that the overview hero lacks mobile-specific right-side spacing refinement.

**Step 2: Capture fix strategy**

- Document that the change is CSS-only and mobile-only.
- Document that desktop behavior remains unchanged.

### Task 2: Apply the mobile CSS fix

**Files:**
- Modify: `/Users/wenjiayan/PycharmProjects/驴迹AI/index.html`

**Step 1: Make mobile sections visible by default**

- In the `@media (max-width: 760px)` block, override `.reveal` to `opacity: 1`, `transform: none`, and remove transition.

**Step 2: Refine overview spacing**

- Add mobile-only spacing adjustments for `#overview .hero-copy`.
- Slightly narrow the mobile `#overview .hero-title` width so it stops visually pressing against the right side.

### Task 3: Verify mobile rendering

**Files:**
- Verify: `/Users/wenjiayan/PycharmProjects/驴迹AI/index.html`

**Step 1: Check `#overview`**

- Confirm the hero title and definition card keep visible right-side space.

**Step 2: Check `#execution`**

- Confirm the execution section renders visible content immediately on mobile-sized navigation.

**Step 3: Record evidence**

- Capture screenshots for both anchors after the change.
