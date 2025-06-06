#!/usr/bin/env python3
"""Bootstrap module main entry point.

This module provides the primary interface for bootstrapping the development
environment. It can be executed as:
  - python -m helpers.bootstrap
  - python helpers/bootstrap/
"""

from __future__ import annotations

import argparse
import sys

from . import orchestrator


def main() -> None:
  """Bootstrap development environment with layered approach."""
  parser = argparse.ArgumentParser(
    description="Bootstrap development environment",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog="""
Layers:
  0 - Foundation (OS, architecture, network)
  1 - Prerequisites (shell, git, base Python)
  2 - Managed Tools (uv, pyenv, Python version)
  3 - Project Environment (venv, dependencies)
  4 - Developer Experience (git hooks, IDE config)

Examples:
  # Full bootstrap (layers 0-4)
  python -m helpers.bootstrap
  
  # Bootstrap only managed tools
  python -m helpers.bootstrap --only-layer 2
  
  # Skip optional components
  python -m helpers.bootstrap --quick
  
  # Minimal setup (venv + deps only)
  python -m helpers.bootstrap --minimal
"""
  )
  
  parser.add_argument("-v", "--verbose", action="store_true", 
                      help="Enable verbose output")
  parser.add_argument("--quick", action="store_true",
                      help="Quick bootstrap (skip optional components)")
  parser.add_argument("--minimal", action="store_true",
                      help="Minimal bootstrap (layers 2-3 only)")
  parser.add_argument("--ci", action="store_true",
                      help="CI mode (non-interactive, fail on warnings)")
  
  # Layer control arguments
  parser.add_argument("--from-layer", type=int, choices=[0, 1, 2, 3, 4],
                      help="Start from specific layer (default: 0)")
  parser.add_argument("--to-layer", type=int, choices=[0, 1, 2, 3, 4],
                      help="Stop after specific layer (default: 4)")
  parser.add_argument("--only-layer", type=int, choices=[0, 1, 2, 3, 4],
                      help="Run only the specified layer")
  parser.add_argument("--skip-layer", type=int, action="append",
                      help="Skip specific layer(s)")
  parser.add_argument("--dry-run", action="store_true",
                      help="Show what would be run without executing")
  
  args = parser.parse_args()
  
  # Build orchestrator arguments
  orch_args = []
  
  if args.verbose:
    orch_args.append("-v")
  
  if args.minimal:
    orch_args.extend(["--from-layer", "2", "--to-layer", "3"])
  elif args.quick:
    # Quick mode - could add layer-specific flags here
    pass
  
  # Pass through layer control arguments
  if args.from_layer is not None:
    orch_args.extend(["--from-layer", str(args.from_layer)])
  if args.to_layer is not None:
    orch_args.extend(["--to-layer", str(args.to_layer)])
  if args.only_layer is not None:
    orch_args.extend(["--only-layer", str(args.only_layer)])
  if args.skip_layer:
    for layer in args.skip_layer:
      orch_args.extend(["--skip-layer", str(layer)])
  if args.dry_run:
    orch_args.append("--dry-run")
  
  # Run the orchestrator
  sys.exit(orchestrator.main(orch_args))


if __name__ == "__main__":
  main()