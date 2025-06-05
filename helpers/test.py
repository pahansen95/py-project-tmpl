"""Run tests."""

from __future__ import annotations

import argparse

from .utils import run_command


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(prog="test")
    parser.add_argument("extra", nargs=argparse.REMAINDER, help="Extra args for pytest")
    args = parser.parse_args(argv)

    run_command(["pytest", *args.extra])


if __name__ == "__main__":
    main()
