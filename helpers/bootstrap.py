"""Bootstrap the development environment."""

from __future__ import annotations

import argparse

from .utils import run_command


def main(argv: list[str] | None = None) -> None:
    """Install dependencies and setup pre-commit."""
    parser = argparse.ArgumentParser(prog="bootstrap")
    parser.add_argument(
        "--ci",
        action="store_true",
        help="Run in CI mode with no prompts",
    )
    parser.parse_args(argv)

    run_command("uv venv", check=False)
    run_command("uv pip install -r uv.lock", check=False)
    run_command("pre-commit install", check=False)


if __name__ == "__main__":
    main()
