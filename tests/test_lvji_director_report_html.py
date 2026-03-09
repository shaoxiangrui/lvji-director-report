from pathlib import Path
import unittest


PROJECT_ROOT = Path("/Users/wenjiayan/PycharmProjects/驴迹AI")
REPORT_HTML = PROJECT_ROOT / "index.html"


class LvjiDirectorReportHtmlTest(unittest.TestCase):
    def test_report_html_has_core_sections(self):
        self.assertTrue(REPORT_HTML.exists(), "index.html should exist")

        text = REPORT_HTML.read_text(encoding="utf-8")

        required_markers = [
            'meta name="viewport"',
            'id="overview"',
            'id="strategy"',
            'id="scenarios"',
            'id="execution"',
            'id="evidence"',
            'id="decision"',
            "驴迹文旅 AI 中枢",
        ]

        for marker in required_markers:
            with self.subTest(marker=marker):
                self.assertIn(marker, text)

    def test_report_html_has_boardroom_atlas_design_system(self):
        text = REPORT_HTML.read_text(encoding="utf-8")

        required_markers = [
            "--paper",
            "--ink",
            "--accent",
            "--signal",
            'class="atlas-nav"',
            'class="hero-map"',
            "Boardroom Atlas",
            "solution-architecture",
            "capability-ledger",
            "capability-road-ledger",
            "capability-plan-row",
            "capability-plan-head",
            "capability-plan-meta",
            "capability-plan-detail",
            "investment-assessment",
            "investment-row",
            "deprioritized-board",
            "deprioritized-card",
            'class="chapter-head is-selected"',
            ".atlas-link.is-active",
            "strategy-analysis-button",
            "strategy-analysis-modal",
            "strategy-analysis-dialog",
            "strategy-analysis-overlay",
            "strategy-analysis-scroll",
            "analysis-summary-board",
            "analysis-card-grid",
            "analysis-focus-card",
            "analysis-card-verdict",
            "strategy-analysis-footer",
            "P0",
            "P1",
            "P2",
        ]

        for marker in required_markers:
            with self.subTest(marker=marker):
                self.assertIn(marker, text)

    def test_report_html_has_p0_strategy_and_scenarios(self):
        text = REPORT_HTML.read_text(encoding="utf-8")
        strategy_start = text.index('id="strategy"')
        scenarios_start = text.index('id="scenarios"')
        execution_start = text.index('id="execution"')
        strategy_text = text[strategy_start:scenarios_start]
        scenarios_text = text[scenarios_start:execution_start]

        required_markers = [
            "解决方案架构",
            "定位分析",
            "为什么本年度优先做 AI 中枢知识底座和 4 个数字员工，而不是通用办公 AI 数字员工",
            "AI 中枢知识底座 + 4 个数字员工",
            "通用办公 AI 数字员工（如财务/行政）",
            "与公司现有资产匹配度",
            "应优先投向资产匹配度更高的方向",
            "应优先投向能直接作用主航道收入与毛利的方向",
            "应优先投向可沉淀长期壁垒的方向",
            "今年应优先双重 ROI 路径，而不是单一降本",
            "应优先做客户看得见、愿意买单的能力",
            "今年应先完成统一底座建设，再扩内部通用助手",
            "能力边界",
            "L1 文旅知识中枢",
            "L2 Agent 工作流层",
            "L3 数字员工层",
            "L4 产品接入层",
            "检索、引用、标签、审批、版本、租户隔离",
            "工作流编排、消息通知、人工审核、日志审计",
            "电子导览、SaaS、一部手机游、全域旅游、智慧景区、运营后台",
            "文旅 AI 工作平台",
            "有限的人力，服务更复杂、更多变、更多角色参与的文旅场景",
            "文旅知识中枢",
            "数字交付员工",
            "数字导游员工",
            "数字营销员工",
            "数字运营员工",
            "问答与检索",
            "文案与内容生成",
            "推荐与建议",
            "预警与摘要",
            "流程协同",
            "不能独立决策的场景",
            "涉及票价、合同承诺、投诉定责、政府对外口径、安全事故处置、重大调度等，必须人工审批",
            "完全无人运营景区",
            "0-3 个月",
            "4-8 个月",
            "9-12 个月",
            "驴迹内部交付提效",
            "游客实时导览服务",
            "景区运营与营销协同",
            "作为一名 驴迹交付经理",
            "作为一名 游客",
            "作为一名 景区内容运营",
            "景区运营总监",
            "驴迹交付经理",
            "游客",
        ]

        for marker in required_markers:
            with self.subTest(marker=marker):
                self.assertIn(marker, text)

        strategy_only_markers = [
            "data-modal-open",
        ]

        for marker in strategy_only_markers:
            with self.subTest(strategy_marker=marker):
                self.assertIn(marker, strategy_text)

        strategy_removed_markers = [
            "data-modal-close",
            "data-modal-overlay",
            'id="strategy-analysis-modal"',
            'class="strategy-analysis-modal"',
        ]

        for marker in strategy_removed_markers:
            with self.subTest(strategy_removed_marker=marker):
                self.assertNotIn(marker, strategy_text)

        modal_index = text.index('id="strategy-analysis-modal"')
        main_close_index = text.index("</main>")
        self.assertGreater(modal_index, main_close_index)

        removed_markers = [
            "Opportunity Solution Tree",
            "ost-board",
            "ost-flowchart",
            "ost-target-node",
            "ost-pathway",
            "ost-node",
            "ost-arrow",
            "认知",
            "问题验证",
            "商业验证",
        ]

        for marker in removed_markers:
            with self.subTest(removed_marker=marker):
                self.assertNotIn(marker, text)

        story_index = scenarios_text.index("作为一名 驴迹交付经理")
        role_index = scenarios_text.index("景区运营总监")
        self.assertLess(story_index, role_index)

    def test_report_html_has_execution_and_evidence_layers(self):
        text = REPORT_HTML.read_text(encoding="utf-8")
        execution_start = text.index('id="execution"')
        evidence_start = text.index('id="evidence"')
        decision_start = text.index('id="decision"')
        execution_text = text[execution_start:evidence_start]
        evidence_text = text[evidence_start:decision_start]

        execution_markers = [
            "Epic 1：文旅知识中枢",
            "Epic 2：数字交付员工",
            "Epic 3：数字导游员工",
            "Epic 4：数字营销/运营员工",
            "按能力划分的执行计划",
            "文旅知识中枢 v1",
            "数字交付员工 v1",
            "安全与治理",
            "数字导游员工 v1",
            "数字营销员工 v1",
            "商业化包装",
            "数字运营员工 v1",
            "ROI 看板与续约策略",
            "月 1-2",
            "月 9-12",
            "知识中枢、数据字典、治理规范",
            "ROI 仪表板、续约话术、复盘机制",
            "class=\"chapter-head is-selected\"",
        ]

        for marker in execution_markers:
            with self.subTest(marker=marker):
                self.assertIn(marker, text)

        execution_removed_markers = [
            "story-map",
            "priority-grid",
            "Backbone",
            "Release 1（P0）",
        ]

        for marker in execution_removed_markers:
            with self.subTest(removed_marker=marker):
                self.assertNotIn(marker, execution_text)

        evidence_markers = [
            "投资评估",
            "文旅知识中枢",
            "数字交付员工",
            "数字导游员工",
            "数字营销员工",
            "数字运营员工",
            "间接，支撑全部后续收入",
            "短期 ROI 最强",
            "对外价值最直观，是 AI 形象入口",
            "最容易标准化与复制",
            "如果做成，将提升客单价与竞争壁垒",
            "不建议优先投资的方向",
            "自研底层大模型",
            "完全无人化运营",
            "泛办公助手",
            "重度定制的一客一版 AI",
            "资金消耗大，不是驴迹的核心优势",
            "长期会吞噬毛利并破坏平台化节奏",
        ]

        for marker in evidence_markers:
            with self.subTest(evidence_marker=marker):
                self.assertIn(marker, evidence_text)

        evidence_removed_markers = [
            'class="signal-grid"',
            'class="evidence-split"',
            'class="market-grid"',
            'class="do-not-grid"',
            "平台 + 解决方案 + 运营服务",
            "Context Design",
            "Agent Orchestration",
            "TAM",
            "SAM",
            "SOM",
            "建议做",
            "当前不做",
        ]

        for marker in evidence_removed_markers:
            with self.subTest(evidence_removed_marker=marker):
                self.assertNotIn(marker, evidence_text)

    def test_report_html_has_decision_board_and_interactions(self):
        text = REPORT_HTML.read_text(encoding="utf-8")

        required_markers = [
            "决策思考 / Decision Thinking",
            "标准化优先还是客户定制优先，以及谁有特批权",
            "模型、部署与数据边界策略",
            "知识治理责任制：谁拥有内容质量、更新 SLA 和口径仲裁权",
            "IntersectionObserver",
            "prefers-reduced-motion: reduce",
            "body.modal-open",
            "document.documentElement.classList.add(\"modal-open\")",
            "data-nav-target",
            "querySelectorAll(\".atlas-link\")",
            "const syncActiveLinkWithViewport = () =>",
            "window.addEventListener(\"hashchange\", syncActiveLinkWithViewport)",
            "link.addEventListener(\"click\", () => {",
            "requestAnimationFrame(syncActiveLinkWithViewport)",
            "const strategyAnalysisModal = document.querySelector(\"[data-modal]\")",
            "data-modal-scroll",
            "const getStrategyAnalysisFocusableElements = () =>",
            "const openStrategyAnalysisModal = (trigger) =>",
            "document.addEventListener(\"keydown\", (event) => {",
            "event.key === \"Escape\"",
            "event.key === \"Tab\"",
            "focus({ preventScroll: true })",
            "@media (max-width: 1080px)",
        ]

        for marker in required_markers:
            with self.subTest(marker=marker):
                self.assertIn(marker, text)


if __name__ == "__main__":
    unittest.main()
