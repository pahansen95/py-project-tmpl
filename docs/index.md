# Python Project Template

## Overview

A modern Python project template implementing the **Architecture Realization Framework** — a systematic approach to building software from architectural first principles. This template provides a complete development environment with integrated tooling, documentation standards, and architectural guidance.

## Key Features

- **Architecture-First Development**: Comprehensive 8-phase framework from vision to implementation
- **Modern Python Tooling**: Built on Python 3.13, uv package manager, and pre-configured development environments
- **Documentation Registry**: Centralized paradigms and standards for consistent development
- **Integrated Development Workflow**: Helper scripts, pre-commit hooks, and testing infrastructure

## Quick Navigation

### [Architecture Realization Framework](./ArchitectureRealization/index.md)
A systematic 8-phase process for developing software from architectural principles:

1. **Vision, Models & Predicates** — Establish mental models and first principles
2. **Architectural Design** — Transform concepts into high-level components  
3. **Hierarchical Design Tree** — Decompose architecture into implementable constructs
4. **Solution Design** — Group constructs into cohesive systems
5. **System Specifications** — Define internal behaviors and constraints
6. **Project Structure** — Organize code reflecting architectural boundaries
7. **API Specifications** — Establish prescriptive contracts before implementation
8. **Implementation** — Build computational models of semantic designs

### [Documentation Registry](./Registry/index.md)
Foundational documents defining reusable paradigms and standards:

- **[Automated Development Paradigm](./Registry/AutomatedDevelopment.md)** — Framework for human-guided, agent-implemented development
- **[Python API Specification Standard](./Registry/PyAPISpec.md)** — Three-tier stability model for API design
- **[Narrative Procedural Language](./Registry/NarrativeProceduralLang.md)** — Human-readable procedure expression

## Getting Started

### Prerequisites

Install **Python 3.13** and the [uv](https://github.com/astral-sh/uv) package manager:

#### Python 3.13
- **Linux** – install via your package manager or [pyenv](https://github.com/pyenv/pyenv)
- **macOS** – `brew install python@3.13`
- **Windows** – download from [python.org](https://www.python.org/downloads/)

#### uv Package Manager
- **Linux** – `curl -Ls https://astral.sh/uv/install.sh | sh`
- **macOS** – `brew install uv`
- **Windows (PowerShell)** – `irm https://astral.sh/uv/install.ps1 | iex`

### Quick Setup

Clone the template and run the bootstrap script:

```bash
git clone <repo> && cd py-project-tmpl
helpers/bootstrap.sh                 # setup dev/test/docs venvs and hooks
helpers/tool --help                  # list helper commands
```

Bootstrap creates three virtual environments:
- `dev` – all dependencies for development
- `test` – project and test dependencies  
- `docs` – documentation build dependencies

### Development Workflow

The template provides helper scripts for common tasks:

```bash
helpers/tool lint            # Run linting checks
helpers/tool test           # Execute test suite
helpers/tool docs serve     # Serve documentation locally
helpers/tool docs build     # Build documentation
```

## Project Philosophy

This template embodies several key principles:

- **Architecture First**: Design decisions precede implementation
- **Semantic Modeling**: Computational models reflect conceptual understanding
- **Progressive Refinement**: Iterative development through architectural phases
- **Contract-Driven**: APIs specified before implementation
- **Documentation as Code**: Living documentation integrated with development

## Contributing

When working with this template:

1. Familiarize yourself with the [Architecture Realization Framework](./ArchitectureRealization/index.md)
2. Review relevant [Registry documents](./Registry/index.md) for paradigms and standards
3. Follow the phase-appropriate process for your contribution
4. Maintain alignment between semantic models and computational implementations

## Learn More

- Explore the complete [Architecture Realization Framework](./ArchitectureRealization/index.md)
- Study paradigms in the [Documentation Registry](./Registry/index.md)
- Review the Contributor's Guide for development practices
- Check Claude Developer Guide for AI-assisted development