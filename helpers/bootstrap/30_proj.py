#!/usr/bin/env python3
"""Layer 3: Project Environment - Setup virtual environment and install dependencies."""

from __future__ import annotations

import argparse
import json
import logging
import subprocess
import sys
from pathlib import Path
import shutil
from typing import Any

from .state import BootstrapState
from .verify import verify_venv, verify_tool
from ..tools import python as pytools
from ..utils import configure_logging, run_command

logger = logging.getLogger(__name__)


def create_virtual_environment(project_root: Path, python_version: str | None = None) -> dict[str, Any]:
  """Create project virtual environment using uv."""
  result = {"venv": {"created": False, "path": None, "error": None}}

  venv_path = project_root / ".venv"

  try:
    if venv_path.exists():
      verification = verify_venv(venv_path)
      if verification["valid"]:
        logger.info("Valid virtual environment exists at %s", venv_path)
        result["venv"]["created"] = True
        result["venv"]["path"] = str(venv_path)
        return result
      if verification["corrupt"]:
        logger.warning("Invalid venv detected, recreating...")
        shutil.rmtree(venv_path)

    args = argparse.Namespace(
      name="default",
      force=False,
      symlink_parent=None,
      directory=project_root,
      verbose=0,
      log_file=None,
    )
    pytools.create_venv(args)
    result["venv"]["created"] = True
    result["venv"]["path"] = str(venv_path)
    logger.info("Created virtual environment at %s", venv_path)

  except subprocess.CalledProcessError as e:
    result["venv"]["error"] = f"Failed to create venv: {e}"
    logger.error("Virtual environment creation failed: %s", e)

  return result


def install_dependencies(project_root: Path, venv_path: Path) -> dict[str, Any]:
  """Install project dependencies from uv.lock."""
  result = {"dependencies": {"base": {"installed": False, "error": None}, "dev": {"installed": False, "error": None}}}

  # Install base dependencies
  lock_file = project_root / "uv.lock"
  if lock_file.exists():
    try:
      args = argparse.Namespace(group="base", venv="default", directory=project_root, verbose=0, log_file=None)
      pytools.install_deps(args)
      result["dependencies"]["base"]["installed"] = True
      logger.info("Base dependencies installed successfully")
    except subprocess.CalledProcessError as e:
      result["dependencies"]["base"]["error"] = str(e)
      logger.error("Failed to install base dependencies: %s", e)
  else:
    result["dependencies"]["base"]["error"] = "uv.lock not found"
    logger.warning("No uv.lock file found, skipping base dependency installation")

  # Install dev dependencies
  try:
    args = argparse.Namespace(group="dev", venv="default", directory=project_root, verbose=0, log_file=None)
    pytools.install_deps(args)
    result["dependencies"]["dev"]["installed"] = True
    logger.info("Development dependencies installed successfully")
  except subprocess.CalledProcessError as e:
    logger.debug("Failed to install dev dependencies (may not exist): %s", e)
    result["dependencies"]["dev"]["error"] = "No dev group or installation failed"

  return result


def install_development_tools(venv_path: Path) -> dict[str, Any]:
  """Install essential development tools in the virtual environment."""
  result = {"dev_tools": {"pre_commit": False, "mkdocs": False}}

  tools = [
    ("pre-commit", "pre_commit"),
    ("mkdocs", "mkdocs"),
  ]

  for package, result_key in tools:
    try:
      cmd = ["uv", "pip", "install", package, "--python", str(venv_path)]
      run_command(cmd, check=True)
      result["dev_tools"][result_key] = True
      logger.info("Installed %s", package)
    except subprocess.CalledProcessError:
      logger.debug("Failed to install %s (may already be in dependencies)", package)

  return result


def verify_project_structure(project_root: Path) -> dict[str, Any]:
  """Verify essential project files exist."""
  result = {"project_files": {"present": [], "missing": []}}

  essential_files = [
    "pyproject.toml",
    "README.md",
    ".gitignore",
  ]

  for file_name in essential_files:
    file_path = project_root / file_name
    if file_path.exists():
      result["project_files"]["present"].append(file_name)
    else:
      result["project_files"]["missing"].append(file_name)

  if result["project_files"]["missing"]:
    logger.warning("Missing project files: %s", ", ".join(result["project_files"]["missing"]))

  return result


def verify_dev_tools(venv_path: Path) -> dict[str, Any]:
  """Verify that development tools are available."""
  return {
    "dev_tools": {"pre_commit": verify_tool("pre-commit")["installed"], "mkdocs": verify_tool("mkdocs")["installed"]}
  }


def verify_dependencies_accessible(venv_path: Path) -> dict[str, Any]:
  """Check that pip is functional inside the venv."""
  res = run_command(["uv", "pip", "list", "--python", str(venv_path)], check=False)
  return {"dependencies": {"accessible": res.returncode == 0}}


def main() -> None:
  """Setup project environment."""
  parser = argparse.ArgumentParser(description="Layer 3: Project Environment")
  parser.add_argument("-v", "--verbose", action="store_true", help="Enable debug logging")
  parser.add_argument("--python", help="Python version to use for venv")
  parser.add_argument("--skip-deps", action="store_true", help="Skip dependency installation")
  parser.add_argument("--skip-tools", action="store_true", help="Skip dev tool installation")
  args = parser.parse_args()

  configure_logging(args.verbose)

  if not sys.stdin.isatty():
    try:
      input_state = json.load(sys.stdin)
      logger.debug("Received input state: %s", input_state)
    except json.JSONDecodeError:
      logger.warning("Failed to parse input JSON, using defaults")
      input_state = {}
  else:
    input_state = {}

  if "project_root" not in input_state:
    input_state["project_root"] = str(Path.cwd())

  state = BootstrapState.from_dict(input_state)
  project_root = Path(state.project_root)
  python_version = args.python or state.installed_tools.get("python", {}).get("version")

  if not project_root.exists():
    logger.error("Project root does not exist: %s", project_root)
    sys.exit(1)

  layer_results: dict[str, Any] = {}

  layer_results.update(verify_project_structure(project_root))

  venv_path = project_root / ".venv"
  initial_venv = verify_venv(venv_path)
  state.record_verification("venv", initial_venv)
  if initial_venv["valid"]:
    state.record_decision("venv", "reuse")
  else:
    venv_result = create_virtual_environment(project_root, python_version)
    layer_results.update(venv_result)
    state.record_decision("venv", "create" if venv_result["venv"]["created"] else "fail")
    state.record_verification("venv", verify_venv(venv_path))

  if (venv_path / "bin/python").exists():
    # Install dependencies
    if not args.skip_deps:
      layer_results.update(install_dependencies(project_root, venv_path))
      dep_verify = verify_dependencies_accessible(venv_path)
      state.record_verification("dependencies", dep_verify)

    # Install development tools
    if not args.skip_tools:
      layer_results.update(install_development_tools(venv_path))
      state.record_decision("dev_tools", "install")
      state.record_verification("dev_tools", verify_dev_tools(venv_path))
    else:
      state.record_decision("dev_tools", "skip")

  # Pass through previous layer data
  state.layer = 3
  state.layers.append({"layer": 3, "name": "project_environment", "results": layer_results})

  # Output state to stdout
  json.dump(state.to_dict(), sys.stdout, indent=2)
  print()

  logger.info("Layer 3 configuration complete")


if __name__ == "__main__":
  main()
