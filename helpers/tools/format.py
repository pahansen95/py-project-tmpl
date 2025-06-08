"""Format code with Ruff."""

from __future__ import annotations

import argparse
from helpers.utils import logger, run_command
from helpers.tools import tool, SubParser

VENV_WANT = "dev"


def run(args: argparse.Namespace) -> None:
  logger.debug("paths: %s", args.paths)
  run_command(["ruff", "format", *args.paths])


@tool("format")
def register(subparsers: SubParser) -> None:
  parser = subparsers.add_parser("format", help="Format code with Ruff")
  parser.add_argument("paths", nargs=argparse.REMAINDER, help="Paths to format")
  parser.set_defaults(func=run)

