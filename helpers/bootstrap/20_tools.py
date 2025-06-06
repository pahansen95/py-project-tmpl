#!/usr/bin/env python3
"""Layer 2: Managed Tools - Install and configure uv, pyenv, and Python."""

from __future__ import annotations

import argparse
import json
import logging
import os
import platform
import subprocess
import sys
import urllib.request
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)


def setup_logging(verbose: bool = False) -> None:
  """Configure logging to stderr."""
  level = logging.DEBUG if verbose else logging.INFO
  logging.basicConfig(
    level=level,
    format="[L2] %(levelname)s: %(message)s",
    stream=sys.stderr,
  )


def run_command(cmd: list[str], check: bool = True, **kwargs) -> subprocess.CompletedProcess:
  """Execute command and return result."""
  logger.debug("Running: %s", " ".join(cmd))
  return subprocess.run(cmd, capture_output=True, text=True, check=check, **kwargs)


def check_command_exists(cmd: str) -> bool:
  """Check if a command exists in PATH."""
  result = run_command(["which", cmd], check=False)
  return result.returncode == 0


def install_uv() -> dict[str, Any]:
  """Install uv package manager."""
  result = {"uv": {"installed": False, "version": None, "error": None}}
  
  # Check if already installed
  if check_command_exists("uv"):
    version_result = run_command(["uv", "--version"], check=False)
    if version_result.returncode == 0:
      result["uv"]["installed"] = True
      result["uv"]["version"] = version_result.stdout.strip()
      logger.info("uv already installed: %s", result["uv"]["version"])
      return result
  
  # Install uv
  try:
    logger.info("Installing uv package manager...")
    
    # Download and run installer
    if platform.system() == "Windows":
      # Windows PowerShell installation
      ps_cmd = "irm https://astral.sh/uv/install.ps1 | iex"
      subprocess.run(["powershell", "-Command", ps_cmd], check=True)
    else:
      # Unix-like installation
      installer_url = "https://astral.sh/uv/install.sh"
      with urllib.request.urlopen(installer_url) as response:
        installer_script = response.read().decode('utf-8')
      
      # Run installer
      process = subprocess.Popen(
        ["sh", "-"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
      )
      stdout, stderr = process.communicate(installer_script)
      
      if process.returncode != 0:
        raise subprocess.CalledProcessError(process.returncode, "uv installer", stderr)
    
    # Verify installation
    if check_command_exists("uv"):
      version_result = run_command(["uv", "--version"], check=False)
      result["uv"]["installed"] = True
      result["uv"]["version"] = version_result.stdout.strip()
      logger.info("uv installed successfully: %s", result["uv"]["version"])
    else:
      result["uv"]["error"] = "uv not found after installation"
      logger.error("uv installation verification failed")
      
  except Exception as e:
    result["uv"]["error"] = str(e)
    logger.error("Failed to install uv: %s", e)
  
  return result


def install_pyenv() -> dict[str, Any]:
  """Install pyenv for Python version management."""
  result = {"pyenv": {"installed": False, "version": None, "error": None}}
  
  # Check if already installed
  if check_command_exists("pyenv"):
    version_result = run_command(["pyenv", "--version"], check=False)
    if version_result.returncode == 0:
      result["pyenv"]["installed"] = True
      result["pyenv"]["version"] = version_result.stdout.strip()
      logger.info("pyenv already installed: %s", result["pyenv"]["version"])
      return result
  
  # Platform-specific installation
  system = platform.system()
  
  try:
    if system == "Darwin":  # macOS
      # Try homebrew first
      if check_command_exists("brew"):
        logger.info("Installing pyenv via Homebrew...")
        run_command(["brew", "install", "pyenv"], check=True)
        result["pyenv"]["installed"] = True
      else:
        result["pyenv"]["error"] = "Homebrew not found, manual installation required"
    
    elif system == "Linux":
      logger.info("Installing pyenv via git...")
      
      # Clone pyenv repository
      pyenv_root = Path.home() / ".pyenv"
      if not pyenv_root.exists():
        run_command([
          "git", "clone", 
          "https://github.com/pyenv/pyenv.git", 
          str(pyenv_root)
        ], check=True)
      
      # Add to shell profile
      shell_config = Path.home() / ".bashrc"
      if Path.home() / ".zshrc" in Path.home().iterdir():
        shell_config = Path.home() / ".zshrc"
      
      pyenv_init = '\n# pyenv\nexport PYENV_ROOT="$HOME/.pyenv"\nexport PATH="$PYENV_ROOT/bin:$PATH"\neval "$(pyenv init -)"\n'
      
      if shell_config.exists():
        content = shell_config.read_text()
        if "PYENV_ROOT" not in content:
          shell_config.write_text(content + pyenv_init)
          logger.info("Added pyenv to shell configuration")
      
      result["pyenv"]["installed"] = True
      result["pyenv"]["version"] = "git installation"
      
    elif system == "Windows":
      result["pyenv"]["error"] = "Windows requires pyenv-win, manual installation recommended"
    
    else:
      result["pyenv"]["error"] = f"Unsupported platform: {system}"
    
  except Exception as e:
    result["pyenv"]["error"] = str(e)
    logger.error("Failed to install pyenv: %s", e)
  
  return result


def ensure_python_version(target_version: str) -> dict[str, Any]:
  """Ensure the target Python version is available."""
  result = {
    "python": {
      "version": target_version,
      "available": False,
      "installed": False,
      "error": None
    }
  }
  
  # Check if Python version is already available
  try:
    # Try direct python command
    for python_cmd in [f"python{target_version}", "python3", "python"]:
      if check_command_exists(python_cmd):
        version_check = run_command([python_cmd, "--version"], check=False)
        if version_check.returncode == 0 and target_version in version_check.stdout:
          result["python"]["available"] = True
          result["python"]["installed"] = True
          logger.info("Python %s already available via %s", target_version, python_cmd)
          return result
    
    # Try pyenv if available
    if check_command_exists("pyenv"):
      # Check installed versions
      versions_result = run_command(["pyenv", "versions", "--bare"], check=False)
      if versions_result.returncode == 0:
        installed_versions = versions_result.stdout.strip().split('\n')
        if target_version in installed_versions:
          result["python"]["available"] = True
          result["python"]["installed"] = True
          logger.info("Python %s available via pyenv", target_version)
          return result
      
      # Install via pyenv
      logger.info("Installing Python %s via pyenv...", target_version)
      install_result = run_command(["pyenv", "install", target_version], check=False)
      if install_result.returncode == 0:
        result["python"]["available"] = True
        result["python"]["installed"] = True
        logger.info("Python %s installed successfully", target_version)
      else:
        result["python"]["error"] = f"pyenv install failed: {install_result.stderr}"
    
    else:
      result["python"]["error"] = "pyenv not available for Python installation"
      
  except Exception as e:
    result["python"]["error"] = str(e)
    logger.error("Failed to ensure Python version: %s", e)
  
  return result


def get_project_python_version(project_root: Path) -> str | None:
  """Read Python version from .python-version file."""
  version_file = project_root / ".python-version"
  if version_file.exists():
    return version_file.read_text().strip()
  return None


def main() -> None:
  """Install and configure managed tools."""
  parser = argparse.ArgumentParser(description="Layer 2: Managed Tools")
  parser.add_argument("-v", "--verbose", action="store_true", help="Enable debug logging")
  parser.add_argument("--skip-uv", action="store_true", help="Skip uv installation")
  parser.add_argument("--skip-pyenv", action="store_true", help="Skip pyenv installation")
  parser.add_argument("--skip-python", action="store_true", help="Skip Python installation")
  parser.add_argument("--python", help="Override Python version to install")
  args = parser.parse_args()
  
  setup_logging(args.verbose)
  
  # Read input state from stdin
  if not sys.stdin.isatty():
    try:
      input_state = json.load(sys.stdin)
      logger.debug("Received input state: %s", input_state)
    except json.JSONDecodeError:
      logger.warning("Failed to parse input JSON, using defaults")
      input_state = {}
  else:
    input_state = {}
  
  # Determine project root
  project_root = Path(input_state.get("project_root", Path.cwd()))
  
  # Layer 2 operations
  output_state = {
    "layer": 2,
    "name": "managed_tools",
    "project_root": str(project_root),
    "results": {}
  }
  
  # Install uv
  if not args.skip_uv:
    output_state["results"].update(install_uv())
  
  # Install pyenv (optional, not critical)
  if not args.skip_pyenv:
    output_state["results"].update(install_pyenv())
  
  # Ensure Python version
  if not args.skip_python:
    # Determine target Python version
    python_version = args.python
    if not python_version:
      python_version = get_project_python_version(project_root)
    if not python_version:
      python_version = input_state.get("python_version", "3.13")
    
    output_state["results"].update(ensure_python_version(python_version))
    output_state["python_version"] = python_version
  
  # Check for critical failures
  if not args.skip_uv and not output_state["results"].get("uv", {}).get("installed"):
    logger.error("Critical: uv installation failed")
    output_state["critical_error"] = "uv installation failed"
  
  # Pass through previous layer data
  if "layers" in input_state:
    output_state["layers"] = input_state["layers"]
  else:
    output_state["layers"] = []
  output_state["layers"].append({k: v for k, v in output_state.items() if k != "layers"})
  
  # Output state to stdout
  json.dump(output_state, sys.stdout, indent=2)
  print()  # Newline for readability
  
  logger.info("Layer 2 configuration complete")


if __name__ == "__main__":
  main()