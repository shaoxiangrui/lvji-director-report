# Lvji Capability Road Ledger Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Remove the Opportunity Solution Tree, move the existing user story cards into the scenarios section without changing their content or style, and replace the old execution artifacts with a director-facing capability execution ledger.

**Architecture:** Keep the current `Boardroom Atlas` visual system and only restructure the `#scenarios` and `#execution` sections. Reuse the existing `stories-grid` markup unchanged, delete the OST and the old `story-map` / `priority-grid`, and introduce one new execution-ledger module that reads like a board-level operating ledger rather than a generic table.

**Tech Stack:** HTML5, CSS3, vanilla JavaScript, Python `unittest`

---

### Task 1: Update structural tests for the new section order and removals

**Files:**
- Modify: `/Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py:30-170`
- Test: `/Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py`

**Step 1: Write the failing test**

Update the report test so it expects:
- the OST markers to be absent
- the `stories-grid` content to appear in `#scenarios`
- the first story text to appear before the first role card
- `story-map` and `priority-grid` to be absent
- a new execution ledger marker such as `capability-road-ledger`
- execution-plan rows for the eight capability items

Example assertions to add:

```python
self.assertNotIn("Opportunity Solution Tree", text)
self.assertNotIn("ost-board", text)
self.assertNotIn("story-map", text)
self.assertNotIn("priority-grid", text)
self.assertIn("capability-road-ledger", text)

story_index = text.index("作为一名 驴迹交付经理")
role_index = text.index("景区运营总监")
self.assertLess(story_index, role_index)
```

**Step 2: Run test to verify it fails**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py -v`  
Expected: FAIL because the current page still contains the OST and old execution artifacts

**Step 3: Write minimal implementation**

Do not implement everything yet. Only adjust the test file so it describes the intended structure.

**Step 4: Run test to verify it fails for the right reason**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py -v`  
Expected: FAIL on missing ledger markers and on the presence of the old OST / story-map / priority-grid content

**Step 5: Commit**

```bash
git add /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py
git commit -m "test: update report expectations for capability ledger"
```

### Task 2: Remove the OST and move the existing stories-grid into the scenarios section

**Files:**
- Modify: `/Users/wenjiayan/PycharmProjects/驴迹AI/lvji-director-report.html:1948-2075`
- Test: `/Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py`

**Step 1: Write the failing test**

Extend or confirm tests for:
- no `ost-board`, `ost-flowchart`, `ost-target-node`, `ost-pathway`, `ost-node`, or `ost-arrow`
- `stories-grid` content still exists
- the three user stories appear before the first role card

**Step 2: Run test to verify it fails**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py -v`  
Expected: FAIL on the old OST block still being present

**Step 3: Write minimal implementation**

In `/Users/wenjiayan/PycharmProjects/驴迹AI/lvji-director-report.html`:
- delete the entire OST block at `#scenarios`
- cut the existing `stories-grid` block from `#execution`
- paste that same block above `roles-grid` in `#scenarios`
- do not change any story text, story order, or `stories-grid` / `story-card` classes

The moved block should remain identical in content and classes:

```html
<div class="stories-grid">
  <article class="story-card">...</article>
  <article class="story-card">...</article>
  <article class="story-card">...</article>
</div>
```

**Step 4: Run test to verify it passes**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py -v`  
Expected: PASS on the moved-story and removed-OST assertions, while still failing on the missing execution ledger

**Step 5: Commit**

```bash
git add /Users/wenjiayan/PycharmProjects/驴迹AI/lvji-director-report.html /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py
git commit -m "refactor: move user stories into scenarios section"
```

### Task 3: Remove story-map and priority-grid from the execution section

**Files:**
- Modify: `/Users/wenjiayan/PycharmProjects/驴迹AI/lvji-director-report.html:2114-2187`
- Test: `/Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py`

**Step 1: Write the failing test**

Add or keep assertions that:
- `story-map` is absent
- `priority-grid` is absent
- `Backbone`, `Release 1（P0）`, and the old priority card titles are no longer required in the execution section

Example test change:

```python
self.assertNotIn("story-map", text)
self.assertNotIn("priority-grid", text)
```

**Step 2: Run test to verify it fails**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py -v`  
Expected: FAIL because the old blocks still exist

**Step 3: Write minimal implementation**

In `/Users/wenjiayan/PycharmProjects/驴迹AI/lvji-director-report.html`:
- remove the entire `<div class="story-map">...</div>`
- remove the entire `<div class="priority-grid">...</div>`
- keep `epic-grid` in place

**Step 4: Run test to verify it passes**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py -v`  
Expected: PASS on removal checks, while still failing on the missing capability execution ledger

**Step 5: Commit**

```bash
git add /Users/wenjiayan/PycharmProjects/驴迹AI/lvji-director-report.html /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py
git commit -m "refactor: remove old execution map and priority blocks"
```

### Task 4: Add the Capability Road Ledger styles

**Files:**
- Modify: `/Users/wenjiayan/PycharmProjects/驴迹AI/lvji-director-report.html:300-520`
- Test: `/Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py`

**Step 1: Write the failing test**

Add expectations for new markers:
- `capability-road-ledger`
- `capability-plan-row`
- `capability-plan-head`
- `capability-plan-meta`
- `capability-plan-detail`

Example:

```python
for marker in [
    "capability-road-ledger",
    "capability-plan-row",
    "capability-plan-head",
]:
    self.assertIn(marker, text)
```

**Step 2: Run test to verify it fails**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py -v`  
Expected: FAIL on missing capability-ledger style markers

**Step 3: Write minimal implementation**

Add CSS that fits the current `Boardroom Atlas` system:
- a ledger wrapper using the existing paper background and border treatment
- row-level cards with slightly stronger left-to-right reading structure
- copper priority tags for `P0 / P1 / P2`
- a two-part detail area for `关键动作` and `交付物`
- responsive fallback that collapses each row to one column on narrow screens

Example CSS skeleton:

```css
.capability-road-ledger {
  display: grid;
  gap: 14px;
  padding: 24px;
  border-radius: 26px;
  border: 1px solid rgba(24, 37, 33, 0.08);
}

.capability-plan-row {
  display: grid;
  grid-template-columns: 200px minmax(0, 1fr);
  gap: 16px;
}
```

**Step 4: Run test to verify it passes**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py -v`  
Expected: PASS on style marker checks, while still failing on missing row content if not yet added

**Step 5: Commit**

```bash
git add /Users/wenjiayan/PycharmProjects/驴迹AI/lvji-director-report.html /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py
git commit -m "style: add capability road ledger system"
```

### Task 5: Add the capability execution ledger content

**Files:**
- Modify: `/Users/wenjiayan/PycharmProjects/驴迹AI/lvji-director-report.html:2078-2188`
- Test: `/Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py`

**Step 1: Write the failing test**

Add expectations for the execution-plan content:
- `文旅知识中枢 v1`
- `数字交付员工 v1`
- `安全与治理`
- `数字导游员工 v1`
- `数字营销员工 v1`
- `商业化包装`
- `数字运营员工 v1`
- `ROI 看板与续约策略`
- `月 1-2`
- `月 9-12`
- `知识中枢、数据字典、治理规范`
- `ROI 仪表板、续约话术、复盘机制`

**Step 2: Run test to verify it fails**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py -v`  
Expected: FAIL because the execution ledger content is not in the HTML yet

**Step 3: Write minimal implementation**

Insert a new block below `epic-grid`:

```html
<section class="capability-road-ledger" aria-label="按能力划分的执行计划">
  <div class="ledger-head">
    <span class="meta-label">执行计划</span>
    <h3>按能力划分的执行计划</h3>
  </div>
  <article class="capability-plan-row">...</article>
</section>
```

Represent each row with:
- `优先级`
- `能力`
- `时间`
- `关键动作`
- `交付物`

Include all eight rows exactly as provided in the design:

```html
<article class="capability-plan-row">
  <div class="capability-plan-head">
    <span class="priority-chip">P0</span>
    <h4>文旅知识中枢 v1</h4>
    <p>月 1-2</p>
  </div>
  <div class="capability-plan-detail">
    <div>
      <strong>关键动作</strong>
      <p>定义知识域、主数据、权限、引用、更新时间规则</p>
    </div>
    <div>
      <strong>交付物</strong>
      <p>知识中枢、数据字典、治理规范</p>
    </div>
  </div>
</article>
```

Repeat for the remaining seven rows:
- `数字交付员工 v1`
- `安全与治理`
- `数字导游员工 v1`
- `数字营销员工 v1`
- `商业化包装`
- `数字运营员工 v1`
- `ROI 看板与续约策略`

**Step 4: Run test to verify it passes**

Run: `python3 -m unittest /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py -v`  
Expected: PASS

**Step 5: Commit**

```bash
git add /Users/wenjiayan/PycharmProjects/驴迹AI/lvji-director-report.html /Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py
git commit -m "feat: add capability road ledger to execution section"
```

### Task 6: Final verification

**Files:**
- Verify: `/Users/wenjiayan/PycharmProjects/驴迹AI/lvji-director-report.html`
- Verify: `/Users/wenjiayan/PycharmProjects/驴迹AI/tests/test_lvji_director_report_html.py`

**Step 1: Run automated verification**

Run: `python3 -m unittest discover -s /Users/wenjiayan/PycharmProjects/驴迹AI/tests -v`

**Step 2: Run structural sanity checks**

Run: `python3 - <<'PY'\nfrom pathlib import Path\ntext = Path('/Users/wenjiayan/PycharmProjects/驴迹AI/lvji-director-report.html').read_text(encoding='utf-8')\nchecks = {\n    'removed_ost': 'Opportunity Solution Tree' not in text,\n    'removed_story_map': 'story-map' not in text,\n    'removed_priority_grid': 'priority-grid' not in text,\n    'has_capability_ledger': 'capability-road-ledger' in text,\n    'has_story_before_role': text.index('作为一名 驴迹交付经理') < text.index('景区运营总监'),\n}\nfor key, value in checks.items():\n    print(f'{key}={value}')\nPY`

Expected:
- all checks print `True`

**Step 3: Review against design goals**

Confirm manually:
- `P0` now reads as `场景 -> 用户故事 -> 角色`
- `P1` now reads as `Epic -> 执行计划`
- the new execution module feels like a board-level ledger, not a backend table
