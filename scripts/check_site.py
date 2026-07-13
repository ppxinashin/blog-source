#!/usr/bin/env python3
"""Validate the generated Hugo site without third-party dependencies."""

from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse


SITE_ORIGIN = "https://www.jehol-ppx.com"


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.canonical: str | None = None
        self.description: str | None = None
        self.ids: list[str] = []
        self.lang: str | None = None
        self.references: list[tuple[str, str]] = []
        self.title_parts: list[str] = []
        self.in_title = False
        self.is_redirect = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "html":
            self.lang = values.get("lang")
        if tag == "title":
            self.in_title = True
        if values.get("id"):
            self.ids.append(values["id"])
        if tag == "link" and values.get("rel") == "canonical":
            self.canonical = values.get("href")
        if tag == "meta" and values.get("name") == "description":
            self.description = values.get("content")
        if tag == "meta" and values.get("http-equiv", "").lower() == "refresh":
            self.is_redirect = True
        for attribute in ("href", "src"):
            if values.get(attribute):
                self.references.append((attribute, values[attribute]))
        if values.get("srcset"):
            for candidate in values["srcset"].split(","):
                url = candidate.strip().split(" ", 1)[0]
                if url:
                    self.references.append(("srcset", url))

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data)


def output_path(public_dir: Path, url_path: str) -> Path:
    decoded = unquote(url_path).lstrip("/")
    candidate = public_dir / decoded
    if url_path.endswith("/") or candidate.is_dir():
        return candidate / "index.html"
    return candidate


def main() -> int:
    public_dir = Path(sys.argv[1] if len(sys.argv) > 1 else "public").resolve()
    html_files = sorted(public_dir.rglob("*.html"))
    if not html_files:
        print(f"No HTML files found in {public_dir}", file=sys.stderr)
        return 1

    pages: dict[Path, PageParser] = {}
    errors: list[str] = []

    for html_file in html_files:
        parser = PageParser()
        parser.feed(html_file.read_text(encoding="utf-8"))
        pages[html_file] = parser
        relative = html_file.relative_to(public_dir)

        if not "".join(parser.title_parts).strip():
            errors.append(f"{relative}: missing title")
        if not parser.lang or not parser.lang.lower().startswith("zh"):
            errors.append(f"{relative}: invalid html lang {parser.lang!r}")
        if not parser.canonical or not parser.canonical.startswith(SITE_ORIGIN):
            errors.append(f"{relative}: invalid canonical {parser.canonical!r}")
        if not parser.is_redirect and (
            not parser.description or not parser.description.strip()
        ):
            errors.append(f"{relative}: missing description")
        duplicates = sorted({item for item in parser.ids if parser.ids.count(item) > 1})
        if duplicates:
            errors.append(f"{relative}: duplicate ids {', '.join(duplicates)}")

    for html_file, parser in pages.items():
        page_url = SITE_ORIGIN + "/" + str(html_file.relative_to(public_dir).parent) + "/"
        if html_file.name != "index.html":
            page_url = SITE_ORIGIN + "/" + str(html_file.relative_to(public_dir))

        for attribute, reference in parser.references:
            if reference.startswith(("#", "mailto:", "tel:", "data:", "javascript:")):
                if reference.startswith("#") and unquote(reference[1:]) not in parser.ids:
                    errors.append(
                        f"{html_file.relative_to(public_dir)}: missing anchor {reference}"
                    )
                continue

            parsed = urlparse(urljoin(page_url, reference))
            if parsed.scheme not in ("http", "https") or parsed.netloc != "www.jehol-ppx.com":
                continue

            target = output_path(public_dir, parsed.path)
            if not target.exists():
                errors.append(
                    f"{html_file.relative_to(public_dir)}: broken {attribute} {reference}"
                )
                continue
            if parsed.fragment and target.suffix == ".html":
                target_parser = pages.get(target)
                if target_parser and unquote(parsed.fragment) not in target_parser.ids:
                    errors.append(
                        f"{html_file.relative_to(public_dir)}: missing anchor {reference}"
                    )

    if errors:
        print("Site validation failed:", file=sys.stderr)
        for error in sorted(set(errors)):
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(html_files)} HTML pages and all internal references.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
