# Hierarchical Design Tree Generation Procedure

## Purpose
Systematically decompose architectural components into a hierarchical tree structure, distinguishing between design nodes (requiring further decomposition) and computational nodes (ready for implementation).

## Global Invariants
- ALWAYS maintain breadth-first traversal order
- NEVER modify the Mermaid diagram without explicit user instruction
- ALWAYS classify each node as either design or computational
- NEVER proceed to the next level without user confirmation

---

=== INITIALIZATION ===

Assume the architectural design document and call it arch_doc.
Assume the current hierarchical tree structure and call it design_tree.
Assume the root architectural component and call it root_node.

Initialize the design_tree with root_node as the single element at level 0.
Set current_level to 0.

---

=== LEVEL PROCESSING ===

For every level in the decomposition process:

1. Identify all nodes at current_level that are design nodes.
   
2. If no design nodes exist at current_level, then stop here and report "Decomposition complete - all leaf nodes are computational constructs."

3. For every design node in the current level:
   
   a. Articulate the architectural design of this parent node:

      - State the node's primary responsibility
      - Identify its key concerns and boundaries
      - Describe its relationship to sibling nodes
   
   b. Propose a composite set of child nodes:

      - Apply separation of concerns principles
      - Maintain single responsibility per child
      - Balance decomposition granularity
      - Document the rationale for this specific decomposition
   
   c. For every proposed child node:

      - Determine if the node represents a design decision or computational construct
      - If it requires further architectural decisions, then classify as "design node"
      - If it can be directly implemented without design choices, then classify as "computational node"
      - Document the classification rationale
   
   d. Add all child nodes to design_tree under their parent node.

(End per-node decomposition loop)

4. Generate the level summary report:

   - Total nodes processed at current_level
   - Number of design nodes identified
   - Number of computational nodes identified
   - Key decomposition decisions made

5. Present the completed level to the user:

   - Display the updated tree structure for this level
   - Highlight new design vs computational nodes
   - Provide decomposition rationale summary

6. Wait for user confirmation before proceeding.
   
   If the user requests modifications, then:

   - Apply the requested changes to the current level
   - Re-classify affected nodes if necessary
   - Return to step 5
   
   Otherwise, increment current_level and continue.

(End per-level loop)

---

=== OUTPUT ARTIFACTS ===

You should now have:

- **design_tree**: Complete hierarchical structure with all nodes classified
- **node_classification_registry**: Comprehensive list of all nodes with their types
- **decomposition_rationale_log**: Documentation of all decomposition decisions
- **computational_construct_catalog**: List of all leaf nodes ready for implementation

Share the final tree visualization and classification report with the user for validation.

---

=== ERROR HANDLING ===

If decomposition becomes unclear or ambiguous:

- Stop the current node processing
- Document the ambiguity clearly
- Request clarification from the user
- Resume from the problematic node once resolved

If circular dependencies are detected:

- Highlight the circular reference
- Suggest alternative decomposition strategies
- Wait for user guidance

---

## Execution Notes

(This procedure typically reveals 3-5 levels of decomposition for most systems)
(Each level should maintain consistent abstraction - avoid mixing high and low-level concerns)
(The breadth-first approach ensures balanced tree development)

---

## Application to Architecture Realization Framework

When applying this procedure within the Architecture Realization Framework context:

### Starting Point
The root nodes are the 6 architectural components from Phase 2:

- Entity (Logical Layer)
- Capability (Logical Layer)
- Message Broker (Computational Layer)
- State Manager (Bridge Layer)
- Controller (Bridge Layer)
- Microcosm (Bridge Layer)

### Classification Guidelines

**Design Node Indicators:**
- Contains multiple distinct responsibilities
- Hides complex internal structure
- Mixes different abstraction levels
- Cannot be directly coded without further decisions

**Computational Node Indicators:**
- Single, clear responsibility
- Defines specific data structures or algorithms
- Maps directly to code constructs
- Requires no architectural decisions to implement

### Level Processing Example

For the Entity component at Level 0:

1. **Articulate Design**: Entity manages game object lifecycle, state, and interactions
2. **Propose Children**: 

   - Identity Management (design)
   - State Management (design)
   - Lifecycle Management (design)
   - Capability Registry (design)
   - Message Handling (design)
   - Event Generation (design)
3. **Classify Each**: All are design nodes requiring further decomposition
4. **Document Rationale**: Separation follows distinct architectural concerns

### Integration with Phase 4

As you decompose, consider how computational constructs might group into systems:

- Note constructs with tight coupling
- Identify shared data structures
- Mark communication patterns
- Consider deployment boundaries

This forward-looking approach aids Phase 4's system minimization goals.

### Typical Outcomes

- **Tree Depth**: 3-5 levels
- **Computational Constructs**: 40-60 for medium complexity systems
- **Design/Computational Ratio**: Roughly 1:1.5
- **Cross-references**: 10-20% of nodes have dependencies outside their branch