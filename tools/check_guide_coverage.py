#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The usage guides must teach every rule the validator enforces.

Both guides headed their rule section "G1–G15 in the schema" and taught
thirteen: G14 (what the batch cost) and G15 (accepted warnings) were enforced
and never explained, and the warning paragraph said "five" while the schema
had seven. The heading was pinned to nothing, so it stayed right while the
list under it went stale. The same drift was found in Mizan's guides the same
day; Mizan has its own copy of this check, shaped for how that guide is written.

The guides here teach the hard rules as a numbered list, item n = Gn. So the
check is structural: in section 3 of each guide, the heading's range must end
at the schema's highest G number, and the list must have exactly that many
items.

What it does not check: the warnings. The guides describe them in a sentence
("Seven further checks ..."), which a regex can count only by parsing prose.
That half stays a review item.

Usage:
    python tools/check_guide_coverage.py    # exit 1 if a guide fell behind
"""
from __future__ import annotations

import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCHEMA = os.path.join(ROOT, "skill", "kiyas", "schemas", "kiyas-seed.yaml")
GUIDES = ["docs/en/usage-guide.md", "docs/tr/kullanim-kilavuzu.md"]

DEFINED = re.compile(r"^#\s+G(\d+)\.\s", re.M)
SECTION = re.compile(r"^## 3\. (.*?)$(.*?)(?=^## 4\. )", re.M | re.S)
RANGE = re.compile(r"G1[–-]G(\d+)")
ITEM = re.compile(r"^(\d+)\. ", re.M)


def read(path):
    with io.open(path, encoding="utf-8") as fh:
        return fh.read()


def main():
    defined = [int(n) for n in DEFINED.findall(read(SCHEMA))]
    if not defined:
        sys.stderr.write("FAIL: found no G-rule definitions in %s -- the "
                         "pattern no longer matches the schema\n" % SCHEMA)
        return 1
    top = max(defined)

    problems = []
    for rel in GUIDES:
        m = SECTION.search(read(os.path.join(ROOT, rel)))
        if not m:
            problems.append("%s: no '## 3.' section before '## 4.'" % rel)
            continue
        heading, body = m.group(1), m.group(2)
        r = RANGE.search(heading)
        if not r or int(r.group(1)) != top:
            problems.append("%s: section 3 heading says %s, the schema "
                            "defines G1-G%d" % (rel, r.group(0) if r else
                                                "no range", top))
        items = [int(n) for n in ITEM.findall(body)]
        if items != list(range(1, top + 1)):
            problems.append("%s: section 3 teaches items %s, expected 1-%d"
                            % (rel, ",".join(map(str, items)) or "none", top))

    if problems:
        sys.stderr.write("FAIL: a usage guide fell behind the schema:\n")
        for line in problems:
            sys.stderr.write("  " + line + "\n")
        return 1
    print("ok  %d guide(s) teach G1-G%d, one item per rule" % (len(GUIDES), top))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
