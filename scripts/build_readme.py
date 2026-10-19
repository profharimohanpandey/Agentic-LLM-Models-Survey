#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Normalise README.md and recompute its counts.

Reads README.md in the Awesome-list style, rebuilds every entry's link and
venue badge from its canonical parts (so editing a URL re-derives the badge),
regenerates the Contents table with correct GitHub anchors, and refreshes
every count: the header badge, the teaser caption and the Statistics table.

The file is rewritten in place and the transformation is idempotent -- running
it on its own output is a no-op.  METHODOLOGY.md is maintained by hand and is
deliberately left alone.

Usage:  python scripts/build_readme.py
"""

import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README = os.path.join(ROOT, "README.md")

EMOJI = {1: "\U0001f4d6", 2: "\U0001f39b", 3: "\U0001f3c6", 4: "\U0001f9e0",
         5: "\U0001f916", 6: "\U0001f6e0", 7: "\U0001f3d7", 8: "\U0001f91d",
         9: "\U0001f6e1", 10: "\U0001f4ca", 11: "\U0001f680", 12: "\u2699"}

BADGE_PREFIX = "https://img.shields.io/badge/"

CAT_HDR = re.compile(r"^## (\d+)\.\s+(.*)$")
BULLET = re.compile(
    r"^- (?P<title>.+?)"
    r"(?: \[\[(?P<tag>[^\]]+)\]\]\((?P<url>[^)]+)\))?"
    r" !\[\]\((?P<badge>" + re.escape(BADGE_PREFIX) + r".+)\)\s*$")
CONTENTS_ROW = re.compile(
    r"^\|\s*(?P<emoji>\S+)\s+\[(?P<idx>\d+)\.\s+(?P<title>.*?)\]\(#(?P<anchor>[^)]+)\)"
    r"\s*\|\s*(?P<subs>[^|]*?)\s*\|$")

def esc_badge(s):
    return s.replace("-", "--").replace(" ", "_").replace("/", "%2F")

def unesc_badge(s):
    return s.replace("%2F", "/").replace("_", " ").replace("--", "-")

def gh_anchor(s):
    s = s.lower()
    s = re.sub(r"[^\w\s\-]", "", s, flags=re.UNICODE)
    return re.sub(r"\s", "-", s)

def badge(venue, year, url):
    if venue == "arXiv" or "arxiv.org" in (url or "").lower():
        label, colour = "arXiv", "red"
    else:
        label, colour = (venue or "link"), "blue"
    return "![](%s%s-%s-%s)" % (BADGE_PREFIX, esc_badge(label),
                                esc_badge(year or "link"), colour)

def link_tag(url):
    return "Code" if "github.com" in (url or "") else "Paper"

def render(title, venue, year, url):
    entry = "- %s" % title
    if url:
        entry += " [[%s]](%s)" % (link_tag(url), url)
    return entry + " " + badge(venue, year, url)

def parse_badge(badge_url):
    rest = badge_url[len(BADGE_PREFIX):]
    label_msg, colour = rest.rsplit("-", 1)
    if colour not in ("red", "blue", "green", "informational", "brightgreen"):
        label_msg = rest
    label, _, year = label_msg.rpartition("-")
    return unesc_badge(label), (year if year != "link" else "")

text = io.open(README, encoding="utf-8").read()
lines = text.splitlines()

def find(pat, start=0):
    for i in range(start, len(lines)):
        if re.match(pat, lines[i]):
            return i
    return -1

i_contents = find(r"^## .*\bContents\b")
i_conv = find(r"^> \*\*Link conventions\.\*\*")
i_stats = find(r"^## .*\bStatistics\b")
if -1 in (i_contents, i_conv, i_stats):
    sys.exit("README.md: headings missing")

cat_hdrs = [(i, int(m.group(1)), m.group(2))
            for i, l in enumerate(lines) for m in [CAT_HDR.match(l)] if m]
if not cat_hdrs:
    sys.exit("README.md: no category headings")

i_first_row = next((i for i in range(i_contents, i_conv)
                    if CONTENTS_ROW.match(lines[i])), i_contents)

intro = lines[:i_first_row]

contents = {}
extra_rows = []
for l in lines[i_first_row:i_conv]:
    m = CONTENTS_ROW.match(l)
    if m:
        contents[int(m.group("idx"))] = (m.group("emoji"), m.group("subs").strip())
    elif l.startswith("|") and not re.match(r"^\|\s*-+\s*\|", l) and not re.match(r"^\|\s*Section\s*\|", l):
        extra_rows.append(l)

cats = []
for idx, (start, num, title) in enumerate(cat_hdrs):
    end = cat_hdrs[idx + 1][0] if idx + 1 < len(cat_hdrs) else i_stats
    note, entries = [], []
    in_bullets = False
    for l in lines[start + 1:end]:
        if l.startswith("- "):
            in_bullets = True
            m = BULLET.match(l)
            if not m:
                sys.exit("README.md: unparsable: %s" % l)
            url = m.group("url") or ""
            venue, year = parse_badge(m.group("badge"))
            entries.append((m.group("title").rstrip(), venue, year, url))
        elif l.strip() and l.strip() != "---":
            if in_bullets:
                sys.exit("README.md: stray: %s" % l)
            note.append(l.strip())
    cats.append((num, title, " ".join(note), entries))

i_stats_end = i_stats + 1
while i_stats_end < len(lines) and not lines[i_stats_end].startswith("|"):
    i_stats_end += 1
while i_stats_end < len(lines) and lines[i_stats_end].startswith("|"):
    i_stats_end += 1
bottom = lines[i_stats_end:]

out = list(intro)
for num, title, _, entries in cats:
    emoji, subs = contents.get(num, (EMOJI.get(num, ""), ""))
    out.append("| %s [%d. %s](#%s) | %s |"
               % (emoji, num, title, gh_anchor("%d. %s" % (num, title)), subs))
for l in extra_rows:
    out.append(l)
out.append("")
out.append(lines[i_conv])
out.append("")
for num, title, note, entries in cats:
    out.append("---")
    out.append("")
    out.append("## %d. %s" % (num, title))
    out.append("")
    if note:
        out.append(note)
        out.append("")
    out.extend(render(*e) for e in entries)
    out.append("")
out.append("---")
out.append("")
out.append("## \U0001f4ca Statistics")
out.append("")
out.append("| Metric | Count |")
out.append("|--------|-------|")
out.append("| Categories | %d |" % len(cats))
tot = sum(len(e) for _, _, _, e in cats)
out.append("| References indexed | %d |" % tot)
out.append("| With arXiv links | %d |" % sum(1 for _, _, _, es in cats for *_, u in es if "arxiv.org" in u))
out.append("| With DOI links | %d |" % sum(1 for _, _, _, es in cats for *_, u in es if "doi.org" in u))
out.append("| Code / report links | %d |" % sum(1 for _, _, _, es in cats for *_, u in es if "github.com" in u))
out.extend(bottom)

text = "\n".join(out) + "\n"
text = re.sub(r"(\[!\[References: )\d+(\])", r"\g<1>%d\g<2>" % tot, text)
text = re.sub(r"(badge/References-)\d+(?=-informational)", r"\g<1>%d" % tot, text)
text = re.sub(r"(\*Distribution of the )\d+( references)",
              lambda m: "%s%d%s" % (m.group(1), tot, m.group(2)), text)

io.open(README, "w", encoding="utf-8", newline="\n").write(text)
print("ok refs=%d" % tot)
