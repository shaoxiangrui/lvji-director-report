# Lvji OST Executive Flowchart Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Restyle the Opportunity Solution Tree as a director-facing flowchart while preserving the existing content and Boardroom Atlas palette.

**Architecture:** Replace the current four-column grouped-card OST with a flowchart-oriented layout: one target node on the left and four pathway rows on the right. Keep the content text unchanged, but change the HTML structure and CSS classes so the block reads as a strategy flow diagram rather than a column board.

**Tech Stack:** HTML5, CSS3, vanilla JavaScript, Python `unittest`

---

### Task 1: Add failing tests for flowchart-specific markers

**Files:**
- Modify: `/Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py`
- Test: `/Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py`

**Step 1: Write the failing test**

Add expectations for:
- `ost-flowchart`
- `ost-target-node`
- `ost-pathway`
- `ost-node`
- `ost-arrow`

**Step 2: Run test to verify it fails**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py -v`  
Expected: FAIL because the current OST still uses the old grouped-column structure

**Step 3: Write minimal implementation**

Update the OST structure and classes to the flowchart layout.

**Step 4: Run test to verify it passes**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py -v`  
Expected: PASS

### Task 2: Implement Executive Flowchart styling

**Files:**
- Modify: `/Users/wenjiayan/PycharmProjects/驴迹AI/lvji-director-report.html`
- Test: `/Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py`

**Step 1: Write the failing test**

Add expectations for:
- a target node marker
- pathway rows
- explicit arrow markers
- a flowchart wrapper class

**Step 2: Run test to verify it fails**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py -v`  
Expected: FAIL on missing flowchart markers

**Step 3: Write minimal implementation**

Implement:
- target node shell
- pathway rows
- node styles for opportunity / solution / experiment
- arrow connectors
- responsive fallback

**Step 4: Run test to verify it passes**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py -v`  
Expected: PASS

### Task 3: Final verification

**Files:**
- Verify: `/Users/wenjiayan/PycharmProjects/驴迹AI/lvji-director-report.html`
- Verify: `/Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py`

**Step 1: Run automated verification**

Run: `python3 -m unittest discover -s /Users/wenjiayan/PycharmProjects/驴迹AI/tests -v`

**Step 2: Run structural sanity checks**

Run: `python3 - <<'PY'\nfrom pathlib import Path\ntext = Path('/Users/wenjiayan/PycharmProjects/驴迹AI/lvji-director-report.html').read_text(encoding='utf-8')\nchecks = {\n    'has_flowchart': 'ost-flowchart' in text,\n    'has_target_node': 'ost-target-node' in text,\n    'has_pathway': 'ost-pathway' in text,\n    'has_arrow': 'ost-arrow' in text,\n}\nfor key, value in checks.items():\n    print(f'{key}={value}')\nPY`

Expected:
- all checks print `True`

**Step 3: Review against design goals**

Confirm manually:
- the OST now reads as a flowchart
- the palette still matches the Boardroom Atlas page
- the structure remains easy to scan in a director review
