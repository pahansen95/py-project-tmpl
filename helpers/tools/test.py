"""Run tests."""

from __future__ import annotations

import argparse
import importlib.util
from helpers.utils import logger, run_command
from helpers.tools import tool, SubParser

VENV_WANT = "test"


def run(args: argparse.Namespace) -> None:
  logger.debug("extra args: %s", args.extra)

  cmd = ["pytest"]
  if importlib.util.find_spec("pytest_cov") is None:
    logger.warning("pytest-cov not installed; running without coverage")
    cmd.extend(["-o", "addopts="])

  cmd.extend(args.extra)
  run_command(cmd)


@tool("test")
def register(subparsers: SubParser) -> None:
  parser = subparsers.add_parser("test", help="Run tests")
  parser.add_argument("extra", nargs=argparse.REMAINDER, help="Extra args for pytest")
  parser.set_defaults(func=run)
