# LVJI Positioning Analysis Focus Layer Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Replace the weak `定位分析` modal in `lvji-director-report.html` with a full-screen focus layer that matches the page’s boardroom aesthetic and preserves reliable open/close behavior.

**Architecture:** Keep the existing vanilla-JS modal entry points and accessibility hooks, but rebuild the visual shell and content structure around a fixed-header, scroll-body, fixed-footer layout. Update the static HTML tests first so they describe the new focus-layer structure, then implement only the HTML/CSS/JS needed to satisfy those expectations.

**Tech Stack:** Static HTML, CSS, vanilla JavaScript, Python `unittest`

---

### Task 1: Update the tests to define the new focus-layer contract

**Files:**
- Modify: `tests/test_lvji_director_report_html.py`
- Reference: `docs/plans/2026-03-08-lvji-positioning-analysis-focus-layer-design.md`

**Step 1: Replace stale navigation styling expectation**

Update the test marker list so it expects the shared `.atlas-link.is-active` rule instead of the removed `execution`-specific active-state selector.

**Step 2: Add new focus-layer structure markers**

Add assertions for:

```text
strategy-analysis-scroll
analysis-summary-board
analysis-card-grid
analysis-focus-card
analysis-card-verdict
strategy-analysis-footer
```

**Step 3: Add interaction markers for the stronger modal behavior**

Add assertions for:

```text
body.modal-open
const getStrategyAnalysisFocusableElements = ()
event.key === "Tab"
data-modal-scroll
```

**Step 4: Run the test suite and confirm it fails for the missing focus-layer markers**

Run:

```bash
python3 -m unittest -q tests/test_lvji_director_report_html.py
```

Expected:
- FAIL because the new focus-layer markers do not exist yet.

### Task 2: Rebuild the positioning analysis as a full-screen focus layer

**Files:**
- Modify: `lvji-director-report.html`
- Reference: `docs/plans/2026-03-08-lvji-positioning-analysis-focus-layer-design.md`

**Step 1: Upgrade the trigger button styling**

Add production styling for `.strategy-analysis-button` so the entry point matches the current boardroom UI.

**Step 2: Add the full-screen shell styles**

Implement CSS for:

```text
body.modal-open
.strategy-analysis-modal
.strategy-analysis-overlay
.strategy-analysis-dialog
.strategy-analysis-topbar
.strategy-analysis-scroll
.strategy-analysis-footer
```

The dialog must:
- fill most of the viewport on desktop
- become edge-to-edge on mobile
- keep header/footer fixed inside the shell
- make only the central body scroll

**Step 3: Replace the table-like content structure**

Refactor the existing `analysis-table` rows into:

- one summary board
- one two-column grid of focus cards
- one footer verdict strip

Preserve the existing business content and annual judgments.

**Step 4: Strengthen modal behavior**

Extend the existing JS so the focus layer:
- resets internal scroll position on open
- traps focus with `Tab`
- still supports close button, overlay click, and `Escape`
- restores focus to the trigger on close

### Task 3: Verify the implementation

**Files:**
- Verify: `tests/test_lvji_director_report_html.py`
- Verify: `lvji-director-report.html`

**Step 1: Run the HTML tests**

Run:

```bash
python3 -m unittest -q tests/test_lvji_director_report_html.py
```

Expected:
- OK

**Step 2: Run a quick JS syntax validation**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
import re

text = Path("lvji-director-report.html").read_text(encoding="utf-8")
script = re.search(r"<script>(.*)</script>", text, re.S)
assert script, "script block missing"
print("script block found:", len(script.group(1)) > 0)
PY
```

Expected:
- script block found: True

**Step 3: Review the diff**

Run:

```bash
git diff -- docs/plans/2026-03-08-lvji-positioning-analysis-focus-layer-design.md docs/plans/2026-03-08-lvji-positioning-analysis-focus-layer.md tests/test_lvji_director_report_html.py lvji-director-report.html
```

Expected:
- new design doc and implementation plan
- updated tests for the new focus layer
- HTML/CSS/JS changes limited to the positioning analysis area and shared modal behavior
