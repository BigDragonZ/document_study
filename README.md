# 文档研习所

当前项目用于持续学习官方文档，把官方资料整理成中文学习手册、笔记和可操作的练习。现有内容包括 Claude Code、Codex 和 Godot 三条学习路线；这些资料均为非官方学习成果，产品行为、版本和适用限制以官方原文为准。

- **在线阅读**：<https://bigdragonz.github.io/document_study/>
- **GitHub 仓库**：<https://github.com/BigDragonZ/document_study>

## 学习入口

| 路线 | 入口 | 形式 |
| --- | --- | --- |
| Claude Code | [实战手册](claude/index.html) | 11 个专题，涵盖入门、上下文、工作流、扩展、自动化和安全 |
| Codex | [实战手册](codex/index.html) | 11 个专题，涵盖入门、基础、配置、工作流、开发者功能和安全 |
| Godot 4.7 | [学习路线](godot/index.html) | 6 篇笔记与 4 个渐进式练习，使用 GDScript |

根目录的 `index.html` 是统一学习入口。两套手册保留各自的视觉和交互；Godot 同时保留 Markdown 原稿与 HTML 阅读页，网页入口为 `godot/index.html`。

## 本地预览

直接在浏览器打开根目录的 `index.html`，或在当前项目运行：

```bash
cd /Users/naihe/Documents/document_study
python3 -m http.server 8000
```

然后访问 `http://127.0.0.1:8000/index.html`。验证结束后按 `Ctrl+C` 停止服务器。

## 持续学习与技能改进

研究新的官方文档、整理笔记、制作课程或迁移学习项目时，使用用户级技能：

```text
/Users/naihe/.claude/skills/learning-official-docs/
```

技能在所有项目中共享，不在本项目中另存副本。每次学习交付后，根据真实经历复盘：只有可复用的问题才转化为技能规则或评估场景；修改技能前后运行 `evaluations.md` 中的场景，不为追求改动数量而扩写。

## 内容维护

- 修改课程事实前核对官方原文，保留来源链接和实际核对日期。
- 区分官方事实与学习建议，练习默认只读、小范围、可恢复。
- 修改子目录时阅读其中的 `AGENTS.md`，保留各项目原有约定。
- 修改 Godot Markdown 后运行 `python3 godot/generate.py` 重新生成 HTML；该命令需要本机已有 Pandoc。
- 修改网页后检查链接、锚点、交互和移动端布局。
- 提交、推送和发布需要另行明确授权。
