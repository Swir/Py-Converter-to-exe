#!/usr/bin/env python3
"""Deterministic SWIR Progress SVG generator/check for Py Converter to EXE."""
from __future__ import annotations
import argparse
import re
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ASSET = ROOT / "assets" / "readme"
LEGACY = re.compile(r"(?:[█▓▒░]{4,}|\[(?:[#=\-]){6,}\])")

CARD = '''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="180" viewBox="0 0 1200 180" role="img" aria-labelledby="title desc"><title id="title">Py Converter to EXE product progress</title><desc id="desc">Product progress is N/A because there is no authoritative measurable roadmap.</desc><defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#02050A"/><stop offset="1" stop-color="#07111C"/></linearGradient><pattern id="grid" width="28" height="28" patternUnits="userSpaceOnUse"><path d="M28 0H0V28" fill="none" stroke="#62E5FF" stroke-opacity=".05"/></pattern></defs><rect x="1" y="1" width="1198" height="178" rx="22" fill="url(#bg)" stroke="#62E5FF" stroke-opacity=".25"/><rect x="1" y="1" width="1198" height="178" rx="22" fill="url(#grid)"/><text x="50" y="38" fill="#62E5FF" font-family="Segoe UI,Arial,sans-serif" font-size="15" font-weight="700" letter-spacing="3">SWIR PROGRESS</text><text x="50" y="72" fill="#F4FAFF" font-family="Segoe UI,Arial,sans-serif" font-size="26" font-weight="800">Py Converter to EXE</text><text x="50" y="98" fill="#8DA8B8" font-family="Segoe UI,Arial,sans-serif" font-size="14">Product progress · no authoritative roadmap</text><text x="1110" y="72" text-anchor="end" fill="#F4FAFF" font-family="Segoe UI,Arial,sans-serif" font-size="30" font-weight="800">N/A</text><text x="1110" y="98" text-anchor="end" fill="#62E5FF" font-family="Segoe UI,Arial,sans-serif" font-size="13" font-weight="700">N/A</text><rect x="50" y="116" width="1100" height="18" rx="9" fill="#08131F" stroke="#62E5FF" stroke-opacity=".15"/><text x="50" y="158" fill="#8DA8B8" font-family="Segoe UI,Arial,sans-serif" font-size="12">Product completion: N/A · no measurable completion denominator is documented</text></svg>\n'''
MINI = '''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="72" viewBox="0 0 900 72" role="img" aria-labelledby="title desc"><title id="title">Py Converter to EXE compact product progress</title><desc id="desc">Product progress is N/A because there is no authoritative measurable roadmap.</desc><rect x="1" y="1" width="898" height="70" rx="16" fill="#02050A" stroke="#62E5FF" stroke-opacity=".24"/><text x="24" y="28" fill="#F4FAFF" font-family="Segoe UI,Arial,sans-serif" font-size="14" font-weight="700">Py Converter to EXE · Product progress</text><text x="24" y="51" fill="#8DA8B8" font-family="Segoe UI,Arial,sans-serif" font-size="12">Product completion: N/A</text><rect x="590" y="27" width="220" height="14" rx="7" fill="#08131F" stroke="#62E5FF" stroke-opacity=".15"/><text x="866" y="40" text-anchor="end" fill="#62E5FF" font-family="Segoe UI,Arial,sans-serif" font-size="14" font-weight="800">N/A</text></svg>\n'''

def valid_xml(text: str) -> None:
    ET.fromstring(text)

def write() -> None:
    ASSET.mkdir(parents=True, exist_ok=True)
    (ASSET / "progress-card.svg").write_text(CARD, encoding="utf-8")
    (ASSET / "progress-mini.svg").write_text(MINI, encoding="utf-8")

def check() -> int:
    for name, expected in (("progress-card.svg", CARD), ("progress-mini.svg", MINI)):
        valid_xml(expected)
        path = ASSET / name
        if not path.exists() or path.read_text(encoding="utf-8") != expected:
            print(f"stale or missing: {path}")
            return 1
    template = ASSET / "progress-template.svg"
    if not template.exists():
        print("missing progress-template.svg")
        return 1
    valid_xml(template.read_text(encoding="utf-8"))
    readme = ROOT / "README.md"
    if LEGACY.search(readme.read_text(encoding="utf-8")):
        print("legacy progress meter found in README.md")
        return 1
    print("SWIR progress check: OK")
    return 0

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if not args.check:
        write()
    return check()

if __name__ == "__main__":
    raise SystemExit(main())
