#!/usr/bin/env python3
"""Extract DOCX body views, tracked changes and anchored comments read-only."""

from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


W_URI = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
W = f"{{{W_URI}}}"
WORD_RE = re.compile(r"\b[A-Za-z0-9]+(?:[’'-][A-Za-z0-9]+)*\b")


class ReviewError(Exception):
    """Raised for concise user-facing extraction failures."""


def wattr(node: ET.Element, name: str) -> str:
    return node.attrib.get(W + name, "")


def plain_text(node: ET.Element) -> str:
    """Return text from a subtree, including deleted text."""
    parts: list[str] = []
    for item in node.iter():
        if item.tag in (W + "t", W + "delText"):
            parts.append(item.text or "")
        elif item.tag == W + "tab":
            parts.append("\t")
        elif item.tag in (W + "br", W + "cr"):
            parts.append("\n")
    return "".join(parts)


def render_node(node: ET.Element, mode: str) -> str:
    """Render an element for accepted, rejected, or all-change views."""
    if node.tag in (W + "t", W + "delText"):
        return node.text or ""
    if node.tag == W + "tab":
        return "\t"
    if node.tag in (W + "br", W + "cr"):
        return "\n"

    if node.tag == W + "ins":
        inserted = "".join(render_node(child, "accepted") for child in node)
        if mode == "rejected":
            return ""
        return f"{{+{inserted}+}}" if mode == "all" and inserted else inserted

    if node.tag == W + "del":
        deleted = plain_text(node)
        if mode == "accepted":
            return ""
        return f"[-{deleted}-]" if mode == "all" and deleted else deleted

    return "".join(render_node(child, mode) for child in node)


def extract_paragraphs(root: ET.Element) -> dict[str, list[str]]:
    views: dict[str, list[str]] = {"accepted": [], "rejected": [], "all": []}
    for paragraph in root.iter(W + "p"):
        for mode in views:
            rendered = render_node(paragraph, mode).strip()
            if rendered:
                views[mode].append(rendered)
    return views


def extract_changes(root: ET.Element) -> list[dict[str, str]]:
    changes: list[dict[str, str]] = []
    for node in root.iter():
        if node.tag not in (W + "ins", W + "del"):
            continue
        content = plain_text(node)
        if content:
            changes.append(
                {
                    "kind": "insertion" if node.tag == W + "ins" else "deletion",
                    "author": wattr(node, "author"),
                    "date": wattr(node, "date"),
                    "text": content,
                }
            )
    return changes


def comment_bodies(root: ET.Element | None) -> dict[str, dict[str, str]]:
    if root is None:
        return {}
    bodies: dict[str, dict[str, str]] = {}
    for comment in root.findall(W + "comment"):
        paragraphs = [plain_text(p).strip() for p in comment.iter(W + "p")]
        bodies[wattr(comment, "id")] = {
            "author": wattr(comment, "author"),
            "date": wattr(comment, "date"),
            "text": "\n".join(p for p in paragraphs if p),
        }
    return bodies


def comment_anchors(document_root: ET.Element) -> dict[str, str]:
    active: set[str] = set()
    chunks: dict[str, list[str]] = {}

    def walk(node: ET.Element) -> None:
        if node.tag == W + "commentRangeStart":
            comment_id = wattr(node, "id")
            active.add(comment_id)
            chunks.setdefault(comment_id, [])
            return
        if node.tag == W + "commentRangeEnd":
            active.discard(wattr(node, "id"))
            return
        if node.tag in (W + "t", W + "delText"):
            for comment_id in active:
                chunks.setdefault(comment_id, []).append(node.text or "")
            return
        if node.tag == W + "tab":
            for comment_id in active:
                chunks.setdefault(comment_id, []).append("\t")
            return
        if node.tag in (W + "br", W + "cr"):
            for comment_id in active:
                chunks.setdefault(comment_id, []).append("\n")
            return
        for child in node:
            walk(child)
        if node.tag == W + "p":
            for comment_id in active:
                chunks.setdefault(comment_id, []).append(" ")

    walk(document_root)
    return {key: "".join(value).strip() for key, value in chunks.items()}


def id_sort_key(value: str) -> tuple[int, int | str]:
    try:
        return (0, int(value))
    except ValueError:
        return (1, value)


def extract_comments(
    document_root: ET.Element, comments_root: ET.Element | None
) -> list[dict[str, str]]:
    bodies = comment_bodies(comments_root)
    anchors = comment_anchors(document_root)
    ids = sorted(set(bodies) | set(anchors), key=id_sort_key)
    return [
        {
            "id": comment_id,
            "author": bodies.get(comment_id, {}).get("author", ""),
            "date": bodies.get(comment_id, {}).get("date", ""),
            "text": bodies.get(comment_id, {}).get("text", ""),
            "anchor": anchors.get(comment_id, ""),
        }
        for comment_id in ids
    ]


def count_words(paragraphs: list[str]) -> int:
    """Count English-style tokens; PS drafts are normally written in English."""
    return len(WORD_RE.findall(" ".join(paragraphs)))


def read_xml(
    archive: zipfile.ZipFile, name: str, *, required: bool
) -> ET.Element | None:
    try:
        raw = archive.read(name)
    except KeyError:
        if required:
            raise ReviewError(f"DOCX is missing required part: {name}") from None
        return None
    try:
        return ET.fromstring(raw)
    except ET.ParseError as exc:
        raise ReviewError(f"Invalid XML in {name}: {exc}") from exc


def extract_review(path: Path) -> dict[str, object]:
    if not path.is_file():
        raise ReviewError(f"File not found: {path}")
    if path.suffix.lower() != ".docx":
        raise ReviewError(f"Expected a .docx file: {path}")
    try:
        with zipfile.ZipFile(path) as archive:
            document_root = read_xml(archive, "word/document.xml", required=True)
            comments_root = read_xml(archive, "word/comments.xml", required=False)
    except zipfile.BadZipFile as exc:
        raise ReviewError(f"Not a valid DOCX archive: {path}") from exc

    assert document_root is not None
    paragraphs = extract_paragraphs(document_root)
    return {
        "source": str(path.resolve()),
        "word_counts": {mode: count_words(items) for mode, items in paragraphs.items()},
        "paragraphs": paragraphs,
        "comments": extract_comments(document_root, comments_root),
        "changes": extract_changes(document_root),
    }


def md_escape(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", "<br>")


def to_markdown(review: dict[str, object]) -> str:
    counts = review["word_counts"]
    paragraphs = review["paragraphs"]
    comments = review["comments"]
    changes = review["changes"]
    assert isinstance(counts, dict)
    assert isinstance(paragraphs, dict)
    assert isinstance(comments, list)
    assert isinstance(changes, list)

    lines = [f"# DOCX review: {Path(str(review['source'])).name}", ""]
    lines.extend(["## Word counts", "", "| View | Words |", "| --- | ---: |"])
    lines.extend(f"| {mode} | {count} |" for mode, count in counts.items())
    lines.append("")
    for mode in ("accepted", "rejected", "all"):
        lines.extend([f"## {mode.title()} text", ""])
        for paragraph in paragraphs[mode]:
            lines.extend([str(paragraph), ""])

    lines.extend(
        [
            "## Comments",
            "",
            "| ID | Author | Date | Anchor | Comment |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in comments:
        assert isinstance(item, dict)
        fields = {key: md_escape(value) for key, value in item.items()}
        lines.append(
            "| {id} | {author} | {date} | {anchor} | {text} |".format(**fields)
        )

    lines.extend(
        [
            "",
            "## Tracked changes",
            "",
            "| Kind | Author | Date | Text |",
            "| --- | --- | --- | --- |",
        ]
    )
    for item in changes:
        assert isinstance(item, dict)
        fields = {key: md_escape(value) for key, value in item.items()}
        lines.append("| {kind} | {author} | {date} | {text} |".format(**fields))
    return "\n".join(lines).rstrip() + "\n"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Extract DOCX body views, tracked changes and anchored comments."
    )
    parser.add_argument("input", type=Path, help="Input .docx file")
    parser.add_argument(
        "--format", choices=("json", "markdown"), default="json", dest="fmt"
    )
    parser.add_argument("-o", "--output", type=Path, help="UTF-8 output file")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        review = extract_review(args.input)
        output = (
            json.dumps(review, ensure_ascii=False, indent=2) + "\n"
            if args.fmt == "json"
            else to_markdown(review)
        )
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(output, encoding="utf-8")
        else:
            if hasattr(sys.stdout, "reconfigure"):
                sys.stdout.reconfigure(encoding="utf-8")
            sys.stdout.write(output)
    except (OSError, ReviewError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

