# Operator Library — Lemelson Invention Method

### 🧾 Record-of-Conception

**Definition**: Create a dated, formal statement of the idea and intent to patent.

**When-to-Use Triggers**:
- When a concept is first articulated.
- When a material change to the mechanism is made.
- Before any external disclosure.

**Failure Modes**:
- No date or missing intent → weak priority evidence.
- Vague scope → unclear claim boundaries.

**Prompt Module** (copy/paste for agents):
~~~text
[OPERATOR: 🧾 Record-of-Conception]
1) Write a dated conception entry in 4–8 sentences.
2) State the mechanism, purpose, and intended application.
3) Add a one-line intent-to-file note.

Output (required): A markdown block labeled "Record of Conception".
Optional: Variants list, manufacturing notes.
Anchors: cite §2, §20, or §21.
~~~

**Canonical tag**: record-of-conception

**Quote-bank anchors**: §2, §20, §21

**Sources**: gpt_distillation.md, opus_distillation.md, gemini_distillation.md

---

### 🧾 Witness-Sign

**Definition**: Obtain independent signatures that the disclosure was read and understood.

**When-to-Use Triggers**:
- After recording a conception entry.
- After a multi-page disclosure.
- When documenting major revisions.

**Failure Modes**:
- Missing date → ambiguous timeline.
- Non-independent witness → credibility risk.

**Prompt Module** (copy/paste for agents):
~~~text
[OPERATOR: 🧾 Witness-Sign]
1) Add a witness line with name and date.
2) Include “read and understood” language.
3) If multiple pages, note page range.

Output (required): Witness block with name/date.
Anchors: cite §11, §12, §19, or §24.
~~~

**Canonical tag**: witness-sign

**Quote-bank anchors**: §11, §12, §19, §24

**Sources**: gpt_distillation.md, opus_distillation.md, gemini_distillation.md

---

### 🔒 Disclosure-Log

**Definition**: Track who saw what, under what confidentiality conditions.

**When-to-Use Triggers**:
- When showing models to manufacturers.
- During licensing discussions.
- When confidentiality is emphasized.

**Failure Modes**:
- Unlogged disclosure → IP leakage.
- No agreement → loss of leverage.

**Prompt Module** (copy/paste for agents):
~~~text
[OPERATOR: 🔒 Disclosure-Log]
1) Record the person/company and date.
2) State what was shown or disclosed.
3) Note confidentiality terms or agreements.

Output (required): Disclosure log entry (3–6 lines).
Anchors: cite §1, §13, or §16.
~~~

**Canonical tag**: disclosure-log

**Quote-bank anchors**: §1, §13, §16

**Sources**: gpt_distillation.md, opus_distillation.md, gemini_distillation.md

---

### ✏ Figure-and-Embodiment

**Definition**: Tie textual descriptions to explicit figures and labeled embodiments.

**When-to-Use Triggers**:
- When describing mechanical structure.
- When listing multiple embodiments.
- When preparing attorney handoff.

**Failure Modes**:
- Text without figure references → ambiguity.
- Figures without operational description → weak claims.

**Prompt Module** (copy/paste for agents):
~~~text
[OPERATOR: ✏ Figure-and-Embodiment]
1) Assign figure numbers to each embodiment.
2) Write 2–4 sentences per figure describing function.
3) Cross-reference figures in the main description.

Output (required): Figure list with descriptions.
Anchors: cite §14 or §4.
~~~

**Canonical tag**: figure-and-embodiment

**Quote-bank anchors**: §14, §4

**Sources**: gpt_distillation.md, opus_distillation.md, gemini_distillation.md

---

### ♻ Variant-Enumeration

**Definition**: Enumerate alternate embodiments, materials, or applications.

**When-to-Use Triggers**:
- When the mechanism is adaptable.
- When widening claim scope.
- When targeting multiple markets.

**Failure Modes**:
- Single-embodiment tunnel vision → narrow claims.
- Variant sprawl without rationale → incoherence.

**Prompt Module** (copy/paste for agents):
~~~text
[OPERATOR: ♻ Variant-Enumeration]
1) State the core mechanism in one sentence.
2) List 3–6 variants (materials, shapes, contexts).
3) Tag each variant with intended use.

Output (required): Variant list with tags.
Anchors: cite §7 or §14.
~~~

**Canonical tag**: variant-enumeration

**Quote-bank anchors**: §7, §14

**Sources**: gpt_distillation.md, opus_distillation.md, gemini_distillation.md

---

### ⚙ Manufacturing-Feasibility

**Definition**: Specify materials and fabrication methods inside the concept.

**When-to-Use Triggers**:
- When a device must be molded or sealed.
- When packaging is part of the mechanism.
- When production method constrains form.

**Failure Modes**:
- Unspecified process → unbuildable claims.
- Ignoring process constraints → unrealistic designs.

**Prompt Module** (copy/paste for agents):
~~~text
[OPERATOR: ⚙ Manufacturing-Feasibility]
1) List primary materials and thicknesses (if known).
2) Specify forming method (molding, slush, rotational, etc.).
3) Identify joining/sealing steps.

Output (required): Manufacturing notes block.
Anchors: cite §20, §22, or §14.
~~~

**Canonical tag**: manufacturing-feasibility

**Quote-bank anchors**: §20, §22, §14

**Sources**: gpt_distillation.md, opus_distillation.md, gemini_distillation.md

---

### 🧪 Experiment-Log

**Definition**: Record material/process experiments and outcomes.

**When-to-Use Triggers**:
- When material behavior is uncertain.
- When performance tests are needed.
- When a failure informs design changes.

**Failure Modes**:
- Experiments without logs → lost knowledge.
- No link to design change → no learning loop.

**Prompt Module** (copy/paste for agents):
~~~text
[OPERATOR: 🧪 Experiment-Log]
1) State the hypothesis or purpose of the experiment.
2) Record the procedure and materials.
3) Record outcomes and implications.

Output (required): Experiment log entry.
Anchors: cite §5 or §8.
~~~

**Canonical tag**: experiment-log

**Quote-bank anchors**: §5, §8

**Sources**: gpt_distillation.md, opus_distillation.md, gemini_distillation.md

---

### 🧩 Prototype-Build

**Definition**: Build/show models to validate feasibility and persuade partners.

**When-to-Use Triggers**:
- When feasibility is uncertain.
- When preparing for manufacturer meetings.
- When soliciting feedback or quotes.

**Failure Modes**:
- Prototype without documentation → lost insights.
- Prototype without manufacturing plan → dead end.

**Prompt Module** (copy/paste for agents):
~~~text
[OPERATOR: 🧩 Prototype-Build]
1) Describe the model built or shown.
2) Record who saw it and their feedback.
3) Note next actions (samples/quotes).

Output (required): Prototype log entry.
Anchors: cite §6 or §17.
~~~

**Canonical tag**: prototype-build

**Quote-bank anchors**: §6, §17

**Sources**: gpt_distillation.md, opus_distillation.md, gemini_distillation.md

---

### § Patent-Link

**Definition**: Cross-reference applications, exhibits, and prior filings.

**When-to-Use Triggers**:
- When building on earlier filings.
- When preparing claim language.
- When listing exhibits for attorneys.

**Failure Modes**:
- No cross-reference → isolated records.
- Weak lineage → narrower protection.

**Prompt Module** (copy/paste for agents):
~~~text
[OPERATOR: § Patent-Link]
1) Cite prior application numbers or exhibits.
2) State how the current concept extends them.
3) Note intended filing or continuation.

Output (required): Patent linkage note.
Anchors: cite §4 or §12.
~~~

**Canonical tag**: patent-link

**Quote-bank anchors**: §4, §12

**Sources**: gpt_distillation.md, opus_distillation.md, gemini_distillation.md
