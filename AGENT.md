# Agentic Developer Guide

This document provides basic guidance for Agentic Developers interfacing with this project. It reflects needs & expectations at the current moment in time.

## Agent Directives

- Adhere to the principles laid out in the [Contributor's Guide](./CONTRIBUTOR.md).
- Consult the [documentation](./docs/) but the [source code](./src/) is always ground truth.
- Consult the [KnowledgeBase](./meta/kb/) for contextual & supporint information.
- Formatting & Style will be enforced but attempt your best to produce [well formed code](./pyproject.toml).

## Project Lifecycle

> This project is currently in active development.

- Do not concern yourself with backwards compatability; we do not need to implement Shims or other "change the wheels while driving" code.
- API is unstable. Refactor often & early.
- Keep files (modules) loosely coupled; it's okay to duplicate code or semantics, we can always refactor cross cutting concerns later.
- Favor organization by domain/concepts. Favor modules (files) over packages (fodlers).
- Articulate your mental models about the project's functionaity & features. Think through things deeply.
- When implementing new functionality; K.I.S.S. Be iterative & aim to deduplicate, minimize or otherwise reduce the amount of code written.
 
## Tools & Procedures

- When running python & python based tools, you MUST activate the [Python Virtual Environment](./.venv/) first.
- The Python Project is managed via the `uv` command; consult the [Python Project Config](./pyproject.toml) to understand available packages, project metadata & structural concerns.
- We use `pre-commit` to manage Git commit hooks. The current set of hooks is configured in the [pre-commit config](./.pre-commit-config.yaml).
- When tracking files in Git, specifically when adding & removing files/folders, you must update the [Git Ignore](./.gitignore) adhering to the embedded instructions.
- When adding & removing [Documentation](./docs/) you must also update the [MkDocs Config](./mkdocs.yml).
- Scripts & Tools intended to aid development should be maintained under the [Helpers Subdirectory](./helpers/).
- Development related data may be cached under the [Project Cache](./.cache/)
