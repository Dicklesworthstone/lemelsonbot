# Protocol Session: LEMELSON-OPERATOR-DERIVATION

## Triangulated Kernel (single)

<!-- TRIANGULATED_KERNEL_START v0.1 -->
## Triangulated Kernel v0.1

### Axioms (consensus)

**1. Priority Requires Evidence**
Statement: A conception only counts when dated, recorded, and witnessed.
Evidence: §2, §20, §21, §11, §12
Confidence: HIGH (3/3 agree)

**2. Buildability Is Part of the Idea**
Statement: An invention description must include materials and fabrication methods.
Evidence: §20, §22, §14
Confidence: HIGH (3/3 agree)

**3. Disclosure Is Controlled and Logged**
Statement: External sharing must be tracked and conditioned.
Evidence: §1, §13, §16
Confidence: HIGH (3/3 agree)

**4. Claim Scope Expands Through Variants**
Statement: A core mechanism should be expressed in multiple embodiments.
Evidence: §7, §14
Confidence: HIGH (3/3 agree)

### Operators (consensus)

**🧾 Record-of-Conception**
- Definition: Create a dated, formal statement of the idea and intent to patent.
- Triggers: first articulation; major revision; pre-disclosure.
- Failure modes: undated entry; vague scope; missing intent.
- Anchors: §2, §20, §21
- Confidence: HIGH (3/3)

**🧾 Witness-Sign**
- Definition: Obtain independent signatures that disclosure was read/understood.
- Triggers: after conception entry; after multi-page disclosure.
- Failure modes: no date; non-independent witness.
- Anchors: §11, §12, §19, §24
- Confidence: HIGH (3/3)

**🔒 Disclosure-Log**
- Definition: Track who saw what, under what confidentiality conditions.
- Triggers: manufacturer meetings; licensing talks; model demos.
- Failure modes: unlogged disclosure; no agreement.
- Anchors: §1, §13, §16
- Confidence: HIGH (3/3)

**✏ Figure-and-Embodiment**
- Definition: Tie textual descriptions to explicit figures/embodiments.
- Triggers: mechanism descriptions; multi-variant claims; attorney handoff.
- Failure modes: text-only ambiguity; figure-only vagueness.
- Anchors: §14, §4
- Confidence: HIGH (3/3)

**♻ Variant-Enumeration**
- Definition: Enumerate alternate embodiments/materials/applications.
- Triggers: adaptable mechanism; multi-market potential.
- Failure modes: single-embodiment tunnel vision; variant sprawl.
- Anchors: §7, §14
- Confidence: HIGH (3/3)

**⚙ Manufacturing-Feasibility**
- Definition: Specify materials and fabrication methods within the concept.
- Triggers: molding/sealing/packaging decisions.
- Failure modes: unbuildable claims; ignored process constraints.
- Anchors: §20, §22, §14
- Confidence: HIGH (3/3)

**🧪 Experiment-Log**
- Definition: Record material/process experiments and outcomes.
- Triggers: uncertain materials; performance tests.
- Failure modes: lost results; no learning loop.
- Anchors: §5, §8
- Confidence: HIGH (3/3)

**🧩 Prototype-Build**
- Definition: Build/show models to validate feasibility and persuade partners.
- Triggers: feasibility unknown; partner outreach.
- Failure modes: no documentation; no manufacturing plan.
- Anchors: §6, §17
- Confidence: HIGH (3/3)

**§ Patent-Link**
- Definition: Cross-reference applications, exhibits, and prior filings.
- Triggers: building on prior work; claim preparation.
- Failure modes: isolated notes; weak lineage.
- Anchors: §4, §12
- Confidence: HIGH (3/3)

### Anti-Patterns (consensus)

**Undated or unwitnessed notes**: weak priority evidence (contra §2, §11).

**Disclosure without logging/terms**: IP leakage (contra §13, §16).

**No manufacturing method**: unbuildable claims (contra §20, §22).

**Single embodiment fixation**: narrow claim scope (contra §7, §14).

**Experiments without records**: lost knowledge (contra §5, §8).

### Output Contract
- All invention records must include date, scope, and intent.
- Each disclosure must have witness confirmation or explicit log entry.
- Each concept must include materials/process feasibility notes.
- Every major idea should list at least two variants.

<!-- TRIANGULATED_KERNEL_END v0.1 -->

## Your Role: Hypothesis Generator
You generate candidate methodology hypotheses by separating levels and importing patterns.

**Primary Operators**: 🧾 Record-of-Conception, 🔒 Disclosure-Log, ♻ Variant-Enumeration

**You MUST**:
1. Separate documentation, fabrication, and disclosure layers.
2. Cite anchors for every claim.
3. Output structured hypotheses, not narrative.

**Citation Conventions**:
- Quote bank: (§n)
- Inference: [inference]

**Output Format**: Use ```delta blocks with operation, section, payload.

## Research Question
What is Lemelson’s repeatable invention methodology as evidenced in the notebooks?

## Context
We have a cleaned notebook corpus with a quote bank. The goal is to operationalize
repeated invention practices into reusable operators and constraints.

## Excerpt
“Record of Conception” entries tied to patent intent (§2, §20, §21) and witness
confirmations (§11, §12) demonstrate the evidentiary pattern.

## Requested Outputs
- 3–5 concise hypotheses about the invention workflow
- Any missing operators you detect
- Warnings about overreach

## Response Format
Reply with subject `DELTA[hypothesis_generator]: <description>`.
Include reasoning as prose, then `## Deltas` with structured contributions.
