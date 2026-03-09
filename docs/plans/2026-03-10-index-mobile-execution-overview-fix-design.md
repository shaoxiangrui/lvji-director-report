# Index Mobile Execution and Overview Fix Design

**Goal:** Fix two mobile-only presentation issues in `/Users/wenjiayan/PycharmProjects/驴迹AI/index.html`: the `03 执行计划` section can appear blank after mobile navigation jumps, and the `00 概览` hero content sits too close to the right edge.

**Problem**

There are two distinct mobile regressions:

1. `03 执行计划` content exists in the DOM, but mobile navigation can land on that section while the section is still in the `.reveal` hidden state.
2. The `00 概览` hero block keeps desktop-oriented copy proportions on phones, so the title and supporting content visually crowd the right edge instead of preserving the same breathing room seen in other sections.

**Root Cause**

- `.reveal` defaults to `opacity: 0` and `transform: translateY(28px)`. Content becomes visible only after the reveal observer adds `.is-visible`.
- On some mobile embedded browsers and anchor-jump paths, the page can move to the target section before that reveal lifecycle produces a visible section, causing a “blank section” impression even though the nav highlights the correct chapter.
- The hero mobile breakpoint currently reduces title size, but does not add a dedicated right-side breathing zone for `.hero-copy`, nor reduce the visual width of the title block.

**Chosen Approach**

Use a mobile-only CSS fix inside the existing `@media (max-width: 760px)` block.

- Disable the section reveal hiding behavior on phones by forcing `.reveal` to stay visible on mobile.
- Keep desktop and tablet reveal behavior unchanged.
- Add mobile-only spacing refinement for the overview hero copy:
  - give `.hero-copy` a small right-side inset
  - slightly tighten the mobile title width
  - keep other panels untouched

**Why This Approach**

- It stays within the requested boundary: mobile styles only.
- It fixes the root cause instead of tuning observer thresholds or adding more JS conditions.
- It keeps the page robust in WeChat-like browsers where animation lifecycle timing is less reliable.
- It solves the overview spacing issue with minimal CSS surface area.

**Verification**

- Open the page in a phone-sized viewport and visit `#execution`; the section should show content immediately rather than appearing blank.
- Open `#overview`; the hero title and copy should keep visible breathing room on the right side, closer to the spacing rhythm of the other sections.
