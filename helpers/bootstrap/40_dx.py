#!/usr/bin/env python3
"""Layer 4: Developer Experience - Configure git hooks, helpers, and IDE settings."""

from __future__ import annotations

import argparse
import json
import logging
import subprocess
import sys
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)


def setup_logging(verbose: bool = False) -> None:
  """Configure logging to stderr."""
  level = logging.DEBUG if verbose else logging.INFO
  logging.basicConfig(
    level=level,
    format="[L4] %(levelname)s: %(message)s",
    stream=sys.stderr,
  )


def run_command(cmd: list[str], check: bool = True) -> subprocess.CompletedProcess:
  """Execute command and return result."""
  logger.debug("Running: %s", " ".join(cmd))
  return subprocess.run(cmd, capture_output=True, text=True, check=check)


def install_pre_commit_hooks(project_root: Path) -> dict[str, Any]:
  """Install pre-commit hooks in the repository."""
  result = {"pre_commit": {"installed": False, "error": None}}
  
  try:
    # Check if pre-commit is available
    check = run_command(["pre-commit", "--version"], check=False)
    if check.returncode != 0:
      result["pre_commit"]["error"] = "pre-commit not found"
      logger.warning("pre-commit not available, skipping hook installation")
      return result
    
    # Install hooks
    run_command(["pre-commit", "install"], check=True)
    result["pre_commit"]["installed"] = True
    logger.info("Pre-commit hooks installed successfully")
    
  except subprocess.CalledProcessError as e:
    result["pre_commit"]["error"] = str(e)
    logger.error("Failed to install pre-commit hooks: %s", e)
  
  return result


def configure_ide_settings(project_root: Path) -> dict[str, Any]:
  """Create IDE configuration files if not present."""
  result = {"ide_settings": {"vscode": False, "pycharm": False}}
  
  # VS Code settings
  vscode_dir = project_root / ".vscode"
  if not vscode_dir.exists():
    vscode_dir.mkdir(parents=True)
    settings = {
      "python.linting.enabled": True,
      "python.linting.ruffEnabled": True,
      "python.formatting.provider": "none",
      "[python]": {
        "editor.formatOnSave": True,
        "editor.codeActionsOnSave": {
          "source.fixAll.ruff": True
        }
      }
    }
    (vscode_dir / "settings.json").write_text(json.dumps(settings, indent=2))
    result["ide_settings"]["vscode"] = True
    logger.info("Created VS Code settings")
  
  # PyCharm settings
  idea_dir = project_root / ".idea"
  if not idea_dir.exists():
    idea_dir.mkdir(parents=True)
    (idea_dir / ".gitignore").write_text("*\n!.gitignore\n")
    result["ide_settings"]["pycharm"] = True
    logger.info("Created PyCharm directory structure")
  
  return result


def verify_helper_scripts(project_root: Path) -> dict[str, Any]:
  """Verify helper scripts are accessible."""
  result = {"helpers": {"available": [], "missing": []}}
  
  helpers_dir = project_root / "helpers"
  expected_helpers = [
    "bootstrap.py", "build.py", "test.py", "format.py", 
    "lint.py", "docs.py", "python.py", "cache.py"
  ]
  
  for helper in expected_helpers:
    helper_path = helpers_dir / helper
    if helper_path.exists():
      result["helpers"]["available"].append(helper)
    else:
      result["helpers"]["missing"].append(helper)
  
  if result["helpers"]["missing"]:
    logger.warning("Missing helpers: %s", ", ".join(result["helpers"]["missing"]))
  else:
    logger.info("All helper scripts verified")
  
  return result


def main() -> None:
  """Configure developer experience components."""
  parser = argparse.ArgumentParser(description="Layer 4: Developer Experience")
  parser.add_argument("-v", "--verbose", action="store_true", help="Enable debug logging")
  parser.add_argument("--skip-pre-commit", action="store_true", help="Skip pre-commit setup")
  parser.add_argument("--skip-ide", action="store_true", help="Skip IDE configuration")
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
  if not project_root.exists():
    logger.error("Project root does not exist: %s", project_root)
    sys.exit(1)
  
  # Layer 4 operations
  output_state = {
    "layer": 4,
    "name": "developer_experience",
    "project_root": str(project_root),
    "results": {}
  }
  
  # Install pre-commit hooks
  if not args.skip_pre_commit:
    output_state["results"].update(install_pre_commit_hooks(project_root))
  
  # Configure IDE settings
  if not args.skip_ide:
    output_state["results"].update(configure_ide_settings(project_root))
  
  # Verify helper scripts
  output_state["results"].update(verify_helper_scripts(project_root))
  
  # Pass through previous layer data
  if "layers" in input_state:
    output_state["layers"] = input_state["layers"]
  else:
    output_state["layers"] = []
  output_state["layers"].append(output_state.copy())
  
  # Output state to stdout
  json.dump(output_state, sys.stdout, indent=2)
  print()  # Newline for readability
  
  logger.info("Layer 4 configuration complete")


if __name__ == "__main__":
  main()