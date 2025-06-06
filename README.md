# py-project-tmpl

A sample Python project template based on **pyenv**, **uv**, and helper scripts.

## Quickstart

```bash
git clone <repo> && cd py-project-tmpl
python -m helpers.bootstrap          # setup venv and hooks
python helpers/run.py --help         # list helper commands
```

## Prerequisites

The project requires **Python&nbsp;3.13** and the
[uv](https://github.com/astral-sh/uv) package manager. Once both are
available on your ``PATH`` the ``bootstrap`` helper will create a virtual
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

- `python helpers/build.py` – build distribution packages
- `python helpers/test.py` – run pytest
- `python helpers/format.py` – format via Ruff
- `python helpers/lint.py` – lint via Ruff
- `python helpers/docs.py [build|serve]` – MkDocs commands

All helpers support `-v/--verbose` to increase logging detail and
`--log-file` to duplicate logs to a file.

The project ships with a minimal `pyproject.toml` and `.pre-commit` configuration.

### Dependency groups

Development requirements live in optional groups:

- `build` – wheel/sdist build tools
- `dev` – linting, testing, and formatting tools

