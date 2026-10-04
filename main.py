"""Refresh the "Latest from LHCb" list on the home page.

Reads the LHCb outreach RSS feed and rewrites the block between the
LHCB-NEWS markers in index.html. On any failure the file is left untouched,
so the site never shows an empty or broken list. Standard library only.
"""

import html
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from pathlib import Path

FEED_URL = "https://lhcb-outreach.web.cern.ch/feed/"
INDEX = Path(__file__).with_name("index.html")
N_ITEMS = 5
MARKERS = re.compile(r"(<!-- LHCB-NEWS:START -->)(.*?)(<!-- LHCB-NEWS:END -->)", re.S)


def fetch_items():
    req = urllib.request.Request(FEED_URL, headers={"User-Agent": "ahmedabdelmotteleb.github.io news updater"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        root = ET.fromstring(resp.read())
    items = []
    for item in root.iter("item"):
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        date = parsedate_to_datetime(item.findtext("pubDate"))
        if title and link.startswith("https://"):
            items.append((date, title, link))
    items.sort(key=lambda x: x[0], reverse=True)
    return items[:N_ITEMS]


def render(items):
    lines = ['<ul class="news">']
    for date, title, link in items:
        lines.append(
            f'            <li><a href="{html.escape(link)}">'
            f'<time datetime="{date:%Y-%m-%d}">{date:%d %b %Y}</time>'
            f"<span>{html.escape(title)}</span></a></li>"
        )
    lines.append("          </ul>")
    return "\n          " + "\n".join(lines) + "\n          "


def main():
    try:
        items = fetch_items()
    except Exception as exc:  # network or parse problem: keep the current list
        print(f"Could not read feed, leaving index.html unchanged: {exc}")
        return 0
    if not items:
        print("Feed returned no items, leaving index.html unchanged.")
        return 0

    page = INDEX.read_text(encoding="utf-8")
    if not MARKERS.search(page):
        print("News markers not found in index.html.")
        return 1
    updated = MARKERS.sub(lambda m: m.group(1) + render(items) + m.group(3), page, count=1)
    if updated != page:
        INDEX.write_text(updated, encoding="utf-8", newline="\n")
        print(f"Updated index.html with {len(items)} headlines.")
    else:
        print("Headlines unchanged.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
