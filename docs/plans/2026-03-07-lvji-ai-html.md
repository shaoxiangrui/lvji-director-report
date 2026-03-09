# Lvji AI Report HTML Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a single-page HTML report for the Lvji AI strategy brief that presents the refined content in a director-ready, high-design format.

**Architecture:** Use one static `index.html` with embedded content sections, a cohesive CSS design system, and a small amount of vanilla JavaScript for active navigation, staged reveals, and lightweight interactions. Keep the page portable, offline-friendly, and readable without build tooling.

**Tech Stack:** HTML5, CSS3, vanilla JavaScript, Python `unittest` for structural verification

---

### Task 1: Create a failing structural test

**Files:**
- Create: `/Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_index_html.py`
- Test: `/Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_index_html.py`

**Step 1: Write the failing test**

Create a test that expects:
- `/Users/wenjiayan/PycharmProjects/驴迹AI/index.html` to exist
- the document to contain `meta name="viewport"`
- sections for `hero`, `stage-1`, `stage-2`, `stage-3`, `stage-4`, `stage-5`
- the text `1 个文旅 AI 中枢 + 4 类数字员工`

**Step 2: Run test to verify it fails**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_index_html.py -v`  
Expected: FAIL because `index.html` does not exist yet

**Step 3: Write minimal implementation**

Create the minimal `index.html` skeleton with required section IDs and key text.

**Step 4: Run test to verify it passes**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_index_html.py -v`  
Expected: PASS

### Task 2: Build the visual system and page shell

**Files:**
- Modify: `/Users/wenjiayan/PycharmProjects/驴迹AI/index.html`
- Test: `/Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_index_html.py`

**Step 1: Write the failing test**

Add expectations for:
- CSS custom properties for theme colors
- a sticky navigation block
- a route/timeline area
- semantic headings for all stages

**Step 2: Run test to verify it fails**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_index_html.py -v`  
Expected: FAIL on missing design system markers

**Step 3: Write minimal implementation**

Add:
- global CSS variables
- page shell layout
- sticky section navigation
- hero composition
- shared card styles

**Step 4: Run test to verify it passes**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_index_html.py -v`  
Expected: PASS

### Task 3: Implement P0 sections with strongest visual emphasis

**Files:**
- Modify: `/Users/wenjiayan/PycharmProjects/驴迹AI/index.html`
- Test: `/Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_index_html.py`

**Step 1: Write the failing test**

Add expectations for:
- stage 2 section containing problem statement, strategy positioning, capability boundary, roadmap
- stage 3 section containing three scenes and three personas
- navigation labels marking stage 2 and stage 3 as `P0`

**Step 2: Run test to verify it fails**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_index_html.py -v`  
Expected: FAIL on missing P0 content markers

**Step 3: Write minimal implementation**

Implement:
- stage 2 strategic grid and timeline
- stage 3 scene cards, persona cards, and validation flow
- visual treatments that make P0 the dominant reading path

**Step 4: Run test to verify it passes**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_index_html.py -v`  
Expected: PASS

### Task 4: Implement P1 and P2 evidence layers

**Files:**
- Modify: `/Users/wenjiayan/PycharmProjects/驴迹AI/index.html`
- Test: `/Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_index_html.py`

**Step 1: Write the failing test**

Add expectations for:
- stage 4 epic cards and story map labels
- stage 5 TAM/SAM/SOM and investment matrix
- stage 1 company signals and readiness summary
- final decision block with 4 approval questions

**Step 2: Run test to verify it fails**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_index_html.py -v`  
Expected: FAIL on missing P1/P2 markers

**Step 3: Write minimal implementation**

Implement:
- stage 1 evidence cards
- stage 4 epic, user story, and release slice area
- stage 5 market cards, investment matrix, final board questions

**Step 4: Run test to verify it passes**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_index_html.py -v`  
Expected: PASS

### Task 5: Add lightweight interactions and responsive refinement

**Files:**
- Modify: `/Users/wenjiayan/PycharmProjects/驴迹AI/index.html`
- Test: `/Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_index_html.py`

**Step 1: Write the failing test**

Add expectations for:
- script markers for active navigation
- reduced-motion handling
- responsive breakpoints
- visible text for final recommendation

**Step 2: Run test to verify it fails**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_index_html.py -v`  
Expected: FAIL on missing interaction markers

**Step 3: Write minimal implementation**

Add:
- intersection-based active nav
- section reveal classes
- reduced-motion CSS fallback
- responsive layout adjustments for mobile

**Step 4: Run test to verify it passes**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_index_html.py -v`  
Expected: PASS

### Task 6: Final verification

**Files:**
- Verify: `/Users/wenjiayan/PycharmProjects/驴迹AI/index.html`
- Verify: `/Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_index_html.py`

**Step 1: Run automated verification**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_index_html.py -v`

**Step 2: Run basic HTML sanity check**

Run: `python3 - <<'PY'\nfrom pathlib import Path\ntext = Path('/Users/wenjiayan/PycharmProjects/驴迹AI/index.html').read_text(encoding='utf-8')\nprint('has_html', '<html' in text.lower())\nprint('has_css_vars', '--color-ink' in text)\nprint('has_stage_2', 'stage-2' in text)\nprint('has_stage_3', 'stage-3' in text)\nPY`

Expected:
- all checks print `True`

**Step 3: Review against design goals**

Confirm manually:
- P0 sections dominate above the fold and mid-page
- P1 supports execution without overwhelming
- P2 reads as evidence and investment rationale
- page opens locally without build tooling
