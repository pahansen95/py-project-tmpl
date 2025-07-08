<!--
Standard Phase Document Structure:

- Salient Summary: Brief overview of the phase's purpose and goals
- Requisite Inputs: What artifacts/knowledge this phase requires
- Implementation Details: How to execute this phase
- Stopping Criteria: When to consider this phase complete
- Output Artifacts: What this phase produces
-->

# Phase 4 — Solution Design Document

<!-- Salient Summary -->

The goal of this phase is to transform the flat collection of computational constructs into a coherent system architecture that becomes the solution design. Teams analyze patterns, dependencies, and relationships among constructs; grouping them into the minimum number of implementable systems that balance complexity with maintainability. The principle of "maximizing the work not done" guides teams to create fewer, more cohesive systems rather than many fragmented ones.

<!-- Requisite Inputs -->

Solution design requires the complete **Hierarchical Design Tree** with all computational constructs identified as leaf nodes. The **Architectural Design Document** provides guiding principles for system boundaries and layering. Through iterations, implementation experience reveals coupling patterns that suggest alternative groupings; refining the solution design for optimal cohesion.

<!-- Implementation Details -->

Design articulation follows a systematic analysis process examining constructs from multiple perspectives. Teams identify recurring patterns across constructs — registries requiring CRUD operations, state machines needing transition logic, or managers handling resource lifecycles. These patterns suggest infrastructure abstractions.

Dependency analysis traces data flow and execution sequences:

- Constructs in tight execution chains group together
- Shared data structures indicate cohesion
- Circular dependencies mandate same-system placement
- Communication overhead guides boundary decisions

Layer classification assigns architectural roles:

- Generic, reusable patterns become infrastructure systems
- Core business logic forms domain systems  
- Orchestration and integration create edge systems

Teams document grouping rationale, creating traceability from individual constructs to their containing systems. This mapping proves essential during specification and implementation phases when construct responsibilities must be located within the solution architecture.

## System Minimization Guidance

The goal is to create the minimum number of systems that effectively organize the computational constructs — maximizing the work not done while maintaining architectural clarity.

**Minimization Principles**:

- Start with the assumption of a single system and split only when necessary
- Prefer larger, cohesive systems over many small ones
- Each system boundary should have a compelling justification
- Fewer systems reduce cognitive load and integration complexity

**Minimization Process**:

1. Begin by placing all constructs in one system
2. Identify forces that require splitting:

   - Fundamentally different architectural concerns (e.g., UI vs persistence)
   - Incompatible deployment requirements (e.g., real-time vs batch)
   - Conflicting resource constraints (e.g., CPU-bound vs I/O-bound)
   - Different lifecycle patterns (e.g., startup vs runtime)
   - Security boundaries requiring isolation
3. Split only along the strongest boundaries first
4. Resist creating systems for:

   - Current team organization
   - Speculative future needs
   - Technology preferences alone
   - Minor variations in functionality
5. After initial grouping, attempt to merge systems that:

   - Have high coupling or frequent communication
   - Share significant data structures
   - Have similar architectural characteristics
   - Could be tested as a unit

**Questions to Challenge System Boundaries**:

- What breaks if these constructs are in the same system?
- Is the boundary driven by essential complexity or accidental?
- Would a single developer struggle to understand the combined system?
- Does splitting actually reduce complexity or just move it?

Remember: Every system boundary creates integration work. The best architecture has the fewest systems that still maintain clarity and meet requirements.

<!-- Stopping Criteria -->

Solution design concludes when these conditions emerge:

- Every computational construct belongs to exactly one system
- System boundaries minimize inter-system communication
- Each system maintains clear, focused responsibilities
- System count is minimized while maintaining clarity
- Dependency graph forms clear layers without cycles

Generally, these conditions indicate design stability — further grouping would over-consolidate responsibilities while further splitting would create communication overhead. The solution design balances implementation complexity with operational efficiency.

<!-- Output Artifacts -->

At the conclusion of this phase the following artifacts should be published:

- **Solution Design Document** — The complete system architecture showing all identified systems, their relationships, layer assignments, and the mapping of computational constructs to systems.
- **System Architecture Diagram** — Visual representation of the solution design with systems organized by architectural layers.
- **Construct-to-System Mapping** — Comprehensive assignment of each computational construct to its containing system.
- **System Responsibility Matrix** — Clear descriptions of each system's purpose, scope, and architectural role within the solution.