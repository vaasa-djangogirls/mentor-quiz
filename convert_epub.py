#!/usr/bin/env python3
"""Convert an EPUB into standalone HTML pages with navigation."""

from __future__ import annotations

import argparse
import os
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


def build_head_chunks(head: ET.Element) -> Tuple[str, str, str]:
    title_text = "Untitled"
    additional_parts: List[str] = []
    metas: List[str] = []

    for child in head:
        tag_name = child.tag.split("}", 1)[-1]
        if tag_name == "title":
            if child.text:
                title_text = child.text.strip()
            continue
        if tag_name == "base":
            # We'll inject our own <base>.
            continue
        serialized = ET.tostring(child, encoding="unicode", method="html")
        serialized = strip_xhtml_namespaces(serialized)
        if tag_name == "meta":
            metas.append(serialized)
        else:
            additional_parts.append(serialized)

    return title_text, "".join(metas), "".join(additional_parts)


def extract_body_inner(body: ET.Element) -> str:
    parts = []
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
        body {
            font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
            margin: 0 auto;
            padding: 1rem 1.5rem 3rem;
            max-width: 960px;
            line-height: 1.6;
            color: #202124;
            background: #fafafa;
        }
        main {
            background: #ffffff;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
        }
        nav.book-nav {
            display: flex;
            flex-wrap: wrap;
            gap: 0.75rem;
            margin: 1.5rem 0;
        }
        nav.book-nav a,
        nav.book-nav span {
            padding: 0.4rem 0.95rem;
            border-radius: 999px;
            border: 1px solid #3b6b9a;
            text-decoration: none;
            color: #1a4d7a;
            background: #e6f0fb;
            font-weight: 600;
        }
        nav.book-nav span {
            color: #7a8699;
            border-color: #c7d3e3;
            background: #eef2f9;
        }
        nav.book-nav a:hover {
            background: #d7e8fb;
        }
        .toc-list {
            list-style: none;
            padding: 0;
            margin: 2rem 0;
        }
        .toc-list li {
            margin-bottom: 0.75rem;
        }
        .toc-list a {
            text-decoration: none;
            color: #194877;
            font-weight: 600;
        }
        header.book-header h1 {
            margin: 0;
        }
        footer.book-footer {
            margin-top: 3rem;
            font-size: 0.85rem;
            color: #5f6368;
            text-align: center;
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


@dataclass
class PageData:
    title: str
    metas_html: str
    head_html: str
    body_html: str
    base_href: str
    output_name: str


def render_page(
    title: str,
    base_href: str,
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
    <title>{title}</title>
    <base href="{base_href}" />
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
    next_link = chapters[0][1] if chapters else None
    navigation = textwrap.indent(build_navigation(None, next_link), "    ")
    template = f"""\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8" />
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

        title_text, metas_html, head_html = build_head_chunks(head)
        body_html = extract_body_inner(body)

        slug = slugify(title_text or Path(href).stem)
        output_name = f"{index:03d}-{slug}.html"

        parent_posix = Path(source_rel).parent.as_posix()
        if parent_posix in ("", "."):
            base_href = "content/"
        else:
            base_href = f"content/{parent_posix}/"

        pages.append(
            PageData(
                title=title_text or f"Chapter {index}",
                metas_html=metas_html,
                head_html=head_html,
                body_html=body_html,
                base_href=base_href,
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
            base_href=page.base_href,
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
