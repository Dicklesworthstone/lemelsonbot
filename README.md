# Lemelsonbot

Operationalized methodology from Jerome H. Lemelson's invention notebooks.

## Structure

- `LEMELSON_NOTEBOOKS_EXTRACTED_v1.md` — cleaned notebook corpus
- `corpus/` — primary sources, quote bank, distillations, kernel
- `specs/` — Lemelson protocol specs (artifact schema, delta format, linting)
- `artifacts/` — protocol artifacts and golden examples
- `scripts/` — validation utilities

## Validation

Run all validators:

```
python3 scripts/validate-corpus.py
python3 scripts/validate-kernel.py
python3 scripts/validate-operators.py
python3 scripts/validate-kickoffs.py
```
