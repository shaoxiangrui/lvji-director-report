# Lvji Director Report Share + Print Design

**Context**

现有 [lvji-director-report.html](/Users/wenjiayan/PycharmProjects/驴迹AI/lvji-director-report.html) 已经是单文件汇报页，适合继续作为唯一内容源。当前缺口有两个：

1. 屏幕版视觉完整，但直接导出 PDF 时会带入粘性导航、背景纹理、阴影和动画，不够像正式汇报稿。
2. 如果直接做静态发布，仓库里其他文件也可能被一起上传并暴露，且外链路径不够收敛。

**Decision**

采用“单文件双用途”方案：

- 继续以 `lvji-director-report.html` 作为唯一内容源。
- 在同一文件中新增打印样式，让浏览器打印时自动切换到 A4 友好布局。
- 用 `Vercel + .vercelignore + vercel.json` 发布，只暴露报告页和部署配置。

**Print Design**

- 打印时隐藏左侧导航、弹窗、交互按钮、背景纹理和动画。
- 页面切换为白底、弱装饰、低阴影的纸面风格。
- 章节按 section 分页，卡片、表格行、路线图卡片尽量避免被截断。
- Hero 区保留核心结论和来源说明，隐藏装饰性地图，减少 PDF 首屏浪费。

**Share Design**

- Vercel 仅部署：
  - `lvji-director-report.html`
  - `vercel.json`
  - `.vercelignore`
- 外链支持：
  - 根路径 `/`
  - 短链接 `/report`
  - 清爽路径 `/lvji-director-report`

**Accessibility / Quality Guardrails**

- 增加 skip link 和 `main` 锚点，避免外链页面只有导航没有快速跳转。
- 不改动正文结构和现有章节锚点，保持当前阅读路径不变。
- 部署说明文档写清分享链接、更新路径和 Vercel 面板设置，降低后续维护成本。
