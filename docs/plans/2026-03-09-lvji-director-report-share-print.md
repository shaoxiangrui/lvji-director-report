# Lvji Director Report Share + Print Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Make `lvji-director-report.html` friendlier for PDF export and publish it as a minimal public static page on Vercel.

**Architecture:** Keep the report as a single self-contained HTML file. Add print-specific CSS and small shareability metadata inside the page, then constrain deployment using `.vercelignore` and `vercel.json` so only the report and deployment config are exposed.

**Tech Stack:** Single-file HTML/CSS/JS, Vercel static hosting, `.vercelignore`, `vercel.json`

---

### Task 1: Add print-friendly report behavior

**Files:**
- Modify: `/Users/wenjiayan/PycharmProjects/驴迹AI/lvji-director-report.html`

**Step 1: Add share metadata and accessibility hook**

- Add `meta description` and OG metadata in `<head>`.
- Add a skip link as the first focusable element.
- Add `id="main-content"` to `<main>`.

**Step 2: Add print CSS**

- Add `@page` and `@media print` rules.
- Hide sticky nav, modal, animation layers, and decorative map.
- Flatten gradients/shadows to paper-like styles.
- Add break control for sections, cards, table rows, and roadmap rows.

**Step 3: Keep screen behavior intact**

- Do not change current section anchors, modal behavior, or mobile layout.
- Keep print overrides isolated under `@media print`.

### Task 2: Add minimal public deployment config

**Files:**
- Create: `/Users/wenjiayan/PycharmProjects/驴迹AI/vercel.json`
- Create: `/Users/wenjiayan/PycharmProjects/驴迹AI/.vercelignore`
- Create: `/Users/wenjiayan/PycharmProjects/驴迹AI/docs/lvji-director-report-vercel-publish.md`

**Step 1: Constrain deployment scope**

- Allowlist only the report HTML and Vercel config.
- Prevent `docs/`, `tests/`, `.idea/`, local scripts, and other artifacts from being deployed.

**Step 2: Add routing**

- Route `/` to `lvji-director-report.html`.
- Route `/report` to `lvji-director-report.html`.
- Keep `cleanUrls` enabled so `/lvji-director-report` also works.

**Step 3: Document operator flow**

- Write a short publish guide covering:
  - Vercel dashboard setup
  - expected public URLs
  - update and re-release flow
  - custom domain option

### Task 3: Verify the deliverable

**Files:**
- Verify: `/Users/wenjiayan/PycharmProjects/驴迹AI/lvji-director-report.html`
- Verify: `/Users/wenjiayan/PycharmProjects/驴迹AI/vercel.json`
- Verify: `/Users/wenjiayan/PycharmProjects/驴迹AI/.vercelignore`
- Verify: `/Users/wenjiayan/PycharmProjects/驴迹AI/docs/lvji-director-report-vercel-publish.md`

**Step 1: Validate config and file presence**

- Parse `vercel.json` as JSON.
- Confirm `.vercelignore` contains an allowlist.

**Step 2: Validate printable output**

- Generate a PDF from the local HTML using a headless browser if available.
- Confirm the PDF file is created and non-empty.

**Step 3: Validate requirement coverage**

- Re-read the original request and check both requested outputs:
  - HTML adjusted for PDF export
  - sharable static publish scheme delivered
