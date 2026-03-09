# Lvji Boardroom Atlas OST Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Replace the journey/validation content in the scenarios section with an Opportunity Solution Tree that matches the existing Boardroom Atlas visual system.

**Architecture:** Keep the current scenario cards and role strip, then remove the old `journey-grid` and `validation-grid` blocks. Add a new `ost-board` component with four columns for target, opportunities, solutions, and experiments, styled as a strategic atlas rather than a Mermaid diagram.

**Tech Stack:** HTML5, CSS3, vanilla JavaScript, Python `unittest`

---

### Task 1: Add failing tests for the new OST structure

**Files:**
- Modify: `/Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py`
- Test: `/Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py`

**Step 1: Write the failing test**

Add expectations for:
- `Opportunity Solution Tree`
- `目标：让 AI 成为驴迹新的增长与效率引擎`
- `机会1：内部交付和售前知识分散`
- `方案：数字交付员工`
- `实验：10 份历史方案自动生成与人工对比`
- `ost-board`

Also add negative assertions for:
- `认知`
- `续约增购`
- `问题验证`
- `商业验证`

**Step 2: Run test to verify it fails**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py -v`  
Expected: FAIL because the old content still exists and the new OST is missing

**Step 3: Write minimal implementation**

Update the scenarios section with the new OST component.

**Step 4: Run test to verify it passes**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py -v`  
Expected: PASS

### Task 2: Add Atlas Tree styling

**Files:**
- Modify: `/Users/wenjiayan/PycharmProjects/驴迹AI/lvji-director-report.html`
- Test: `/Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py`

**Step 1: Write the failing test**

Add expectations for:
- `ost-column`
- `ost-card`
- `ost-target`
- `ost-link`

**Step 2: Run test to verify it fails**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py -v`  
Expected: FAIL on missing style markers

**Step 3: Write minimal implementation**

Implement:
- the four-column board
- card styles
- subtle connector lines
- responsive layout updates

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

Run: `python3 - <<'PY'\nfrom pathlib import Path\ntext = Path('/Users/wenjiayan/PycharmProjects/驴迹AI/lvji-director-report.html').read_text(encoding='utf-8')\nchecks = {\n    'has_ost': 'Opportunity Solution Tree' in text,\n    'has_ost_board': 'ost-board' in text,\n    'removed_journey': '认知' not in text,\n    'removed_validation': '问题验证' not in text,\n}\nfor key, value in checks.items():\n    print(f'{key}={value}')\nPY`

Expected:
- all checks print `True`

**Step 3: Review against design goals**

Confirm manually:
- the new block feels like part of the Boardroom Atlas page
- the page reads more like a director brief than a workshop artifact
- target, opportunities, solutions, and experiments are easy to scan left-to-right
