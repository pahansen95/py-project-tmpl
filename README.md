# py-project-tmpl

A sample Python project template based on **pyenv**, **uv**, and helper scripts.

## Quickstart

### `quickstart.sh`

Use the quickstart script to clone this template into a new directory,
wipe its history, and initialise a fresh repository. Provide `-u` to set
the `origin` remote and `--push` to immediately push the initial
commit.

```bash
curl -L https://raw.githubusercontent.com/pahansen95/py-project-tmpl/trunk/quickstart.sh \
  | bash -- -C ./project/path -u git@github.com:username/project.git --push
```

### Manual setup

```bash
git clone <repo> && cd py-project-tmpl
python -m helpers.bootstrap          # setup dev/test/docs venvs and hooks
helpers/tool --help                  # list helper commands
```

Bootstrap creates three virtual environments under `.venv/`:

- `dev`  – all dependencies for development (stored in `.venv/`)
- `test` – project and test dependencies (stored in `.venv/test`)
- `docs` – documentation build/serve dependencies (stored in `.venv/docs`)

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

- `python -m helpers.tools.build` – build distribution packages
- `python -m helpers.tools.test` – run pytest
- `python -m helpers.tools.format` – format via Ruff
- `python -m helpers.tools.lint` – lint via Ruff
- `python -m helpers.tools.docs [build|serve]` – MkDocs commands

Alternatively, use the `helpers/tool` wrapper which activates the required
virtual environment automatically:

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

