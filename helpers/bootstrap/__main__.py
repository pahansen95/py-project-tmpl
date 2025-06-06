#!/usr/bin/env python3
"""Bootstrap the development environment - main entry point."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Add parent directory to path to import from helpers
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from . import orchestrator


def main() -> None:
  """Bootstrap development environment with layered approach."""
  parser = argparse.ArgumentParser(
    description="Bootstrap development environment",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog="""
Layers:
  0 - Foundation (OS, architecture, network) [not implemented]
  1 - Prerequisites (shell, git, base Python) [not implemented]
  2 - Managed Tools (uv, pyenv, Python version)
  3 - Project Environment (venv, dependencies)
  4 - Developer Experience (git hooks, IDE config)

Examples:
  # Full bootstrap (layers 2-4)
  python helpers/bootstrap.py
  
  # Bootstrap only managed tools
  python helpers/bootstrap.py --only-layer 2
  
  # Skip pyenv installation
  python helpers/bootstrap.py --skip-layer 2
  
  # Verbose output
  python helpers/bootstrap.py -v
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
  
  # Pass through to orchestrator
  parser.add_argument("--from-layer", type=int, choices=[0, 1, 2, 3, 4],
                      help="Start from specific layer")
  parser.add_argument("--to-layer", type=int, choices=[0, 1, 2, 3, 4],
                      help="Stop after specific layer")
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
    # Quick mode - skip optional tools like pyenv
    if not args.skip_layer:
      args.skip_layer = []
    # Would skip pyenv in layer 2 with a flag when implemented
  
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
  
  # Set default range to layers 2-4 since 0-1 aren't implemented
  if not any(arg in orch_args for arg in ["--from-layer", "--only-layer", "--minimal"]):
    orch_args.extend(["--from-layer", "2"])
  
  # Run the orchestrator
  orchestrator.main(orch_args)


if __name__ == "__main__":
  main()