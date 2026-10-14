# SBA 网站修改方法（任何 Claude 账号接手先读）

网站 supplybridgeasia.com = 本仓库 zane698/supplybridgeasia-site 的 main 分支，GitHub Pages 自动发布（推送后 1–2 分钟生效）。域名解析已指向 GitHub，不用再动阿里云。

## 怎么改
1. 在 Claude 对话里加载仓库 zane698/supplybridgeasia-site（push 权限），clone 到本地。
2. 改之前先 `git fetch origin main` 并基于最新 main 改，别的账号可能刚改过。不要强推、不要覆盖别人的改动。
3. 改 HTML/CSS/图片 → commit → `git push origin main`。
4. 手机打开 supplybridgeasia.com 检查（强制刷新）。

## 文件
- index.html 首页；company.html 公司页；quote.html 询价页；privacy.html / terms.html
- assets/site.css 样式（藏青 #13285A、金 #E9A63A）；assets/ 图片视频
- downloads/Supply_Bridge_Asia_Company_Profile_2026.pdf 公司 PDF（9 页，发电机组封面版）
- CNAME（supplybridgeasia.com）和 .nojekyll 不要删

## 规则
- 详细规则见 Google Drive《【现行】SBA 网站修改方法》和《【现行】SBA 交接总表》。本仓库公开，不写内部信息。
