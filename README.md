# py-project-tmpl

A sample Python project template based on **pyenv**, **uv**, and helper scripts.

## Quickstart

```bash
git clone <repo> && cd py-project-tmpl
helpers/bootstrap.sh                 # setup dev/test/docs venvs and hooks
helpers/tool --help                  # list helper commands
```

Bootstrap creates three virtual environments under `.venv/`:

- `dev`  – all dependencies for development (stored in `.venv/`)
- `test` – project and test dependencies (stored in `.venv/test`)
- `docs` – documentation build/serve dependencies (stored in `.venv/docs`)

## Prerequisites

The project requires **Python&nbsp;3.13** and the
[uv](https://github.com/astral-sh/uv) package manager. Once both are
available on your ``PATH`` you can run ``helpers/bootstrap.sh`` to create a virtual
environment and install the remaining tools.

### Python 3.13

- **Linux** – install via your package manager or with
  [pyenv](https://github.com/pyenv/pyenv)
- **macOS** – ``brew install python@3.13``
- **Windows** – download the installer from
  [python.org](https://www.python.org/downloads/)

### uv

- **Linux** – ``curl -Ls https://astral.sh/uv/install.sh | sh``
- **macOS** – ``brew install uv``
- **Windows (PowerShell)** – ``irm https://astral.sh/uv/install.ps1 | iex``

## Helpers

- `python -m helpers.tools build` – build distribution packages
- `python -m helpers.tools test` – run pytest
- `python -m helpers.tools format` – format via Ruff (use `--check` to only verify)
- `python -m helpers.tools lint` – lint via Ruff (fixes by default, use `--dry-run` to only check)
- `python -m helpers.tools docs [build|serve]` – MkDocs commands

Alternatively, use the `helpers/tool` wrapper which activates a matching
virtual environment automatically (defaults to `dev`):

```bash
helpers/tool <tool> [args]
```

All helpers support `-v/--verbose` to increase logging detail and
`--log-file` to duplicate logs to a file.

The project ships with a minimal `pyproject.toml` and `.pre-commit` configuration.

### Dependency groups

Development requirements live in optional groups:

- `build` – wheel/sdist build tools
- `dev` – linting, testing, and formatting tools
- `docs` – MkDocs and related tooling

