from __future__ import annotations

import logging
import re
import subprocess
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)


def run_command(cmd: list[str], check: bool = True, **kwargs) -> subprocess.CompletedProcess:
  """Execute *cmd* and return the completed process."""
  logger.debug("Running: %s", " ".join(cmd))
  return subprocess.run(cmd, capture_output=True, text=True, check=check, **kwargs)


def verify_venv(venv_path: Path) -> dict[str, Any]:
  """Verify that a virtual environment at *venv_path* is functional."""
  checks = {
    "exists": venv_path.exists(),
    "pyvenv_cfg": (venv_path / "pyvenv.cfg").exists(),
    "python_executable": (venv_path / "bin/python").exists(),
    "pip_functional": False,
    "corrupt": False,
  }

  if all([checks["exists"], checks["pyvenv_cfg"], checks["python_executable"]]):
    result = run_command([str(venv_path / "bin/python"), "-m", "pip", "--version"], check=False)
    checks["pip_functional"] = result.returncode == 0

  checks["valid"] = all(
    [
      checks["exists"],
      checks["pyvenv_cfg"],
      checks["python_executable"],
      checks["pip_functional"],
    ]
  )
  checks["corrupt"] = checks["exists"] and not checks["valid"]
  return checks


def verify_tool(tool_name: str, version_pattern: str | None = None) -> dict[str, Any]:
  """Verify tool installation and optionally match *version_pattern*."""
  result = {"installed": False, "version": None, "compatible": None}

  check = run_command(["which", tool_name], check=False)
  if check.returncode == 0:
    result["installed"] = True
    version_check = run_command([tool_name, "--version"], check=False)
    if version_check.returncode == 0:
      result["version"] = version_check.stdout.strip()
      if version_pattern is not None:
        result["compatible"] = bool(re.search(version_pattern, result["version"]))

  return result
