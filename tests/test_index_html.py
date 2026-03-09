from pathlib import Path
import unittest


PROJECT_ROOT = Path("/Users/wenjiayan/PycharmProjects/驴迹AI")
INDEX_HTML = PROJECT_ROOT / "index.html"


class ReportHtmlStructureTest(unittest.TestCase):
    def test_index_html_has_required_sections(self):
        self.assertTrue(INDEX_HTML.exists(), "index.html should exist")

        text = INDEX_HTML.read_text(encoding="utf-8")

        required_markers = [
            'meta name="viewport"',
            'id="hero"',
            'id="stage-1"',
            'id="stage-2"',
            'id="stage-3"',
            'id="stage-4"',
            'id="stage-5"',
            "1 个文旅 AI 中枢 + 4 类数字员工",
        ]

        for marker in required_markers:
            with self.subTest(marker=marker):
                self.assertIn(marker, text)

    def test_index_html_has_design_system_and_shell(self):
        text = INDEX_HTML.read_text(encoding="utf-8")

        required_markers = [
            "--color-ink",
            "--color-accent",
            'class="section-nav"',
            'class="route-line"',
            "<nav",
            "阶段导航",
        ]

        for marker in required_markers:
            with self.subTest(marker=marker):
                self.assertIn(marker, text)

    def test_index_html_has_p0_strategy_and_scene_content(self):
        text = INDEX_HTML.read_text(encoding="utf-8")

        required_markers = [
            "驴迹文旅 AI 中枢，是一个面向文旅场景的行业化 AI 工作平台。",
            "不是做一个“更聪明的导游功能”，而是做一个“文旅 AI 工作平台”。",
            "文旅知识中枢",
            "数字交付员工",
            "数字导游员工",
            "数字营销员工",
            "数字运营员工",
            "完全无人运营景区",
            "0-3 个月",
            "4-8 个月",
            "9-12 个月",
            "驴迹内部交付提效",
            "游客实时导览服务",
            "景区运营与营销协同",
            "景区运营总监",
            "驴迹交付经理",
            "工时下降 25% 以上且返工可控",
        ]

        for marker in required_markers:
            with self.subTest(marker=marker):
                self.assertIn(marker, text)

    def test_index_html_has_p1_and_p2_content(self):
        text = INDEX_HTML.read_text(encoding="utf-8")

        required_markers = [
            "平台 + 解决方案 + 运营服务",
            "Context Design",
            "Epic 1：文旅知识中枢",
            "Epic 2：数字交付员工",
            "Epic 3：数字导游员工",
            "作为一名",
            "Backbone",
            "Release 1（P0）",
            "TAM",
            "SAM",
            "SOM",
            "自研底层大模型",
            "完全无人化运营",
            "是否同意把“文旅知识中枢”定为所有 AI 项目的统一底座。",
        ]

        for marker in required_markers:
            with self.subTest(marker=marker):
                self.assertIn(marker, text)

    def test_index_html_has_interaction_and_responsive_markers(self):
        text = INDEX_HTML.read_text(encoding="utf-8")

        required_markers = [
            "IntersectionObserver",
            "prefers-reduced-motion: reduce",
            "data-nav-target",
            "data-section",
            'querySelectorAll(".nav-link")',
            "最终建议",
        ]

        for marker in required_markers:
            with self.subTest(marker=marker):
                self.assertIn(marker, text)


if __name__ == "__main__":
    unittest.main()
