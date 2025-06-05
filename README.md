# py-project-tmpl

A sample Python project template based on **pyenv**, **uv**, and helper scripts.

## Quickstart

```bash
git clone <repo> && cd py-project-tmpl
python helpers/bootstrap.py          # setup venv and hooks
python helpers/run.py --help         # list helper commands
```

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

