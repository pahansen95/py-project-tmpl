"""Utility functions for helpers."""

from __future__ import annotations

import logging
import shlex
import subprocess
from typing import Sequence

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

def run_command(cmd: str | Sequence[str], *, check: bool = True, **kwargs) -> subprocess.CompletedProcess:
    """Run a command and log it."""
    if isinstance(cmd, str):
        args = shlex.split(cmd)
    else:
        args = list(cmd)
    logger.info("$ %s", " ".join(shlex.quote(a) for a in args))
    return subprocess.run(args, check=check, **kwargs)
