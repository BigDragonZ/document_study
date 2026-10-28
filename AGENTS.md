# AGENTS.md

## 项目目标

当前项目是专门学习官方文档的长期学习中心。统一入口是根目录 `index.html`，三套资料分别位于 `claude/`、`codex/` 和 `godot/`。

## 技术与预览

- 根入口和两套手册使用原生 HTML、CSS、JavaScript；Godot 保留 Markdown 原稿，并提供对应的 HTML 阅读页。
- 不引入前端框架、包管理器或测试脚手架。
- 修改 Godot Markdown 后运行 `python3 godot/generate.py` 重新生成 HTML；生成需要本机已有 Pandoc，阅读网页不需要 Pandoc。
- 在项目根目录运行 `python3 -m http.server 8000`，访问 `http://127.0.0.1:8000/index.html`。
- 根目录只保留一个 `.github/workflows/pages.yml`；不复制嵌套 Git 仓库或子项目发布工作流。

## 内容与结构约定

- 保留各子项目的目录隔离、视觉风格、产品术语和相对链接，不因合并而统一改写课程。
- 修改 `claude/` 或 `codex/` 时，同时遵守该目录的 `AGENTS.md`。
- 课程事实以当前官方文档为依据，保留官方 URL 和实际核对日期；区分官方事实与手册建议。
- 练习应可操作、可验证，默认只读、小范围、可恢复；不声称执行过未实际运行的示例。
- 网页交付前检查本地文件与锚点、HTML 结构、复制交互、桌面和移动端布局。

## 学习技能维护

- 官方文档学习使用用户级 `/Users/naihe/.claude/skills/learning-official-docs/`，项目中不复制第二份技能。
- 学习交付后根据真实经历复盘；仅将可复用的问题转化为最小技能改进。
- 修改技能时同步更新 `evaluations.md`，修改前后运行适用场景，并如实说明评估限制。

## 操作边界

不擅自初始化 Git、提交、推送或部署。涉及这些操作时，需要用户另行明确要求。
