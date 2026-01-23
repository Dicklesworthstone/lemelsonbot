#!/usr/bin/env python3
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "corpus"

errors = []

# Primary sources
primary_dir = CORPUS / "primary" / "transcripts"
if not primary_dir.exists():
    errors.append("missing corpus/primary/transcripts")
else:
    primary_files = list(primary_dir.glob("*.md"))
    if len(primary_files) < 3:
        errors.append(f"need >=3 primary transcripts, found {len(primary_files)}")

# Quote bank
quote_bank = CORPUS / "quote_bank" / "quote_bank.md"
if not quote_bank.exists():
    errors.append("missing corpus/quote_bank/quote_bank.md")
else:
    text = quote_bank.read_text(encoding="utf-8")
    anchors = re.findall(r"^## §(\d+) — ", text, flags=re.M)
    if len(anchors) < 100:
        errors.append(f"quote bank must have >=100 entries, found {len(anchors)}")
    # Ensure sequential numbering starts at 1
    nums = [int(a) for a in anchors]
    if nums and nums[0] != 1:
        errors.append("quote bank must start at §1")
    # Check for gaps
    if nums:
        expected = list(range(1, max(nums) + 1))
        if nums != expected:
            errors.append("quote bank anchors must be sequential with no gaps")
    # Basic entry structure checks
    for idx in range(1, min(10, len(nums)) + 1):
        if f"## §{idx} —" not in text:
            errors.append(f"missing entry header for §{idx}")
            break
        if f"— Source:" not in text:
            errors.append("missing Source lines in quote bank")
            break
        if "Tags:" not in text:
            errors.append("missing Tags lines in quote bank")
            break

if errors:
    print("Corpus validation failed:")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)

print("Corpus validation passed")
