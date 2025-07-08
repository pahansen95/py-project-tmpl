<!--
Standard Phase Document Structure:

- Salient Summary: Brief overview of the phase's purpose and goals
- Requisite Inputs: What artifacts/knowledge this phase requires
- Implementation Details: How to execute this phase
- Stopping Criteria: When to consider this phase complete
- Output Artifacts: What this phase produces
-->

# Phase 2 — Architectural Design Document

<!-- Salient Summary -->

The Architectural Document is an informal specification that scaffolds a structural layout and fills it in with conceptual theory. It prescribes, at the highest cognitive level, what the solution *should be*, not concerning itself with concrete implementation details.

<!-- Requisite Inputs -->

This phase relies, at a minimum, on the artifacts produced by Phase 1. After the first iteration of this holistic process, the Architecture may rely on learnings of implementing the project design. Care should be taken that the declared Mental Models & Predicates from Phase 1 still align with any shift in Architectural Design.

<!-- Implementation Details -->

This phase employs structured decomposition techniques to transform mental models into architectural components. Participants begin by identifying major system boundaries and external interfaces; these form the primary architectural divisions. Through iterative refinement, each boundary reveals internal components and their responsibilities.

The decomposition process follows established patterns:

- Domain boundaries become primary components
- Cross-cutting concerns emerge as infrastructure layers
- Integration points crystallize into defined interfaces
- Data flows inform component relationships

Teams document each component's purpose, responsibilities, and constraints. Component interactions are mapped through sequence diagrams and data flow representations. Throughout this process, participants continuously validate alignment with the vision and predicates from Phase 1.

<!-- Stopping Criteria -->

This phase concludes when participants recognize the following indicators:

- All major system components have clear boundaries and responsibilities
- Component interfaces are defined without implementation details
- Architectural patterns address all identified quality attributes
- No significant design decisions remain deferred

Generally, these indicators manifest as architectural stability — further refinement yields implementation details rather than architectural insights. The design satisfies the vision while respecting all predicates, and team members can independently explain how the architecture achieves its goals.

<!-- Output Artifacts -->

At its conclusion, this phase produces a comprehensive architectural design. Small or Simple Designs can be written to a single document, while large or complex designs might require a hierarchical layout of multiple documents.