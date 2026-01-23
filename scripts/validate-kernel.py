#!/usr/bin/env python3
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
kernel_path = ROOT / "corpus" / "specs" / "triangulated_kernel.md"
quote_bank = ROOT / "corpus" / "quote_bank" / "quote_bank.md"

if not kernel_path.exists():
    print("Missing corpus/specs/triangulated_kernel.md")
    sys.exit(1)

text = kernel_path.read_text(encoding="utf-8")

start = "<!-- TRIANGULATED_KERNEL_START"
end = "<!-- TRIANGULATED_KERNEL_END"

if start not in text or end not in text:
    print("Kernel missing TRIANGULATED_KERNEL markers")
    sys.exit(1)

# Count axioms and operators in kernel body
kernel_body = text.split(start, 1)[1].split(end, 1)[0]
axioms = re.findall(r"^\*\*\d+\. ", kernel_body, flags=re.M)
operators = re.findall(r"^\*\*.+\*\*\n- Definition:", kernel_body, flags=re.M)

errors = []
if len(axioms) < 3:
    errors.append(f"expected >=3 axioms, found {len(axioms)}")
if len(operators) < 8:
    errors.append(f"expected >=8 operators, found {len(operators)}")

# Validate anchors against quote bank
if quote_bank.exists():
    qb_text = quote_bank.read_text(encoding="utf-8")
    anchors = set(int(a) for a in re.findall(r"^## §(\d+) — ", qb_text, flags=re.M))
    used = set(int(a) for a in re.findall(r"§(\d+)", kernel_body))
    missing = sorted(a for a in used if a not in anchors)
    if missing:
        errors.append(f"kernel references missing anchors: {missing}")

if errors:
    print("Kernel validation failed:")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)

print("Kernel validation passed")
