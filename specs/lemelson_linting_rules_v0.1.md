# Lemelson Protocol: Linting Rules v0.1

> **Purpose**: Enforce minimum completeness and evidence requirements

## Core Rules

- **LEM-001**: Missing Invention Thread section (IT1 required)
- **LEM-002**: Conception Record missing date or intent to file
- **LEM-003**: Conception Record missing witness line
- **LEM-004**: Variant Slate has fewer than 2 variants
- **LEM-005**: Manufacturing Notes section missing materials or method
- **LEM-006**: Tests & Samples section missing at least 1 entry
- **LEM-007**: Disclosure & Partner Log missing when partner engagement anchors exist
- **LEM-008**: Follow-up missing for any disclosure with pending action
- **LEM-009**: Any item missing anchors or using anchors not in quote bank
- **LEM-010**: Inference claims not labeled `[inference]`

## Severity Levels

- **Error**: LEM-001, LEM-002, LEM-003, LEM-004, LEM-005
- **Warning**: LEM-006, LEM-007, LEM-008, LEM-009, LEM-010
