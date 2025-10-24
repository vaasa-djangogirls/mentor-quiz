#!/usr/bin/env python3
"""Convert an EPUB into standalone, mobile-friendly HTML pages with navigation."""

from __future__ import annotations

import argparse
import posixpath
import re
import shutil
import textwrap
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Sequence, Tuple
import xml.etree.ElementTree as ET

NS = {
    "container": "urn:oasis:names:tc:opendocument:xmlns:container",
    "opf": "http://www.idpf.org/2007/opf",
    "dc": "http://purl.org/dc/elements/1.1/",
    "xhtml": "http://www.w3.org/1999/xhtml",
}

HTML_NS_ATTR_RE = re.compile(r'\s+xmlns(?::\w+)?="http://www.w3.org/1999/xhtml"')
RELATIVE_PREFIX_BLOCKLIST = (
    "#",
    "?",
    "/",
    "//",
    "http://",
    "https://",
    "mailto:",
    "tel:",
    "data:",
    "javascript:",
)

SRC_TAGS = {"img", "script", "iframe", "audio", "video", "embed"}
SRCSET_TAGS = {"img", "source"}
HREF_TAGS = {"link"}
DATA_TAGS = {"object"}


@dataclass
class PageData:
    title: str
    metas_html: str
    head_html: str
    body_html: str
    output_name: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert an EPUB into HTML pages with previous/next links."
    )
    parser.add_argument(
        "epub_path",
        type=Path,
        help="Path to the EPUB file (e.g. django-girls-tutorial_en.epub).",
    )
    parser.add_argument(
        "output_dir",
        type=Path,
        nargs="?",
        default=Path("docs/tutorial"),
        help="Directory to write the generated HTML pages into (default: ./docs/tutorial).",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Delete the output directory before converting.",
    )
    return parser.parse_args()


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-{2,}", "-", value)
    return value.strip("-") or "page"


def read_container(zip_file: zipfile.ZipFile) -> str:
    container_xml = zip_file.read("META-INF/container.xml")
    container = ET.fromstring(container_xml)
    rootfile = container.find("container:rootfiles/container:rootfile", NS)
    if rootfile is None:
        raise RuntimeError("EPUB container is missing <rootfile> information.")
    return rootfile.attrib["full-path"]


def parse_opf(zip_file: zipfile.ZipFile, opf_path: str) -> Tuple[Dict[str, Dict[str, str]], List[str]]:
    opf_xml = zip_file.read(opf_path)
    package = ET.fromstring(opf_xml)

    manifest_elem = package.find("opf:manifest", NS)
    if manifest_elem is None:
        raise RuntimeError("EPUB manifest is missing.")

    manifest: Dict[str, Dict[str, str]] = {}
    for item in manifest_elem.findall("opf:item", NS):
        manifest[item.attrib["id"]] = item.attrib

    spine_elem = package.find("opf:spine", NS)
    if spine_elem is None:
        raise RuntimeError("EPUB spine is missing.")

    spine_ids = [item.attrib["idref"] for item in spine_elem.findall("opf:itemref", NS)]
    return manifest, spine_ids


def strip_xhtml_namespaces(fragment: str) -> str:
    fragment = fragment.replace("html:", "")
    fragment = HTML_NS_ATTR_RE.sub("", fragment)
    return fragment


def local_tag(tag: str) -> str:
    """Return the local part of a potentially namespaced tag."""
    return tag.split("}", 1)[-1]


def should_rewrite_path(value: str) -> bool:
    if not value:
        return False
    for prefix in RELATIVE_PREFIX_BLOCKLIST:
        if value.startswith(prefix):
            return False
    if ":" in value.split("/", 1)[0]:
        # Likely a scheme (e.g. ftp:, about:) we shouldn't modify.
        return False
    return True


def resolve_resource_path(value: str, parent_dir: str) -> str | None:
    if not should_rewrite_path(value):
        return None
    combined = posixpath.normpath(posixpath.join(parent_dir, value))
    if combined.startswith("../"):
        # Outside the EPUB root; leave untouched.
        return None
    if combined in (".", ""):
        result = "content"
    else:
        result = f"content/{combined}"
    if value.endswith("/") and not result.endswith("/"):
        result = f"{result}/"
    return result


def rewrite_srcset(value: str, parent_dir: str) -> str:
    rewritten: List[str] = []
    for entry in value.split(","):
        entry = entry.strip()
        if not entry:
            continue
        if " " in entry:
            url, descriptor = entry.split(None, 1)
        else:
            url, descriptor = entry, ""
        new_url = resolve_resource_path(url, parent_dir)
        if new_url:
            url = new_url
        rewritten.append(f"{url} {descriptor}".strip())
    return ", ".join(rewritten)


def adjust_resource_paths(head: ET.Element | None, body: ET.Element | None, parent_dir: str) -> None:
    for section in filter(None, (head, body)):
        for node in section.iter():
            tag_name = local_tag(node.tag)
            if tag_name in HREF_TAGS and "href" in node.attrib:
                new_value = resolve_resource_path(node.attrib["href"], parent_dir)
                if new_value:
                    node.set("href", new_value)
            if tag_name in SRC_TAGS and "src" in node.attrib:
                new_value = resolve_resource_path(node.attrib["src"], parent_dir)
                if new_value:
                    node.set("src", new_value)
            if tag_name in SRCSET_TAGS and "srcset" in node.attrib:
                node.set("srcset", rewrite_srcset(node.attrib["srcset"], parent_dir))
            if tag_name in DATA_TAGS and "data" in node.attrib:
                new_value = resolve_resource_path(node.attrib["data"], parent_dir)
                if new_value:
                    node.set("data", new_value)


def build_head_chunks(head: ET.Element) -> Tuple[str, str, str]:
    title_text = "Untitled"
    additional_parts: List[str] = []
    metas: List[str] = []

    for child in head:
        tag_name = local_tag(child.tag)
        if tag_name == "title":
            if child.text:
                title_text = child.text.strip()
            continue
        if tag_name == "base":
            continue
        serialized = ET.tostring(child, encoding="unicode", method="html")
        serialized = strip_xhtml_namespaces(serialized)
        if tag_name == "meta":
            metas.append(serialized)
        else:
            additional_parts.append(serialized)

    return title_text, "".join(metas), "".join(additional_parts)


def extract_body_inner(body: ET.Element) -> str:
    parts: List[str] = []
    for child in body:
        serialized = ET.tostring(child, encoding="unicode", method="html")
        parts.append(strip_xhtml_namespaces(serialized))
    return "".join(parts)


def ensure_destination(output_dir: Path, force: bool) -> None:
    if output_dir.exists():
        if not force:
            raise SystemExit(
                f"Output directory {output_dir} already exists. Use --force to overwrite."
            )
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)


def write_css(output_dir: Path) -> None:
    css = textwrap.dedent(
        """
        :root {
            color-scheme: light;
            font-size: 16px;
        }
        body {
            margin: 0;
            min-height: 100vh;
            font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
            color: #202124;
            background: #f5f7fb;
            line-height: 1.7;
            font-size: clamp(1rem, 0.98rem + 0.3vw, 1.1rem);
            display: flex;
            flex-direction: column;
        }
        body > header,
        body > nav.book-nav,
        body > main,
        body > footer {
            width: min(960px, 92vw);
            margin: 0 auto;
        }
        body > header,
        body > footer {
            padding: clamp(1rem, 3vw, 1.75rem) 0;
        }
        header.book-header h1 {
            margin: 0 0 0.35rem;
            font-size: clamp(2rem, 4vw, 2.5rem);
        }
        header.book-header p {
            margin: 0;
            color: #4b5c6b;
        }
        nav.book-nav {
            display: flex;
            flex-wrap: wrap;
            gap: 0.75rem;
            margin: 0 0 clamp(1.25rem, 4vw, 2rem);
            padding-bottom: clamp(0.5rem, 2vw, 1rem);
        }
        nav.book-nav a,
        nav.book-nav span {
            padding: 0.55rem 1.15rem;
            border-radius: 999px;
            border: 1px solid #3b6b9a;
            text-decoration: none;
            color: #1a4d7a;
            background: #e6f0fb;
            font-weight: 600;
            transition: background 0.15s ease, box-shadow 0.15s ease;
            min-width: 9rem;
            text-align: center;
            box-shadow: 0 1px 6px rgba(59, 107, 154, 0.15);
        }
        nav.book-nav span {
            color: #7a8699;
            border-color: #c7d3e3;
            background: #eef2f9;
            box-shadow: none;
        }
        nav.book-nav a:hover,
        nav.book-nav a:focus-visible {
            background: #d7e8fb;
            box-shadow: 0 3px 12px rgba(59, 107, 154, 0.25);
        }
        main {
            flex: 1;
            background: #ffffff;
            padding: clamp(1.5rem, 4vw, 2.6rem);
            border-radius: 12px;
            box-shadow: 0 16px 40px rgba(15, 23, 42, 0.08);
            margin-bottom: clamp(1.5rem, 5vw, 2.5rem);
        }
        main > :first-child {
            margin-top: 0;
        }
        main > :last-child {
            margin-bottom: 0;
        }
        img,
        video,
        iframe {
            max-width: 100%;
            height: auto;
            border-radius: 6px;
        }
        pre {
            overflow-x: auto;
            background: #0f172a;
            color: #e2e8f0;
            padding: 1rem;
            border-radius: 8px;
            font-size: 0.95rem;
        }
        code {
            font-family: "Fira Code", "SFMono-Regular", Menlo, Consolas, monospace;
        }
        blockquote {
            border-left: 4px solid #c8d9ee;
            padding-left: 1rem;
            margin: 1.5rem 0;
            color: #475569;
            background: #f1f6fd;
        }
        .toc-list {
            list-style: none;
            padding: 0;
            margin: 2rem 0;
            display: grid;
            gap: 0.75rem;
        }
        .toc-list a {
            text-decoration: none;
            color: #194877;
            font-weight: 600;
        }
        footer.book-footer {
            margin-top: auto;
            font-size: 0.9rem;
            color: #5f6368;
            text-align: center;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 1.5rem 0;
        }
        table,
        th,
        td {
            border: 1px solid #c7d3e3;
        }
        th,
        td {
            padding: 0.65rem;
            text-align: left;
        }
        @media (max-width: 720px) {
            nav.book-nav {
                flex-direction: column;
                align-items: stretch;
            }
            nav.book-nav a,
            nav.book-nav span {
                width: 100%;
                min-width: 0;
            }
        }
        @media (max-width: 600px) {
            body > header,
            body > nav.book-nav,
            body > main,
            body > footer {
                width: min(640px, 94vw);
            }
            main {
                padding: clamp(1.1rem, 5vw, 1.6rem);
                border-radius: 10px;
            }
        }
        """
    ).strip()
    (output_dir / "book.css").write_text(css, encoding="utf-8")


def build_navigation(prev_link: str | None, next_link: str | None) -> str:
    parts = ['<nav class="book-nav">']
    parts.append('<a href="index.html">Contents</a>')
    if prev_link:
        parts.append(f'<a href="{prev_link}">Previous</a>')
    else:
        parts.append("<span>Previous</span>")
    if next_link:
        parts.append(f'<a href="{next_link}">Next</a>')
    else:
        parts.append("<span>Next</span>")
    parts.append("</nav>")
    return "".join(parts)


def render_page(
    title: str,
    metas_html: str,
    head_html: str,
    body_html: str,
    prev_link: str | None,
    next_link: str | None,
) -> str:
    navigation_top = textwrap.indent(build_navigation(prev_link, next_link), "    ")
    navigation_bottom = textwrap.indent(build_navigation(prev_link, next_link), "    ")
    body_compact = body_html.strip("\n")
    indented_body = textwrap.indent(body_compact, "        ") if body_compact else ""
    template = f"""\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{title}</title>
    <link rel="stylesheet" href="book.css" />
    {metas_html}{head_html}
</head>
<body>
    <header class="book-header">
        <h1>{title}</h1>
    </header>
{navigation_top}
    <main>
{indented_body}
    </main>
{navigation_bottom}
    <footer class="book-footer">
        <p>Generated from the original EPUB. Content © respective authors under CC BY-SA 4.0.</p>
    </footer>
</body>
</html>
"""
    return template.strip()


def render_index(chapters: Sequence[Tuple[str, str]]) -> str:
    items = "\n".join(f'        <li><a href="{output_file}">{title}</a></li>' for title, output_file in chapters)
    navigation = textwrap.indent(build_navigation(None, chapters[0][1] if chapters else None), "    ")
    template = f"""\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Django Girls Tutorial – HTML Edition</title>
    <link rel="stylesheet" href="book.css" />
</head>
<body>
    <header class="book-header">
        <h1>Django Girls Tutorial</h1>
        <p>Converted into navigable HTML pages.</p>
    </header>
{navigation}
    <main>
        <h2>Table of Contents</h2>
        <ul class="toc-list">
{items}
        </ul>
    </main>
    <footer class="book-footer">
        <p>Generated from the original EPUB. Content © respective authors under CC BY-SA 4.0.</p>
    </footer>
</body>
</html>
"""
    return template.strip()


def convert(epub_path: Path, output_dir: Path, force: bool) -> None:
    ensure_destination(output_dir, force)
    content_root = output_dir / "content"
    content_root.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(epub_path) as zip_file:
        opf_path = read_container(zip_file)
        manifest, spine_ids = parse_opf(zip_file, opf_path)
        zip_file.extractall(content_root)

    write_css(output_dir)

    pages: List[PageData] = []
    base_dir = Path(opf_path).parent

    for index, item_id in enumerate(spine_ids, start=1):
        manifest_item = manifest.get(item_id)
        if not manifest_item:
            continue
        media_type = manifest_item.get("media-type", "")
        if media_type not in ("application/xhtml+xml", "text/html"):
            continue
        href = manifest_item["href"]
        source_rel = Path(base_dir, href).as_posix() if base_dir else href
        source_path = content_root / source_rel
        if not source_path.exists():
            continue

        xml_content = source_path.read_bytes()
        try:
            document = ET.fromstring(xml_content)
        except ET.ParseError as exc:
            raise RuntimeError(f"Failed to parse {source_rel}: {exc}") from exc

        head = document.find("xhtml:head", NS)
        body = document.find("xhtml:body", NS)
        if head is None or body is None:
            continue

        parent_posix = Path(source_rel).parent.as_posix()
        resource_parent = "" if parent_posix in ("", ".") else parent_posix
        adjust_resource_paths(head, body, resource_parent)

        title_text, metas_html, head_html = build_head_chunks(head)
        body_html = extract_body_inner(body)

        slug = slugify(title_text or Path(href).stem)
        output_name = f"{index:03d}-{slug}.html"

        pages.append(
            PageData(
                title=title_text or f"Chapter {index}",
                metas_html=metas_html,
                head_html=head_html,
                body_html=body_html,
                output_name=output_name,
            )
        )

    if not pages:
        raise RuntimeError("No XHTML content found in the EPUB spine.")

    for idx, page in enumerate(pages):
        prev_link = pages[idx - 1].output_name if idx > 0 else None
        next_link = pages[idx + 1].output_name if idx + 1 < len(pages) else None
        html_text = render_page(
            title=page.title,
            metas_html=page.metas_html,
            head_html=page.head_html,
            body_html=page.body_html,
            prev_link=prev_link,
            next_link=next_link,
        )
        (output_dir / page.output_name).write_text(html_text, encoding="utf-8")

    chapters_meta = [(page.title, page.output_name) for page in pages]
    index_html = render_index(chapters_meta)
    (output_dir / "index.html").write_text(index_html, encoding="utf-8")


def main() -> None:
    args = parse_args()
    convert(args.epub_path, args.output_dir, args.force)


if __name__ == "__main__":
    main()
