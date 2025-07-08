<!--
Standard Phase Document Structure:

- Salient Summary: Brief overview of the phase's purpose and goals
- Requisite Inputs: What artifacts/knowledge this phase requires
- Implementation Details: How to execute this phase
- Stopping Criteria: When to consider this phase complete
- Output Artifacts: What this phase produces
-->

# Phase 3 — Hierarchical Design Tree

<!-- Salient Summary -->

The goal of this phase is to systematically decompose the architecture into a hierarchical tree of implementable components through an iterative, level-based process. Teams work breadth-first, processing each level of the tree completely before descending, with user confirmation gates ensuring alignment at each stage. The critical distinction between design nodes (requiring further decomposition) and computational nodes (ready for implementation) drives the entire process until all leaf nodes represent directly implementable constructs.

<!-- Requisite Inputs -->

The design tree construction requires the **Architectural Design Document** providing top-level components and their relationships. These architectural boundaries form the root nodes of the hierarchical decomposition. Teams must also understand the **Hierarchical Design Tree Generation Procedure** which provides the authoritative process for level-based decomposition. Active user participation is essential — the procedure includes confirmation gates at each level where stakeholders validate decomposition decisions before proceeding. Through subsequent iterations, implementation insights may reveal missing components or suggest alternative decompositions, triggering targeted refinements to specific tree branches.

<!-- Implementation Details -->

The hierarchical decomposition follows a structured, iterative procedure designed to maintain consistency and enable stakeholder validation throughout the process. The complete procedure is documented in the [Hierarchical Design Tree Generation Procedure](./procedure.md), which serves as the authoritative execution guide.

**Initialization Process**: Begin with the architectural components from Phase 2 as root nodes. Initialize the tree structure and establish decomposition criteria that will be applied consistently across all levels.

**Level-by-Level Processing**: Work breadth-first through the tree, completing each level before descending:

1. Identify all design nodes at the current level
2. For each design node:

   - Articulate its architectural design and boundaries
   - Propose child nodes based on separation of concerns
   - Classify each child as design or computational
   - Document the decomposition rationale
3. Present the completed level for user confirmation
4. Incorporate feedback and modifications before proceeding

**Classification Criteria**: The fundamental decision at each node — is this design or computational?
- **Design nodes** require further architectural decisions and decompose into children
- **Computational nodes** can be directly implemented without design choices and become leaves
- See the [Classification Guide](./classification-guide.md) for detailed criteria and examples

**Error Handling**: When decomposition becomes ambiguous or circular dependencies emerge, the procedure includes explicit steps for resolution. Document the ambiguity, request clarification, and resume once resolved.

Teams maintain comprehensive documentation throughout, capturing not just the final tree structure but the reasoning behind every decomposition decision. This rationale proves invaluable during implementation when boundary decisions face practical challenges.

<!-- Stopping Criteria -->

Decomposition concludes when teams recognize these conditions:

- All leaf nodes represent computational constructs
- No node requires architectural decisions for implementation
- Tree depth remains manageable (typically 3-5 levels)
- Cross-references between branches are minimal
- User confirms the decomposition granularity is sufficient
- Phase 4 minimization principles suggest no further decomposition would aid system grouping

Generally, these conditions indicate decomposition completeness — every architectural element has been refined to implementable components. The procedure explicitly checks for these conditions at each level, with the final user confirmation gate ensuring stakeholder agreement that further decomposition would introduce implementation details rather than design clarity.

<!-- Output Artifacts -->

At the conclusion of this phase the following artifacts should be published:

- **Hierarchical Design Tree** — Visual diagram showing complete decomposition from architectural roots to computational leaves, annotated with level numbers and node classifications. Typically rendered as a tree or graph structure using tools like Mermaid.

- **Node Classification Registry** — Comprehensive list of all nodes in the tree, sortable by level, type (design/computational), and parent component. Each entry includes the node identifier, classification, and brief description.

- **Decomposition Rationale Log** — Searchable documentation capturing the reasoning behind each decomposition decision, including rejected alternatives, boundary justifications, and user feedback incorporated at each level.

- **Computational Construct Catalog** — Enumerated list of all leaf nodes (computational constructs) with implementation scope descriptions, estimated complexity, and notes on system affinity for Phase 4 grouping. Target range: 40-60 constructs for typical systems.