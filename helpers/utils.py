"""Utility functions for helpers."""

from __future__ import annotations

import logging
import shlex
import subprocess
import sys
from typing import Sequence
import argparse

logger = logging.getLogger(__name__)


def configure_logging(verbosity: int = 0, log_file: str | None = None) -> None:
  """Configure basic logging for helper scripts."""
  level = logging.WARNING - (10 * verbosity)
  if level < logging.DEBUG:
    level = logging.DEBUG

  handlers: list[logging.Handler] = [logging.StreamHandler()]
  if log_file:
    handlers.append(logging.FileHandler(log_file))

  logging.basicConfig(
    level=level,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=handlers,
    force=True,
  )


def run_command(cmd: str | Sequence[str], *, check: bool = True, **kwargs) -> subprocess.CompletedProcess:
  """Run a command and log it."""
  if isinstance(cmd, str):
    args = shlex.split(cmd)
  else:
    args = list(cmd)

  log_args = args.copy()
  if log_args and log_args[0] == sys.executable:
    log_args[0] = "python"

  logger.info("$ %s", " ".join(shlex.quote(a) for a in log_args))
  return subprocess.run(args, check=check, **kwargs)


def add_logging_args(parser: argparse.ArgumentParser) -> None:
  """Add common logging arguments to *parser*."""
  parser.add_argument(
    "-v",
    "--verbose",
    action="count",
    default=0,
    help="Increase log verbosity (can be repeated)",
  )
  parser.add_argument("--log-file", help="Write logs to this file as well")
