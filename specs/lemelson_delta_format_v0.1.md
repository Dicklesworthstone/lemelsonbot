# Lemelson Protocol: Delta Output Format v0.1

> **Status**: Draft specification
> **Purpose**: Define how agents express structured updates to Lemelson artifacts

---

## Message Structure

```
# Delta Contribution

[Optional prose for humans]

## Deltas

```lemelson-delta
{ ... }
```
```

---

## Delta Block Schema

```json
{
  "operation": "ADD" | "EDIT" | "KILL",
  "section": "invention_thread" | "conception_record" | "variant_slate" |
             "manufacturing_notes" | "tests_samples" |
             "disclosure_partner_log" | "adversarial_critique",
  "target_id": "IT1" | "CR1" | "V2" | "M3" | "T1" | "D4" | "C2" | null,
  "payload": { ... },
  "rationale": "brief reason"
}
```

### Valid Sections and Prefixes

| Section | Prefix |
|---------|--------|
| invention_thread | IT |
| conception_record | CR |
| variant_slate | V |
| manufacturing_notes | M |
| tests_samples | T |
| disclosure_partner_log | D |
| adversarial_critique | C |

---

## Example: Add Variant

```lemelson-delta
{
  "operation": "ADD",
  "section": "variant_slate",
  "target_id": null,
  "payload": {
    "name": "Bellows toy with suction base",
    "description": "Add a suction cup base for crib attachment",
    "anchors": ["§2", "inference"]
  },
  "rationale": "Expands claim scope with a mounting variant"
}
```
