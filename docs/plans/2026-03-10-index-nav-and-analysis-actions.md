# Index Navigation and Analysis Action Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Fix the navigation active-state race in `/Users/wenjiayan/PycharmProjects/驴迹AI/index.html` and redesign the `定位分析` / `返回报告` controls so they are clearly recognizable buttons across desktop and mobile.

**Architecture:** Keep the existing section observer and active-link system, but add a lightweight pending-target layer that temporarily prioritizes explicit user chapter selection during smooth scrolling. Update the two button DOM structures to support clearer hierarchy and redesign their shared styles without changing modal semantics.

**Tech Stack:** Single-file HTML, CSS, vanilla JavaScript

---

### Task 1: Document the approved solution

**Files:**
- Create: `/Users/wenjiayan/PycharmProjects/驴迹AI/docs/plans/2026-03-10-index-nav-and-analysis-actions-design.md`
- Create: `/Users/wenjiayan/PycharmProjects/驴迹AI/docs/plans/2026-03-10-index-nav-and-analysis-actions.md`

**Step 1: Capture the nav root cause**

- Note the race between click intent and viewport sync during smooth anchor scrolling.

**Step 2: Capture the button redesign direction**

- Note that both actions remain native buttons but gain stronger editorial CTA styling.

### Task 2: Implement the nav active-state fix

**Files:**
- Modify: `/Users/wenjiayan/PycharmProjects/驴迹AI/index.html`

**Step 1: Add pending nav state**

- Introduce a short-lived pending target id and timeout.
- Ensure it is set when a nav item is clicked or when hash-based chapter navigation is intentionally triggered.

**Step 2: Integrate pending state into viewport sync**

- If a pending target exists and the page is still transitioning, keep the clicked target active.
- Clear pending state once the destination section becomes stably visible.

### Task 3: Redesign the analysis buttons

**Files:**
- Modify: `/Users/wenjiayan/PycharmProjects/驴迹AI/index.html`

**Step 1: Update button markup**

- Add richer inner structure for `定位分析` with `点击查看` support text and a directional icon.
- Add richer inner structure for `返回报告` with a back icon and supporting copy.

**Step 2: Update shared styles**

- Replace the current pill-like presentation with clearer CTA styling.
- Keep the same styles working on both desktop and mobile.

### Task 4: Verify the behavior

**Files:**
- Verify: `/Users/wenjiayan/PycharmProjects/驴迹AI/index.html`

**Step 1: Reproduce nav intent**

- Simulate or instrument the `#strategy` click path and confirm the atlas remains on `01 战略定位` during the jump.

**Step 2: Review button affordance**

- Capture strategy-section and modal-open previews.
- Confirm both actions read as buttons at a glance.
