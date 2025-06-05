# py-project-tmpl

A sample Python project template based on **pyenv**, **uv**, and helper scripts.

## Quickstart

```bash
git clone <repo> && cd py-project-tmpl
python helpers/bootstrap.py          # setup venv and hooks
python helpers/run.py --help         # list helper commands
```

## Helpers

- `python helpers/build.py` – create distribution packages
- `python helpers/test.py` – run pytest
- `python helpers/format.py` – format via Ruff
- `python helpers/lint.py` – lint via Ruff
- `python helpers/docs.py [build|serve]` – MkDocs commands

The project ships with a minimal `pyproject.toml` and `.pre-commit` configuration.

### Dependency groups

Development requirements live in optional groups:

- `builder` – packaging, formatting and documentation tools
- `tester` – pytest and related utilities
