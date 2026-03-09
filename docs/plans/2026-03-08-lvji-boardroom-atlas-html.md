# Lvji Boardroom Atlas HTML Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a standalone director-facing HTML report from the refined Lvji AI strategy brief without changing the existing `index.html`.

**Architecture:** Create one offline-friendly HTML document at `/Users/wenjiayan/PycharmProjects/驴迹AI/lvji-director-report.html` with embedded CSS and vanilla JavaScript. Keep the page structured around the approved `Boardroom Atlas` narrative: executive overview, P0 strategy, P0 scenarios, P1 execution, P2 evidence, final decisions. Add a dedicated structural test for the new file rather than reusing the existing `index.html` test.

**Tech Stack:** HTML5, CSS3, vanilla JavaScript, Python `unittest`

---

### Task 1: Add a failing structural test for the new report

**Files:**
- Create: `/Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py`
- Test: `/Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py`

**Step 1: Write the failing test**

Create a test that expects:
- `/Users/wenjiayan/PycharmProjects/驴迹AI/lvji-director-report.html` to exist
- a viewport meta tag
- section IDs for `overview`, `strategy`, `scenarios`, `execution`, `evidence`, and `decision`
- the text `驴迹文旅 AI 中枢`

**Step 2: Run test to verify it fails**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py -v`  
Expected: FAIL because the file does not exist yet

**Step 3: Write minimal implementation**

Create the minimal HTML skeleton with the required IDs and the `驴迹文旅 AI 中枢` text.

**Step 4: Run test to verify it passes**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py -v`  
Expected: PASS

### Task 2: Build the Boardroom Atlas design system and shell

**Files:**
- Modify: `/Users/wenjiayan/PycharmProjects/驴迹AI/lvji-director-report.html`
- Test: `/Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py`

**Step 1: Write the failing test**

Add expectations for:
- CSS custom properties for paper, ink, accent, and signal colors
- a sticky atlas navigation
- a hero route visual
- chapter labels that show `P0`, `P1`, and `P2`

**Step 2: Run test to verify it fails**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py -v`  
Expected: FAIL on missing design system markers

**Step 3: Write minimal implementation**

Implement:
- global CSS variables
- page shell layout
- sticky navigation
- hero layout
- shared panel, card, and metric styles

**Step 4: Run test to verify it passes**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py -v`  
Expected: PASS

### Task 3: Implement P0 strategy and scenario sections

**Files:**
- Modify: `/Users/wenjiayan/PycharmProjects/驴迹AI/lvji-director-report.html`
- Test: `/Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py`

**Step 1: Write the failing test**

Add expectations for:
- the unified problem statement
- the `1 个中枢 + 4 类数字员工` structure
- a can-do / cannot-promise boundary area
- the three key scenarios and three key roles
- the 12-month roadmap

**Step 2: Run test to verify it fails**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py -v`  
Expected: FAIL on missing P0 content

**Step 3: Write minimal implementation**

Implement:
- strategy cards
- architecture spine
- boundary ledger
- roadmap rail
- scenario trio
- roles strip
- journey and validation board

**Step 4: Run test to verify it passes**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py -v`  
Expected: PASS

### Task 4: Implement P1 execution and P2 evidence sections

**Files:**
- Modify: `/Users/wenjiayan/PycharmProjects/驴迹AI/lvji-director-report.html`
- Test: `/Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py`

**Step 1: Write the failing test**

Add expectations for:
- the four epics
- the three core user stories
- story map headers
- company signal markers
- readiness markers
- TAM/SAM/SOM
- do/don't investment items

**Step 2: Run test to verify it fails**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py -v`  
Expected: FAIL on missing execution and evidence content

**Step 3: Write minimal implementation**

Implement:
- epic board
- user story cards
- story map matrix
- priority ladder
- evidence grid
- readiness bars
- investment board

**Step 4: Run test to verify it passes**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py -v`  
Expected: PASS

### Task 5: Implement final decision board and interactions

**Files:**
- Modify: `/Users/wenjiayan/PycharmProjects/驴迹AI/lvji-director-report.html`
- Test: `/Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py`

**Step 1: Write the failing test**

Add expectations for:
- final decision prompts
- final recommendation text
- `IntersectionObserver`
- reduced-motion handling
- responsive breakpoint markers

**Step 2: Run test to verify it fails**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py -v`  
Expected: FAIL on missing decision and interaction markers

**Step 3: Write minimal implementation**

Implement:
- final decision board
- final recommendation block
- section reveal transitions
- active navigation highlighting
- reduced motion fallback
- mobile layout adjustments

**Step 4: Run test to verify it passes**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py -v`  
Expected: PASS

### Task 6: Final verification

**Files:**
- Verify: `/Users/wenjiayan/PycharmProjects/驴迹AI/lvji-director-report.html`
- Verify: `/Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py`

**Step 1: Run automated verification**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py -v`

**Step 2: Run basic HTML sanity checks**

Run: `python3 - <<'PY'\nfrom pathlib import Path\ntext = Path('/Users/wenjiayan/PycharmProjects/驴迹AI/lvji-director-report.html').read_text(encoding='utf-8')\nchecks = {\n    'has_html': '<html' in text.lower(),\n    'has_nav': 'atlas-nav' in text,\n    'has_strategy': 'id=\"strategy\"' in text,\n    'has_scenarios': 'id=\"scenarios\"' in text,\n    'has_execution': 'id=\"execution\"' in text,\n    'has_evidence': 'id=\"evidence\"' in text,\n    'has_decision': 'id=\"decision\"' in text,\n}\nfor key, value in checks.items():\n    print(f'{key}={value}')\nPY`

Expected:
- all checks print `True`

**Step 3: Review against design goals**

Confirm manually:
- the page reads like a director brief, not a product landing page
- `P0` owns the visual center of the page
- `P1` proves executability without overtaking the strategy
- `P2` supports the case with concise evidence
- the page remains readable offline without build tooling
