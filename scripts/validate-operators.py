#!/usr/bin/env python3
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ops_path = ROOT / "corpus" / "specs" / "operator_library.md"

if not ops_path.exists():
    print("Missing corpus/specs/operator_library.md")
    sys.exit(1)

text = ops_path.read_text(encoding="utf-8")
sections = re.split(r"^### ", text, flags=re.M)
# First chunk is header
operators = []
for chunk in sections[1:]:
    title_line = chunk.splitlines()[0].strip()
    body = "\n".join(chunk.splitlines()[1:])
    operators.append((title_line, body))

errors = []
if len(operators) < 8:
    errors.append(f"expected >=8 operators, found {len(operators)}")

required_fields = [
    "**Definition**:",
    "**When-to-Use Triggers**:",
    "**Failure Modes**:",
    "**Prompt Module**",
    "**Canonical tag**:",
    "**Quote-bank anchors**:",
]

for title, body in operators:
    for field in required_fields:
        if field not in body:
            errors.append(f"operator '{title}' missing field {field}")
    if "[OPERATOR:" not in body:
        errors.append(f"operator '{title}' missing prompt module header")

if errors:
    print("Operator validation failed:")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)

print("Operator validation passed")
