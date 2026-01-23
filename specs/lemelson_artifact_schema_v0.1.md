# Lemelson Protocol Artifact Schema v0.1

> **Status**: Draft specification
> **Purpose**: Canonical artifact format for invention sessions
> **Scope**: Artifacts must be auditable, mergeable, and evidence-linked

---

## Overview

A Lemelson Protocol artifact is a markdown document capturing a single invention
thread with evidence anchors, partner activity, and feasibility testing. It is
structured for deterministic merge via delta blocks and anchored citations to the
quote bank (`§n`).

---

## Required Sections (7 total)

| # | Section | ID Prefix | Purpose |
|---|---------|-----------|---------|
| 1 | Invention Thread | `IT` | Stable invention statement (bite point) |
| 2 | Conception Record | `CR` | Dated conception + intent to file |
| 3 | Variant Slate | `V` | Alternate embodiments/materials/applications |
| 4 | Manufacturing Notes | `M` | Materials/process/joining feasibility |
| 5 | Tests & Samples | `T` | Experiments, sample acquisition, results |
| 6 | Disclosure & Partner Log | `D` | Who saw what, agreements, follow-ups |
| 7 | Adversarial Critique | `C` | What breaks the claim or record |

---

## Item ID Conventions

```
IT1
CR1
V1, V2, V3...
M1, M2...
T1, T2...
D1, D2...
C1, C2...
```

**Rules**:
1. IDs are monotonic and never reused.
2. IDs are stable across edits.
3. Each item includes **Anchors** with `§n` or `inference`.

---

## Section Specifications

### 1. Invention Thread (IT)

```
## 1. Invention Thread

**IT1**: [One-sentence invention statement]
**Context**: [2–3 sentences background]
**Why it matters**: [1–2 sentences on downstream value]
**Anchors**: §n, §m
```

### 2. Conception Record (CR)

```
## 2. Conception Record

### CR1: [Date]
**Statement**: [Conception summary + intent to file]
**Witness**: [Name + date]
**Anchors**: §n
```

### 3. Variant Slate (V)

```
## 3. Variant Slate

### V1: [Variant name]
**Description**: [1–2 sentences]
**Anchors**: §n
```

### 4. Manufacturing Notes (M)

```
## 4. Manufacturing Notes

### M1: [Process]
**Materials**: [List]
**Method**: [Process details]
**Joining**: [Seal/weld/etc]
**Anchors**: §n
```

### 5. Tests & Samples (T)

```
## 5. Tests & Samples

### T1: [Test or Sample]
**Purpose**: [Why]
**Procedure**: [How]
**Outcome**: [Result]
**Anchors**: §n
```

### 6. Disclosure & Partner Log (D)

```
## 6. Disclosure & Partner Log

### D1: [Partner]
**Disclosure**: [What was shown]
**Terms**: [Confidentiality/agreements]
**Follow-up**: [Next step + date]
**Anchors**: §n
```

### 7. Adversarial Critique (C)

```
## 7. Adversarial Critique

### C1: [Failure mode]
**Why it breaks**: [Impact on claim]
**Fix**: [Mitigation]
**Anchors**: §n or inference
```

---

## Citation Rules

- Use `§n` anchors for quote bank evidence.
- Use `inference` when not directly supported.
- Mixed: `§12 [inference]` when extrapolating.
