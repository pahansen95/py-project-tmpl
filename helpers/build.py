"""Build the package."""

from __future__ import annotations

import argparse

from .utils import run_command


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(prog="build")
    parser.add_argument("extra", nargs=argparse.REMAINDER, help="Extra args for python -m build")
    args = parser.parse_args(argv)

    run_command(["python", "-m", "build", *args.extra])


if __name__ == "__main__":
    main()
