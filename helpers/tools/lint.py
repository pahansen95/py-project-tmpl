"""Lint code with Ruff."""

from __future__ import annotations

import argparse
from helpers.utils import logger, run_command
from helpers.tools import tool, SubParser

VENV_WANT = "dev"


def run(args: argparse.Namespace) -> None:
  logger.debug("paths: %s", args.paths)
  run_command(["ruff", "check", *args.paths])


@tool("lint")
def register(subparsers: SubParser) -> None:
  parser = subparsers.add_parser("lint", help="Lint code with Ruff")
  parser.add_argument("paths", nargs=argparse.REMAINDER, help="Paths to lint")
  parser.set_defaults(func=run)

