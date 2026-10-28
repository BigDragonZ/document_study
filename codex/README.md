# Codex 实战手册

一份从第一次打开 Codex 开始、通过真实练习逐步成长的中文开源学习手册。

## 本地预览

本手册已合并到 `document_study` 学习中心，当前位于 `/Users/naihe/Documents/document_study/codex/`。直接在浏览器打开 `codex/index.html` 即可。课程站点使用原生 HTML、CSS 和 JavaScript，不需要安装依赖或构建工具。

也可以从学习中心根目录启动 HTTP 预览：

```bash
cd /Users/naihe/Documents/document_study
python3 -m http.server 8000
```

然后访问 `http://127.0.0.1:8000/codex/index.html`，或通过 `http://127.0.0.1:8000/index.html` 返回统一学习入口。

## 页面结构

- `index.html`：手册首页与现有实战学习路线。
- `quickstart.html`：汇总 OpenAI 官方 Quickstart、Use ChatGPT、Get started with Work、Meet dots、Import from another agent 五篇入门文档。
- `foundations.html`：汇总 OpenAI 官方 Foundations 的 Prompting、Model selection、Personalize ChatGPT、Skills & Plugins、Permissions 五篇实际使用文档。
- `configuration.html`：概览 OpenAI 官方 Configuration 的设置层级、项目指导、配置文件、扩展方式与管理边界。
- `developers-guide.html`、`security-guide.html`：概览 Developers 与 Security 两个官方文档栏目，分别整理开发工作流、环境、自动化与集成，以及权限、沙箱、审批和代码安全。
- `workflows-guide.html`、`capabilities-guide.html`、`sites-guide.html`、`dots-guide.html`、`chatgpt-space-guide.html`、`reference-guide.html`：六篇 Workflows 与 Features 专题学习页，可从 `index.html` 的官方课程目录进入。
- `styles.css`：全站基础视觉样式；`course.css`：课程页样式。

后续课程可沿用 `quickstart.html` 的页头、课程目录、正文和课程导航结构，并在首页学习路线中添加对应入口。

## 发布到 GitHub Pages

1. 在 GitHub 新建一个仓库，并将本地项目推送到仓库的 `main` 分支。
2. 打开仓库的 **Settings → Pages**。
3. 在 **Build and deployment** 里选择 **GitHub Actions**。
4. 推送到 `main` 后，工作流会发布网站。首次发布后可从 Pages 页面打开访问地址。

仓库名若为 `你的用户名.github.io`，网站会位于域名根路径；普通仓库会使用 `/仓库名/` 子路径，工作流会自动设置这个路径。

## 课程路线

- 熟悉工作区：认识项目、上下文和安全边界。
- 把想法说成好任务：拆解目标、补充上下文、迭代结果。
- 项目说明：使用 `AGENTS.md` 和可复用规则。
- 审查与交付：检查改动、验证结果、发布到 GitHub。
- 持续成长：在真实工作和团队协作中复盘。

## 内容原则

课程从真实任务开始，每节课明确练习目标、操作步骤、验收方式和复盘问题。Codex 的产品能力会持续变化，涉及具体界面或功能的课程应注明核对日期并定期更新。
