<!--
Standard Phase Document Structure:

- Salient Summary: Brief overview of the phase's purpose and goals
- Requisite Inputs: What artifacts/knowledge this phase requires
- Implementation Details: How to execute this phase
- Stopping Criteria: When to consider this phase complete
- Output Artifacts: What this phase produces
-->

# Phase 6 — Project Structural Layout

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