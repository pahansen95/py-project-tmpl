# Node Classification Guide

## Overview

The fundamental decision in hierarchical decomposition is classifying each node as either a **design node** or a **computational node**. This classification determines whether further decomposition is needed and ultimately shapes the tree structure.

## Core Classification Criteria

### Design Nodes

A node is classified as **design** when it:

1. **Contains Multiple Responsibilities**
   - The node encompasses several distinct concerns
   - Different aspects could be implemented independently
   - Example: "User Management" contains authentication, authorization, and profile management

2. **Requires Architectural Decisions**
   - Implementation approach is not yet determined
   - Multiple valid implementation strategies exist
   - Example: "Data Persistence" could use files, databases, or cloud storage

3. **Hides Complex Internal Structure**
   - The node abstracts significant complexity
   - Internal organization impacts external behavior
   - Example: "Game State Manager" hides state representation, history, and synchronization

4. **Mixes Abstraction Levels**
   - Contains both high-level coordination and low-level operations
   - Combines policy and mechanism
   - Example: "Resource Optimizer" includes both strategy selection and specific optimizations

### Computational Nodes

A node is classified as **computational** when it:

1. **Has Single, Clear Responsibility**
   - Does one thing well
   - Purpose is immediately obvious from the name
   - Example: "UUID Generator" or "Message Queue"

2. **Maps Directly to Code Constructs**
   - Can be implemented as a specific class, module, or function
   - No design decisions remain
   - Example: "LRU Cache" or "Event Publisher"

3. **Defines Specific Algorithms or Data Structures**
   - Implementation approach is clear
   - Standard patterns apply
   - Example: "Merkle Tree Storage" or "A* Pathfinder"

4. **Requires No Further Decomposition**
   - Adding children would describe implementation, not design
   - Further breakdown enters "how" rather than "what"
   - Example: "JSON Parser" doesn't need children for tokenizer, validator, etc.

## Decision Flowchart

```
Start with a node
    ↓
Can this be implemented directly by a developer?
    ├─ Yes → Does it have a single, clear purpose?
    │         ├─ Yes → COMPUTATIONAL NODE ✓
    │         └─ No → Design Node (multiple responsibilities)
    │
    └─ No → What prevents direct implementation?
            ├─ Multiple approaches possible → Design Node
            ├─ Too many responsibilities → Design Node
            ├─ Mixed abstraction levels → Design Node
            └─ Hidden complexity → Design Node
```

## Examples from Game Engine Architecture

### Entity Component (Level 0) → Design Node

**Why Design?**
- Multiple responsibilities: identity, state, lifecycle, capabilities
- Architectural decisions needed: How to store state? How to manage lifecycle?
- Complex internal structure hidden

**Decomposition**:
```
Entity
├── Identity Management (design)
├── State Management (design)
├── Lifecycle Management (design)
├── Capability Registry (design)
├── Message Handling (design)
└── Event Generation (design)
```

### Identity Management (Level 1) → Design Node

**Why Design?**
- Still contains multiple aspects: UUID generation, type registry, agency classification
- Decisions remain: How to ensure uniqueness? Registry structure?

**Decomposition**:
```
Identity Management
├── UUID Generator (computational)
├── Entity Type Registry (computational)
└── Agency Classifier (computational)
```

### UUID Generator (Level 2) → Computational Node

**Why Computational?**
- Single purpose: Generate unique identifiers
- Clear implementation: Use standard UUID algorithm
- No further design decisions
- Maps to a single function or small class

### State Storage (Level 2) → Computational Node

**Why Computational?**
- Specific purpose: Store entity state with versioning
- Clear data structure: Key-value with vector clocks
- Standard pattern: Versioned storage
- No architectural decisions remain

## Edge Cases and Patterns

### Pattern: Infrastructure vs Application

Infrastructure patterns often become computational nodes earlier:

- "Message Queue" → Computational (well-understood pattern)
- "Game Logic Processor" → Design (application-specific complexity)

### Pattern: Standard Algorithms

Known algorithms are typically computational:

- "Dijkstra Pathfinder" → Computational
- "Physics Engine" → Design (unless using specific library)

### Pattern: Collections and Registries

Simple collections are computational:

- "Entity Registry" → Computational (just a typed collection)
- "Resource Manager" → Design (lifecycle, caching, optimization concerns)

### Pattern: Facades and Adapters

Thin wrappers are computational:

- "Database Adapter" → Computational
- "Storage Abstraction Layer" → Design (multiple backends, strategies)

## Common Mistakes

### Over-Decomposition

**Wrong**: Breaking "JSON Parser" into:

- Token Scanner (too fine-grained)
- Grammar Validator (implementation detail)
- Object Builder (implementation detail)

**Right**: Keep "JSON Parser" as computational node

### Under-Decomposition

**Wrong**: Keeping "Game System" as computational
- Too broad
- Multiple responsibilities hidden
- Many design decisions remain

**Right**: Decompose into Entity, Capability, State, etc.

### Misclassification

**Wrong**: Marking "Event System" as computational when it contains:

- Event routing strategies
- Subscription management
- Delivery guarantees
- Ordering policies

**Right**: Classify as design node and decompose

## Validation Questions

Before finalizing a classification, ask:

1. **For Design Nodes**:

   - What architectural decisions remain?
   - Can I identify distinct sub-responsibilities?
   - Would different developers approach this differently?

2. **For Computational Nodes**:

   - Can I sketch the implementation in my head?
   - Is there essentially one "right way" to build this?
   - Would further decomposition just document the implementation?

## Phase 4 Considerations

When classifying nodes, consider their eventual system grouping:

- **High Cohesion**: Computational nodes that work together
- **Clear Interfaces**: Computational nodes that define system boundaries
- **Shared Resources**: Computational nodes accessing same data
- **Communication Patterns**: Computational nodes with heavy interaction

Document these observations in the decomposition rationale for Phase 4's benefit.