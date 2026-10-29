"""Validate the assignment's HTML/CSS portfolio using standard Python."""
from html.parser import HTMLParser
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
ROLL_NUMBER = "FA23-BAI-006"
STUDENT_NAME = "Adil Javed"


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tags = []
        self.text = []
        self.title = []
        self.h1 = []
        self.capture = None

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))
        if tag in ("title", "h1"):
            self.capture = tag

    def handle_endtag(self, tag):
        if tag == self.capture:
            self.capture = None

    def handle_data(self, data):
        self.text.append(data)
        if self.capture == "title":
            self.title.append(data)
        elif self.capture == "h1":
            self.h1.append(data)


def check(condition, message):
    if not condition:
        print(f"FAIL: {message}")
        sys.exit(1)
    print(f"PASS: {message}")


def main():
    page_path = ROOT / "index.html"
    css_path = ROOT / "style.css"
    check(page_path.is_file(), "index.html exists")
    check(css_path.is_file(), "style.css exists")
    page = PageParser()
    page.feed(page_path.read_text(encoding="utf-8-sig"))
    check(bool("".join(page.title).strip()), "Page has a non-empty title")
    check(ROLL_NUMBER in " ".join(page.text), "Page contains the correct roll number")
    heading = " ".join("".join(page.h1).split())
    check(STUDENT_NAME in heading, "Main heading displays the student's name")
    check(any(tag == "link" and attrs.get("href") == "style.css"
              and "stylesheet" in (attrs.get("rel") or "").split()
              for tag, attrs in page.tags), "Page links to style.css")
    check(bool(css_path.read_text(encoding="utf-8-sig").strip()), "Stylesheet is not empty")
    check(any(tag == "meta" and attrs.get("name") == "viewport"
              for tag, attrs in page.tags), "Page includes a mobile viewport")
    check(not any(tag == "script" for tag, _ in page.tags), "Page uses no JavaScript")
    check(not any(tag == "style" or "style" in attrs for tag, attrs in page.tags),
          "Styling is kept in style.css")
    print("All page checks passed.")


if __name__ == "__main__":
    main()
