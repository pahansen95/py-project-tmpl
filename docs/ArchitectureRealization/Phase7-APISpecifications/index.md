<!--
Standard Phase Document Structure:

- Salient Summary: Brief overview of the phase's purpose and goals
- Requisite Inputs: What artifacts/knowledge this phase requires
- Implementation Details: How to execute this phase
- Stopping Criteria: When to consider this phase complete
- Output Artifacts: What this phase produces
-->

# Phase 7 — API Specifications

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