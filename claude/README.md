# Claude Code 实战手册

一份基于 [Claude Code 官方文档](https://code.claude.com/docs/en/overview) 整理的中文实战学习手册。从第一次安装和项目探索开始，逐步学习上下文、项目记忆、常见工作流、扩展、自动化、权限、安全与 Agent SDK。

本站是非官方学习项目，不代表 Anthropic。课程不是官方文档的逐页翻译；每个专题都提供官方原文入口与核对日期，产品功能、账号要求和预览状态以官方页面为准。

## 在学习中心使用

- **统一学习入口**：当前项目根目录的 `index.html`。
- **本手册入口**：`claude/index.html`。
- **项目使用说明**：当前项目根目录的 `README.md`。

## 使用要求

阅读网站只需要一个支持 HTML5、CSS3 和 JavaScript 的现代浏览器，无需安装 Claude Code、Node.js 或任何网站依赖。

以下工具均为可选：

- **Python 3**：用于启动本地 HTTP 预览。
- **Git 与 GitHub CLI (`gh`)**：仅在你要 fork、提交或发布本项目时需要。
- **Claude Code 与对应账号**：仅在你准备亲手完成课程中的安装、终端和 SDK 练习时需要，账号要求见各课官方来源。

## 本地预览

### 方式一：直接打开

在文件管理器中打开 `claude/index.html`。全部 12 个页面、课程导航和样式都可离线使用；在线字体加载失败时会回退到系统字体。

### 方式二：HTTP 预览（推荐）

在学习中心根目录执行：

```bash
cd /Users/naihe/Documents/document_study
python3 -m http.server 8000
```

然后打开 `http://127.0.0.1:8000/claude/index.html`。验证结束后，在终端按 `Ctrl+C` 停止服务器。

通过 HTTP 预览时，复制按钮使用浏览器 Clipboard API。首次点击可能弹出 `clipboardWrite` 权限请求，需要由你允许；如果浏览器拒绝权限或不支持自动复制，页面会提示你手动选择并复制文字。

## 如何使用课程

1. **先浏览首页**：从“先让 Claude 读懂你的项目”开始，复制第一条只读任务。
2. **按顺序完成入门练习**：依次学习任务表达、CLAUDE.md 项目记忆和证据化交付。
3. **进入专题课程**：推荐从 `quickstart.html` 开始，按每页底部的“下一课”继续；也可以从首页的 11 个专题目录按需求跳转。
4. **完成实战练习**：每课末尾都有操作步骤和完成标准。先在小项目或练习仓库中操作，不要直接对重要工作执行高风险示例。
5. **核对官方原文**：涉及安装命令、权限、套餐、平台限制和 SDK API 时，打开该页“官方来源”确认最新行为。

课程中的命令和配置仅供学习，不会在打开网页时自动执行。本站也不需要你填写账号、API key 或其他凭据。

## 课程地图

- `index.html`：首页、四个入门练习、学习路线与专题目录。
- `quickstart.html`：安装、登录、首次会话与第一次小改动。
- `concepts.html`：Agentic loop、工具、执行环境、上下文、会话与检查点。
- `memory.html`：CLAUDE.md、auto memory、规则作用域与项目指令。
- `workflows.html`：探索、调试、重构、测试、Plan Mode、审查与 PR。
- `extensions.html`：Skills、Subagents、MCP、Hooks 与 Plugins。
- `platforms.html`：CLI、IDE、Desktop、Web、Mobile 与外部集成。
- `automation.html`：并行 agents、worktrees、非交互 CLI、定时任务与 CI/CD。
- `configuration.html`：设置层级、权限模式、权限规则、沙箱与模型配置。
- `security-guide.html`：提示注入、秘密、插件信任、云端、数据与团队治理。
- `reference-guide.html`：常用 CLI、会话命令、快捷键、自动化参数与排障。
- `agent-sdk.html`：Python / TypeScript Agent SDK、工具、会话、权限与部署。

## 文件结构

本手册当前位于 `/Users/naihe/Documents/document_study/claude/`。

- `styles.css`：首页与全站基础视觉样式。
- `course.css`：课程 Hero、侧栏、正文、代码卡、练习与来源组件。
- `script.js`：首页任务和课程代码的复制交互与降级反馈。
- `../.github/workflows/pages.yml`：学习中心根目录的 GitHub Pages 静态发布工作流。

## 在其他项目复用学习 Skill

官方文档学习技能安装在用户级 `~/.claude/skills/learning-official-docs/`，所有项目共享，不应放入某个项目的 `.claude/skills/`。当前学习中心也直接使用这份用户级技能。技能包含主流程、课程契约、验证清单和评估场景。

在其他机器安装时，将备份或源码包中的整个 `learning-official-docs/` 目录复制到 `~/.claude/skills/`，并保持 `SKILL.md`、`references/` 和 `evaluations.md` 的相对位置。当任务涉及研究官方文档、整理学习笔记、制作课程或迁移现有手册时，使用该技能；修改技能后先运行其中的评估场景。

## 内容维护原则

- 修改课程内容前，先核对对应官方 `.md` 文档，不以其他 AI 编程工具的术语或行为替代 Claude Code。
- 保留官方来源与核对日期；套餐、平台、模型和研究预览功能要注明适用边界。
- 区分官方事实与手册实战建议，不把教学示例写成已替读者执行的操作。
- 权限、自动化和外部集成示例默认从只读和最小范围开始，不推荐绕过安全检查。
- 修改页面后检查 HTML 结构、站内文件与锚点、复制按钮、桌面和移动端布局。

## 发布到 GitHub Pages

1. 在 GitHub 新建仓库，并将本项目推送到 `main` 分支。
2. 打开仓库 **Settings → Pages**。
3. 在 **Build and deployment** 中选择 **GitHub Actions**。
4. 推送到 `main` 后，工作流会发布网站；也可以手动运行工作流。

普通仓库会使用 `/<仓库名>/` 子路径，本站全部站内资源使用相对路径，无需修改 base URL。部署后还要实际打开 Pages 地址，检查首页、课程链接和复制交互。
