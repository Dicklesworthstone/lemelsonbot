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
    if len(anchors) < 300:
        errors.append(f"quote bank must have >=300 entries, found {len(anchors)}")
    # Ensure sequential numbering starts at 1
    nums = [int(a) for a in anchors]
    if nums and nums[0] != 1:
        errors.append("quote bank must start at §1")
    # Check for gaps
    if nums:
        expected = list(range(1, max(nums) + 1))
        if nums != expected:
            errors.append("quote bank anchors must be sequential with no gaps")
    # Basic entry structure checks and stricter validation
    allowed_tags = {
        "conception",
        "witnessing",
        "confidentiality",
        "ip",
        "design",
        "prototype",
        "manufacturing",
        "joining",
        "packaging",
        "testing",
        "disclosure",
        "collaboration",
        "general",
    }

    lines = text.splitlines()
    entry_re = re.compile(r"^## §(\\d+) — (.+?), Page (\\d+)$")
    source_re = re.compile(r"^— Source: LEMELSON_NOTEBOOKS_EXTRACTED_v1.md, .+?, Page \\d+$")
    quote_re = re.compile(r'^> \".+\"$')
    tags_re = re.compile(r"^Tags: (.+)$")

    i = 0
    while i < len(lines):
        m = entry_re.match(lines[i])
        if not m:
            i += 1
            continue
        # Expect next three lines: quote, source, tags
        if i + 3 >= len(lines):
            errors.append(f"incomplete entry for §{m.group(1)}")
            break
        quote_line = lines[i + 1].strip()
        source_line = lines[i + 2].strip()
        tags_line = lines[i + 3].strip()

        if not quote_re.match(quote_line):
            errors.append(f"invalid quote line for §{m.group(1)}")
        else:
            # Quote length constraints (80–320 chars without quotes)
            q = quote_line[3:-1]
            if len(q) < 80:
                errors.append(f"quote too short for §{m.group(1)}")
            if len(q) > 320:
                errors.append(f"quote too long for §{m.group(1)}")

        if not source_re.match(source_line):
            errors.append(f"invalid source line for §{m.group(1)}")

        tm = tags_re.match(tags_line)
        if not tm:
            errors.append(f"invalid tags line for §{m.group(1)}")
        else:
            tags = [t.strip() for t in tm.group(1).split(",") if t.strip()]
            if not tags:
                errors.append(f"no tags listed for §{m.group(1)}")
            bad = [t for t in tags if t not in allowed_tags]
            if bad:
                errors.append(f"invalid tags for §{m.group(1)}: {bad}")

        i += 1

if errors:
    print("Corpus validation failed:")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)

print("Corpus validation passed")
