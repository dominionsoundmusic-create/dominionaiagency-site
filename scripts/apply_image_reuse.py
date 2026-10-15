#!/usr/bin/env python3
"""Photo reuse report and checks (docs/photos.json + docs/image-reuse.json, Maurice's reuse rule).

- Every photo in docs/photos.json must exist in src/static/images/.
- Every planned image in docs/image-reuse.json must name an existing stand-in photo (`from`).
- Lists which planned images have arrived (their file is now in src/static/images/) and which are still
  shown through their stand-in, and how many pages use each photo, so Maurice can see how far each photo
  is stretched. build.py does the actual stand-in crops at build time; this script only reports.

Usage: python3 scripts/apply_image_reuse.py   (exit code 1 on a missing photo or stand-in)
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / "src" / "static" / "images"


def main():
    photos = json.loads((ROOT / "docs" / "photos.json").read_text())
    reuse = {k: v for k, v in json.loads((ROOT / "docs" / "image-reuse.json").read_text()).items() if not k.startswith("_")}
    bad = 0
    for f in photos:
        if not (IMG / f).exists():
            print("MISSING photo", f)
            bad += 1
    arrived, waiting = [], []
    for slot, e in reuse.items():
        if e["from"] not in photos:
            print("BAD stand-in", slot, "->", e["from"])
            bad += 1
        (arrived if (IMG / slot).exists() else waiting).append(slot)
    use = Counter()
    for p in (ROOT / "src" / "pages").rglob("*.html"):
        t = p.read_text()
        for f in set(re.findall(r"([a-z0-9-]+\.jpg)", t)):
            use[f] += 1
    data = json.loads((ROOT / "src" / "data" / "site.json").read_text())
    for s in data.get("services", []):
        if s.get("card_image"):
            use[s["card_image"]] += 0  # card thumbnails appear wherever service cards are shown
    print(f"{len(photos)} photo files ({len({v['group'] for v in photos.values()})} distinct photos); "
          f"{len(reuse)} planned new images: {len(arrived)} arrived, {len(waiting)} shown through a stand-in")
    for f, n in use.most_common():
        tag = "planned, stand-in " + reuse[f]["from"] if f in reuse and f in waiting else ("photo" if f in photos else "UNKNOWN")
        print(f"  {n:3d} page(s)  {f}  ({tag})")
        if tag == "UNKNOWN":
            bad += 1
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
