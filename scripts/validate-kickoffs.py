#!/usr/bin/env python3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC_DIR = ROOT / "corpus" / "specs"

errors = []

kickoff_files = list(SPEC_DIR.glob("session_kickoff*.md"))
if not kickoff_files:
    errors.append("no session_kickoff*.md files found")

for path in kickoff_files:
    text = path.read_text(encoding="utf-8")
    if "<!-- TRIANGULATED_KERNEL_START" not in text or "<!-- TRIANGULATED_KERNEL_END" not in text:
        errors.append(f"{path.name} missing kernel markers")
    if "v0.3" not in text:
        errors.append(f"{path.name} kernel version mismatch (expected v0.3)")

if errors:
    print("Kickoff validation failed:")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)

print("Kickoff validation passed")
