# Agentic Development Instructions

This file provides guidance to agentic development agents when working with code in this repository.

## Imperatives

- Stay focused; work on exactly one file, or task at a time.
- Scope yourself; limit your planning to sets of 3 (or less): tasks, actions, options, etc...
- Before acting, articulate **what** you intend to do and **why**.
- **Always** consult the project-level README to anchor your understanding.

## Planning

- **Keep it simple**: Think it thorugh & identify what is the minimum you need to implement a given request. Be iterative over exhaustive.
- **Test to validate**: Keep tests up to date after making changes to validate your design & intent.
- **Manage Work & Record Knowledge**: Log your work in [the meta/work dir](./meta/kb/). Leave breadcrumbs for yourself & me. Use human descriptive file names.
- **Explicit Mental Models**: Think it through & articulate the mental models of the designs, tasks or domain concepts you're working on. Keep track of them in [the mental-models dir](./models/mental/).
- **Validate yourself**: Use the `alloy` specification language to structurally & procedurally validate your software design. Maintain them in [the models-spec dir](./models/spec/).

## Coding Style Contract

A pragmatic, declarative coding style optimised for clarity, correctness, and auditability in long-lived systems.

### General Principles

- **Style**: Declarative > procedural; concise > clever; readable > minimal.
- **Correctness**: Prefer explicit constraints (types, assertions, validations) over implicit behaviour.
- **Documentation**: Write to explain **what** the code does and **why** it exists—don't narrate *how*.

### Formatting

> NOTE: Styling is enforced as a pre-commit hook

- **Encoding**: UTF-8; LF; limit characterset to ASCII
- **Indentation**: 2 spaces (no tabs)
- **Line Length**: No limits
- **Whitespace**:
  - Group related logic with vertical spacing
  - Avoid excessive blank lines
- **Type Hints**: Required for all public functions and module-level values
- **Runtime Validation**: Use `pydantic` models for all structured input data

### Naming Conventions

| Element   | Style        | Example        |
| --------- | ------------ | -------------- |
| Classes   | `PascalCase` | `UserSession`  |
| Functions | `snake_case` | `parse_config` |
| Variables | `snake_case` | `file_path`    |
| Constants | `UPPERCASE`  | `MAX_RETRIES`  |

### Error Handling

- Always catch specific exception types
- Include descriptive, contextual error messages

  ```python
  raise ValueError("Expected a non-empty list, got empty.")
  ```

### Assertions & Invariants

- Declare assumptions about program state at function boundaries
- Use assertions for sanity checks that should *never* fail during valid execution
- Be liberal in their usage.

### Documentation

- **Docstrings**: Required on public classes and functions
  - Explain *what* it does and *why* it's needed
- **Inline Comments**:
  - Required for any non-obvious logic or constraint
  - Avoid restating the code

### Misc

- Derive minimal declarative spec before generating logic
- Prioritise correctness and testability over code compactness
- Refactor for clarity as code evolves
- Treat type and lint failures as blocking issues
- Escalate ambiguous requirements—ask the user for guidance
