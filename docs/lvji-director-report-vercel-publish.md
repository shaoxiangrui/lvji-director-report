# lvji-director-report Vercel 发布说明

## 目标

把 [lvji-director-report.html](/Users/wenjiayan/PycharmProjects/驴迹AI/lvji-director-report.html) 作为一个对外可访问的静态汇报页发布，并且只暴露这一份页面，不把仓库里的其他文件一起公开。

## 已配置内容

- [vercel.json](/Users/wenjiayan/PycharmProjects/驴迹AI/vercel.json)
  - 开启 `cleanUrls`
  - 支持根路径 `/`
  - 支持短链接 `/report`
- [.vercelignore](/Users/wenjiayan/PycharmProjects/驴迹AI/.vercelignore)
  - 只允许部署报告页和 Vercel 配置
  - 其余文件不会被上传或对外提供

## 发布步骤

1. 把当前仓库推到你准备接入 Vercel 的 Git 仓库。
2. 在 Vercel 控制台选择 `Add New -> Project`。
3. 导入该仓库。
4. `Framework Preset` 选择 `Other`。
5. `Root Directory` 使用仓库根目录 `/Users/wenjiayan/PycharmProjects/驴迹AI` 对应的仓库根。
6. `Build Command` 留空。
7. `Output Directory` 留空。
8. 点击 `Deploy`。

## 发布后可分享的链接

- `https://<your-project>.vercel.app/`
- `https://<your-project>.vercel.app/report`
- `https://<your-project>.vercel.app/lvji-director-report`

推荐优先发根路径 `/` 或短链接 `/report`。

## 后续更新方式

1. 更新 [lvji-director-report.html](/Users/wenjiayan/PycharmProjects/驴迹AI/lvji-director-report.html)。
2. 提交并推送仓库。
3. Vercel 会自动重新部署。
4. 原分享链接保持不变。

## 自定义域名

如果要给领导一个更正式的地址，可以在 Vercel 项目里绑定自定义域名，例如：

- `https://ai-report.lvji.com/`
- `https://ai-report.lvji.com/report`

## 注意事项

- 如果团队开启了 Vercel 的预览保护，不要直接发 preview 链接，优先发 production 域名。
- 当前方案是“单文件发布”，适合汇报页和静态展示，不适合后续扩展成多页面官网。
