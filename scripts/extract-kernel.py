#!/usr/bin/env python3
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_KERNEL = ROOT / "corpus" / "specs" / "triangulated_kernel.md"

parser = argparse.ArgumentParser(description="Extract triangulated kernel block")
parser.add_argument("--in", dest="input_path", default=str(DEFAULT_KERNEL))
parser.add_argument("--out", dest="output_path", default="")
args = parser.parse_args()

text = Path(args.input_path).read_text(encoding="utf-8")
start = text.find("<!-- TRIANGULATED_KERNEL_START")
end = text.find("<!-- TRIANGULATED_KERNEL_END")

if start == -1 or end == -1:
    raise SystemExit("Kernel markers not found")

# include end marker line
end = text.find("\n", end)
if end == -1:
    end = len(text)

block = text[start:end].rstrip() + "\n"

if args.output_path:
    Path(args.output_path).write_text(block, encoding="utf-8")
else:
    print(block)
