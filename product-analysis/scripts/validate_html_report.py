#!/usr/bin/env python3
"""Validate structural invariants of a local evidence-report HTML file."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path


class ReportParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []
        self.hrefs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.append(values["id"] or "")
        if values.get("href"):
            self.hrefs.append(values["href"] or "")


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        source = path.read_text(encoding="utf-8")
    except OSError as exc:
        return [f"cannot read {path}: {exc}"]

    parser = ReportParser()
    try:
        parser.feed(source)
    except Exception as exc:
        errors.append(f"HTML parse failure: {exc}")

    duplicates = sorted(value for value, count in Counter(parser.ids).items() if count > 1)
    if duplicates:
        errors.append(f"duplicate ids: {', '.join(duplicates)}")

    missing_anchors = sorted(
        href[1:] for href in parser.hrefs if href.startswith("#") and href[1:] not in parser.ids
    )
    if missing_anchors:
        errors.append(f"missing internal anchors: {', '.join(missing_anchors)}")

    missing_files: list[str] = []
    for href in parser.hrefs:
        if not href or href.startswith(("#", "http://", "https://", "mailto:", "tel:", "data:")):
            continue
        target = href.split("#", 1)[0].split("?", 1)[0]
        if target and not (path.parent / target).exists():
            missing_files.append(href)
    if missing_files:
        errors.append(f"missing local links: {', '.join(sorted(set(missing_files)))}")

    style_blocks = re.findall(r"<style\b[^>]*>(.*?)</style>", source, flags=re.I | re.S)
    for index, css in enumerate(style_blocks, start=1):
        if css.count("{") != css.count("}"):
            errors.append(f"unbalanced CSS braces in style block {index}")

    unfinished = sorted(set(re.findall(r"\b(?:TODO|TBD)\b|\[TODO[^\]]*\]", source, flags=re.I)))
    if unfinished:
        errors.append(f"unfinished scaffold markers: {', '.join(unfinished)}")

    if "<meta name=\"viewport\"" not in source and "<meta name='viewport'" not in source:
        errors.append("missing viewport meta tag")
    if not re.search(r"<html\b[^>]*\blang=", source, flags=re.I):
        errors.append("missing html lang attribute")
    if not re.search(r"<main\b", source, flags=re.I):
        errors.append("missing main landmark")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html", nargs="+", type=Path, help="HTML report(s) to validate")
    args = parser.parse_args()

    failed = False
    for path in args.html:
        errors = validate(path)
        if errors:
            failed = True
            print(f"FAIL {path}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"OK   {path}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())

