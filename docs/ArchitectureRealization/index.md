# Architectural Realization Framework

## Summary

The framework described in this document details a systematic process to produce software applications from an architectural first mindset.

The process is an iterative refinement loop producing artifacts at each phase:

**Phase 1** — Vision Statement, Mental Models & First Principles

**Phase 2** — Architectural Design Document

**Phase 3** — Hierarchical Design Tree

**Phase 4** — Solution Design Document

**Phase 5** — System Specifications

**Phase 6** — Project Structural Layout

**Phase 7** — API Specifications

**Phase 8** — Implementation

## Phases

<!-- This section details each phase, in order. Each phase subsection details, at a minimum, the what & why of the phase, how to conduct the phase & any resultant artifacts.  -->

### **Phase 1** — Vision Statement, Mental Models & Predicates

<!-- Salient Summary -->

The goal of the first phase is to have key stakeholders articulate their thoughts, thereby forcing fragments of their implicit mental models to be made apparent. Following this, a formal Mental Model is produced & agreed upon. Lastly, the set of predicates that underpin the mental model are produced & agreed upon; this is usually a list of first principles.

<!-- Requisite Inputs -->

The first phase initially relies on a simple problem statement or project description; just enough to initiate probing questions that spawn larger discussions. As the project matures & this end to end process is iterated, this phase can accept any analysis on any part of the project.  

<!-- Implementation Details -->

This phase is largely unconstrained, favoring chaotic & exploratory brainstorming; throughout the process, the knowledge & information recorded is thoroughly analyzed for emergent patterns & knowledge gaps. Identified patterns are noted & explored while research is conducted to close gaps.

<!-- Stopping Criteria -->

This phase concludes once participants collectively agree on the following heuristics being met:

- Conversations devolve to splitting hairs.
- Discussions or Topics diverge off topic.
- There is a lack of available information.

Generally, these heuristics can be described as "Mental Fatigue" or reaching a point of diminishing returns on further brainstorming. 

<!-- Output Artifacts -->

At the conclusion of the phase the following artifacts should be published; usually as a single document:

- **Vision Statement** — A salient description of the project's perfectly completed state and its usage contextualized to its user base.
- **Mental Model** — A comprehensive articulation of the participant's understanding, knowledge & experience as it relates to the project & its domain. The Mental Model should be pedantic & opinionated in how it describes systems, behaviors, structures & all manners of "cognitive" matters.
- **Predicates** — An itemized list of the invariants, assumptions, first principles, tenet, or any other logical constructs that contextualize the sources & frame of mind(s) informing the Mental Model.

Generally, the vision is the `what`, the mental model the *how*, and the predicates the `why`.

### **Phase 2** — Architectural Design Document

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

### **Phase 3** — Hierarchical Design Tree

<!-- Salient Summary -->

The goal of this phase is to systematically decompose the architecture into a hierarchical tree of implementable components. Teams break down high-level architectural components into progressively finer-grained elements until reaching computational constructs that can be directly implemented without further design decisions.

<!-- Requisite Inputs -->

The design tree construction requires the **Architectural Design Document** providing top-level components and their relationships. These architectural boundaries form the root and primary branches of the hierarchical decomposition. Through subsequent iterations, implementation insights may reveal missing components or suggest alternative decompositions; triggering targeted refinements to specific tree branches.

<!-- Implementation Details -->

Decomposition follows a breadth-first approach to maintain consistent abstraction levels across the tree. Teams evaluate each node asking: can this be directly implemented or does it require further design decisions? Design nodes decompose into child components; computational nodes become leaves.

The decomposition process applies consistent criteria:

- Separate concerns with distinct responsibilities
- Identify reusable patterns across branches
- Maintain single responsibility per node
- Balance tree depth with clarity

Teams document decomposition rationale at each level, capturing why specific boundaries were chosen. This rationale proves invaluable during implementation when boundary decisions face practical challenges.

<!-- Stopping Criteria -->

Decomposition concludes when teams recognize these conditions:

- All leaf nodes represent computational constructs
- No node requires architectural decisions for implementation
- Tree depth remains manageable
- Cross-references between branches are minimal

Generally, these conditions indicate decomposition completeness — every architectural element has been refined to implementable components. Further decomposition would introduce implementation details rather than design clarity.

<!-- Output Artifacts -->

At the conclusion of this phase the following artifacts should be published:

- **Hierarchical Design Tree** — Visual diagram showing complete decomposition from architectural root to computational leaves, typically rendered as a tree or graph structure.
- **Node Classification Registry** — Comprehensive list categorizing each node as either design (requiring further decomposition) or computational (ready for implementation).
- **Decomposition Rationale** — Documentation capturing the reasoning behind each decomposition decision, including rejected alternatives and boundary justifications.
- **Computational Construct Catalog** — Enumerated list of all leaf nodes with brief descriptions of their implementation scope.

### **Phase 4** — Solution Design Document

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

#### System Minimization Guidance

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

### **Phase 5** — System Specifications

<!-- Salient Summary -->

The goal of this phase is to articulate and validate the internal design of each system identified in the solution design. Teams define system structures, behaviors, and constraints with sufficient precision for implementation. Specifications focus on system correctness and completeness, not external integration.

<!-- Requisite Inputs -->

System specifications build upon the **Solution Design Document** which identifies the systems and their responsibilities. The **Construct-to-System Mapping** shows which computational constructs each system must implement. Through iterations, implementation discoveries refine specifications; resolving design ambiguities and optimizing internal structures.

<!-- Implementation Details -->

Specification development focuses on internal system design. Teams define data structures, algorithms, and behavioral patterns that realize the system's assigned constructs. Key activities include:

- Define internal state representations and invariants
- Specify state transition rules and constraints  
- Document algorithms and processing logic
- Establish error conditions and recovery procedures
- Create performance requirements and resource bounds

Specifications use formal methods where appropriate — state machines for lifecycle management, invariants for data integrity, pre/post conditions for operations. Teams validate designs through modeling and analysis before implementation begins.

<!-- Stopping Criteria -->

Specifications reach completion when:

- All computational constructs have implementation strategies
- State machines cover all valid transitions
- Invariants are formally stated and verifiable
- Algorithms are fully specified with complexity bounds
- Resource requirements are quantified

Generally, specifications are complete when implementers can code the system without making design decisions. The specification serves as a blueprint for internal implementation.

<!-- Output Artifacts -->

At the conclusion of this phase the following artifacts should be published:

- **System Design Specifications** — Detailed internal design for each system including data structures, algorithms, and behavioral models.
- **State Machine Diagrams** — Visual representations of system states, transitions, and lifecycle management.
- **Invariant Documentation** — Formal statements of conditions that must hold throughout system operation.
- **Algorithm Specifications** — Step-by-step descriptions of core processing logic with complexity analysis.

### **Phase 6** — Project Structural Layout

<!-- Salient Summary -->

The goal of this phase is to organize the identified systems into a coherent source code structure. Teams establish package hierarchies, module boundaries, and internal dependency rules that translate logical architecture into physical file organization. The structure enforces architectural principles through code organization.

<!-- Requisite Inputs -->

The structural layout requires **System Specifications** defining internal system designs and **Solution Design** establishing system boundaries and layers. Programming language conventions and organizational standards provide additional constraints. Implementation experience refines structure through discovered coupling patterns and build performance considerations.

<!-- Implementation Details -->

Project structure follows language-specific patterns while reflecting architectural layers. Teams organize code based on system boundaries and internal cohesion:

- Map systems to package namespaces following naming conventions
- Establish module boundaries based on functional cohesion
- Create directory structures reflecting architectural layers
- Define import rules enforcing dependency direction
- Organize shared utilities and cross-cutting concerns

Internal structure prioritizes developer navigation and comprehension. Related functionality clusters within modules; modules group into packages; packages organize by architectural layer. Import dependencies flow downward through layers without cycles.

<!-- Stopping Criteria -->

The structural layout achieves completion when:

- Every computational construct has a module assignment
- Package boundaries align with system boundaries
- Import dependencies form an acyclic graph
- Shared code has clear ownership
- Build configuration reflects intended structure

Generally, the structure is complete when developers can locate any component through logical navigation and the build system can enforce architectural constraints through import rules.

<!-- Output Artifacts -->

At the conclusion of this phase the following artifacts should be published:

- **Package Hierarchy Diagram** — Visual representation of source code organization showing packages, modules, and their relationships.
- **Module Assignment Matrix** — Comprehensive mapping of computational constructs to specific file locations.
- **Dependency Rules Document** — Import restrictions between packages and layers enforcing architectural boundaries.
- **Code Organization Guide** — Standards for file naming, directory structure, and component placement within the project.

### **Phase 7** — API Specifications

<!-- Salient Summary -->

The goal of this phase is to establish prescriptive contracts defining how users will interact with the system before implementation begins. API specifications create the exported interface — a carefully designed subset of planned functionality with explicit stability guarantees. Teams apply the three-tier model (Exported/Public/Private) to establish contracts that both guide user integration and constrain implementation. For Python projects, this follows the Python API Specification Standard using .pyi stub files.

<!-- Requisite Inputs -->

API specification requires the **Solution Design Document** identifying which systems need external interfaces and the **System Specifications** defining their capabilities. The **Project Structure** suggests natural module boundaries for exports. API design precedes implementation — establishing the contract that implementation must fulfill. Through iterations, implementation challenges may refine the API contract while preserving its prescriptive intent.

<!-- Implementation Details -->

API design establishes contractual interfaces before implementation begins. Teams define how users should interact with the systems, creating prescriptive patterns that guide both usage and implementation:

- Design primary interaction points based on system capabilities
- Apply three-tier model to planned functionality
- Create stub files (.pyi) documenting intended exports
- Write prescriptive documentation with usage examples
- Establish progressive disclosure layers

Stub files declare the contract — what will be available and how it should be used. Implementation must then fulfill this contract, mapping internal functionality to the prescribed interfaces. The API specification drives implementation decisions rather than documenting them after the fact. The three-tier model creates clear boundaries: exported names receive major version stability, public names may change in minor versions, and private implementation remains flexible.

<!-- Stopping Criteria -->

API specifications reach completion when:

- All intended user workflows have designed entry points
- Stub files define complete contractual interfaces
- Documentation prescribes intended usage patterns
- Progressive disclosure layers are fully mapped
- Implementation requirements are unambiguous

Generally, APIs are complete when the contract is sufficient for implementation teams to build conforming code and users to understand intended integration patterns. The specification prescribes both how the system will be used and what must be implemented.

<!-- Output Artifacts -->

At the conclusion of this phase the following artifacts should be published:

- **API Contract Files (.pyi)** — Type-annotated specifications defining the prescribed interface with complete signatures and documentation.
- **Stability Commitment Matrix** — Explicit guarantees for exported (major), public (minor), and private (none) planned interfaces.
- **Progressive Disclosure Guide** — Structured patterns showing how users should progress from basic to advanced usage.
- **Implementation Requirements** — Clear mapping of what must be built to fulfill the API contract.

### **Phase 8** — Implementation

<!-- Salient Summary -->

The goal of this phase is to build a computational model of the semantic model every other phase laid bare. Package source code aligns with system specifications while tests validate adherence of behaviors, structure & invariants. Finally, examples demonstrate API Specs while also demonstrating package intent.

<!-- Requisite Inputs -->

Implementation synthesizes all prior artifacts: **API Specifications** establish the contractual interface, **System Specifications** define internal behaviors and invariants, **Structural Layout** dictates code organization, and **Solution Design** provides the semantic model to realize. Implementation transforms these abstract specifications into a working computational model.

<!-- Implementation Details -->

Development proceeds systematically from semantic model to computational reality. Teams build systems that embody the prescribed behaviors while maintaining specified invariants:

- Implement core domain logic reflecting the mental model
- Encode invariants as runtime assertions and type constraints  
- Structure code to mirror architectural boundaries
- Create comprehensive test suites validating specifications
- Develop examples that demonstrate both API usage and design intent

Each computational construct finds expression in code that preserves its semantic purpose. Tests serve as executable specifications — validating not just functionality but adherence to the complete design. Examples fulfill dual purposes: demonstrating API contracts while revealing the package's conceptual model.

<!-- Stopping Criteria -->

Implementation reaches completion when:

- All semantic behaviors have computational representations
- Invariants are enforced through code structure and runtime checks
- Test coverage validates all specified behaviors  
- Examples illustrate every major use case
- API contracts type-check without errors
- Performance meets specified bounds

Generally, implementation is complete when the computational model faithfully represents the semantic model, with tests and examples proving this alignment.

<!-- Output Artifacts -->

At the conclusion of this phase the following artifacts should be published:

- **Source Code Repository** — Computational model implementing all specifications with clear mapping to semantic concepts.
- **Test Suite** — Executable specifications validating behaviors, structure, and invariants.
- **Example Gallery** — Demonstrations of API usage that reveal package intent and mental models.
- **Implementation Notes** — Documentation of how semantic concepts map to computational structures.