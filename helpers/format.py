"""Format code with Ruff."""

from __future__ import annotations

import argparse

from .utils import run_command


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(prog="format")
    parser.add_argument("paths", nargs=argparse.REMAINDER, help="Paths to format")
    args = parser.parse_args(argv)

    run_command(["ruff", "format", *args.paths])


if __name__ == "__main__":
    main()
