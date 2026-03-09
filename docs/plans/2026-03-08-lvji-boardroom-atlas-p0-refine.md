# Lvji Boardroom Atlas P0 Refine Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Replace the P0 positioning statement with a solution architecture module and replace the two-column capability promise block with a unified capability boundary ledger in the standalone director report HTML.

**Architecture:** Keep the existing `Boardroom Atlas` design system and restructure only the `#strategy` section. Introduce two new presentation components: a layered solution architecture board and a single capability ledger that groups deliverable abilities and explicit approval boundaries without changing the rest of the page narrative.

**Tech Stack:** HTML5, CSS3, vanilla JavaScript, Python `unittest`

---

### Task 1: Add failing tests for the new P0 structure

**Files:**
- Modify: `/Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py`
- Test: `/Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py`

**Step 1: Write the failing test**

Add expectations for:
- `解决方案架构`
- `L1 文旅知识中枢`
- `L2 Agent 工作流层`
- `L3 数字员工层`
- `L4 产品接入层`
- `检索、引用、标签、审批、版本、租户隔离`
- `能力边界`
- `问答与检索`
- `流程协同`
- `不能独立决策的场景`

**Step 2: Run test to verify it fails**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py -v`  
Expected: FAIL on the new P0 markers

**Step 3: Write minimal implementation**

Update the HTML with the new structure and content.

**Step 4: Run test to verify it passes**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py -v`  
Expected: PASS

### Task 2: Replace the positioning card with layered architecture UI

**Files:**
- Modify: `/Users/wenjiayan/PycharmProjects/驴迹AI/lvji-director-report.html`
- Test: `/Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py`

**Step 1: Write the failing test**

Add expectations for:
- a `solution-architecture` marker class
- a visual layer rail
- the four architecture levels and their mapped abilities

**Step 2: Run test to verify it fails**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py -v`  
Expected: FAIL on missing structure markers

**Step 3: Write minimal implementation**

Implement:
- architecture shell
- level rail
- four architecture cards
- supporting summary copy

**Step 4: Run test to verify it passes**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py -v`  
Expected: PASS

### Task 3: Replace the old boundary cards with a unified capability ledger

**Files:**
- Modify: `/Users/wenjiayan/PycharmProjects/驴迹AI/lvji-director-report.html`
- Test: `/Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py`

**Step 1: Write the failing test**

Add expectations for:
- a `capability-ledger` marker class
- rows for the five deliverable capabilities
- rows for approval-required and cannot-promise boundaries

**Step 2: Run test to verify it fails**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py -v`  
Expected: FAIL on missing ledger markers

**Step 3: Write minimal implementation**

Implement:
- one unified boundary card
- capability rows with green labels
- risk rows with amber labels

**Step 4: Run test to verify it passes**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py -v`  
Expected: PASS

### Task 4: Final verification

**Files:**
- Verify: `/Users/wenjiayan/PycharmProjects/驴迹AI/lvji-director-report.html`
- Verify: `/Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py`

**Step 1: Run automated verification**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py -v`

**Step 2: Run structural sanity checks**

Run: `python3 - <<'PY'\nfrom pathlib import Path\ntext = Path('/Users/wenjiayan/PycharmProjects/驴迹AI/lvji-director-report.html').read_text(encoding='utf-8')\nchecks = {\n    'has_solution_architecture': '解决方案架构' in text,\n    'has_capability_boundary': '能力边界' in text,\n    'has_layered_ui': 'solution-architecture' in text,\n    'has_boundary_ledger': 'capability-ledger' in text,\n}\nfor key, value in checks.items():\n    print(f'{key}={value}')\nPY`

Expected:
- all checks print `True`

**Step 3: Review against design goals**

Confirm manually:
- the P0 section still reads as part of the same `Boardroom Atlas` page
- the architecture is easier to scan than the old positioning card
- the boundary block now makes approval constraints explicit
