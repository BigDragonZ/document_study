from html import escape
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parent


def markdown_sources():
    return [
        ROOT / "README.md",
        ROOT / "SOURCES.md",
        *sorted((ROOT / "notes").glob("*.md")),
        *sorted((ROOT / "exercises").glob("*.md")),
    ]


def target_for(source):
    if source.name == "README.md":
        return ROOT / "index.html"
    return source.with_suffix(".html")


def page_title(text, source):
    first_line = text.splitlines()[0]
    return first_line.removeprefix("# ").strip() if first_line.startswith("# ") else source.stem


def html_links(markdown_text):
    def replace(match):
        label, url = match.groups()
        if url.startswith(("https://", "http://", "mailto:", "#")):
            return match.group(0)
        path, separator, fragment = url.partition("#")
        if not path.endswith(".md"):
            return match.group(0)
        html_path = f"{path[:-9]}index.html" if path.endswith("README.md") else f"{path[:-3]}.html"
        url = f"{html_path}{separator}{fragment}"
        return f"[{label}]({url})"

    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", replace, markdown_text)


def render(source):
    markdown_text = source.read_text(encoding="utf-8")
    title = page_title(markdown_text, source)
    result = subprocess.run(
        [
            "pandoc",
            "--from=gfm",
            "--to=html5",
            "--standalone",
            "--metadata",
            f"pagetitle={title}",
            "--metadata",
            "lang=zh-CN",
        ],
        input=html_links(markdown_text),
        text=True,
        capture_output=True,
        check=True,
    )
    depth = len(source.parent.relative_to(ROOT).parts)
    prefix = "../" * depth
    description = escape(f"Godot 4.7 官方文档中文学习资料：{title}", quote=True)
    head = (
        f'<meta name="description" content="{description}">\n'
        f'<link rel="stylesheet" href="{prefix}course.css">\n'
        "</head>"
    )
    navigation = (
        '<a class="skip-link" href="#content">跳到主要内容</a>\n'
        '<nav class="godot-nav" aria-label="Godot 学习导航">\n'
        f'<a href="{prefix}index.html">Godot 学习路线</a>\n'
        f'<a href="{prefix}../index.html">文档研习所首页</a>\n'
        f'<a href="{prefix}SOURCES.html">官方出处</a>\n'
        '</nav>\n'
        '<main id="content" class="godot-content">'
    )
    return result.stdout.replace("</head>", head).replace("<body>", f"<body>\n{navigation}", 1).replace("</body>", "</main>\n</body>", 1)


def main():
    for source in markdown_sources():
        target = target_for(source)
        target.write_text(render(source), encoding="utf-8")
        print(target.relative_to(ROOT))


if __name__ == "__main__":
    main()
