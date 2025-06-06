#!/usr/bin/env python3
"""Bootstrap orchestrator - Run all layers in sequence or individually."""

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
    format="[Orchestrator] %(levelname)s: %(message)s",
    stream=sys.stderr,
  )


def run_layer(layer_script: Path, input_state: dict[str, Any], args: list[str] = None) -> dict[str, Any]:
  """Run a bootstrap layer and return its output state."""
  cmd = [sys.executable, str(layer_script)]
  if args:
    cmd.extend(args)
  
  logger.info("Running %s", layer_script.name)
  
  # Run layer with input state piped to stdin
  process = subprocess.Popen(
    cmd,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=None,  # Let stderr pass through for logging
    text=True
  )
  
  stdout, _ = process.communicate(json.dumps(input_state))
  
  if process.returncode != 0:
    logger.error("Layer %s failed with exit code %d", layer_script.name, process.returncode)
    return {
      "error": f"Layer {layer_script.name} failed",
      "exit_code": process.returncode
    }
  
  try:
    return json.loads(stdout)
  except json.JSONDecodeError as e:
    logger.error("Failed to parse output from %s: %s", layer_script.name, e)
    return {"error": f"Invalid JSON from {layer_script.name}"}


def print_summary(final_state: dict[str, Any]) -> None:
  """Print a summary of the bootstrap results."""
  print("\n" + "="*60)
  print("Bootstrap Summary")
  print("="*60)
  
  if "layers" not in final_state:
    print("No layer information available")
    return
  
  for layer_data in final_state["layers"]:
    layer_num = layer_data.get("layer", "?")
    layer_name = layer_data.get("name", "unknown")
    print(f"\nLayer {layer_num}: {layer_name}")
    print("-" * 40)
    
    results = layer_data.get("results", {})
    for component, status in results.items():
      if isinstance(status, dict):
        if "installed" in status:
          icon = "✓" if status["installed"] else "✗"
          msg = f"{component}: {icon}"
          if status.get("version"):
            msg += f" ({status['version']})"
          if status.get("error"):
            msg += f" - {status['error']}"
          print(f"  {msg}")
        else:
          # Handle nested results
          print(f"  {component}:")
          for key, value in status.items():
            if isinstance(value, list) and value:
              print(f"    {key}: {', '.join(value)}")
            elif isinstance(value, bool):
              print(f"    {key}: {'✓' if value else '✗'}")
            elif value:
              print(f"    {key}: {value}")


def main(argv: list[str] | None = None) -> int:
  """Orchestrate bootstrap layers.
  
  Args:
    argv: Command line arguments (defaults to sys.argv[1:])
    
  Returns:
    Exit code (0 for success, non-zero for failure)
  """
  parser = argparse.ArgumentParser(description="Bootstrap Orchestrator")
  parser.add_argument("-v", "--verbose", action="store_true", help="Enable debug logging")
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
  parser.add_argument("--output-state", type=Path,
                      help="Save final state to JSON file")
  parser.add_argument("--input-state", type=Path,
                      help="Load initial state from JSON file")
  args = parser.parse_args(argv)
  
  setup_logging(args.verbose)
  
  # Determine which layers to run
  if args.only_layer is not None:
    layers_to_run = [args.only_layer]
  else:
    start_layer = args.from_layer or 0
    end_layer = args.to_layer or 4
    layers_to_run = list(range(start_layer, end_layer + 1))
  
  # Remove skipped layers
  if args.skip_layer:
    layers_to_run = [l for l in layers_to_run if l not in args.skip_layer]
  
  # Find bootstrap directory
  bootstrap_dir = Path(__file__).parent
  
  # Map layer numbers to script files
  layer_scripts = {
    0: "layer_0_foundation.py",
    1: "layer_1_prerequisites.py", 
    2: "layer_2_managed_tools.py",
    3: "layer_3_project_env.py",
    4: "layer_4_dev_experience.py"
  }
  
  # Load initial state if provided
  if args.input_state:
    with open(args.input_state) as f:
      state = json.load(f)
    logger.info("Loaded initial state from %s", args.input_state)
  else:
    state = {"project_root": str(Path.cwd())}
  
  # Dry run - just show what would be executed
  if args.dry_run:
    print("Dry run - would execute:")
    for layer_num in layers_to_run:
      script_name = layer_scripts.get(layer_num)
      if script_name:
        print(f"  Layer {layer_num}: {script_name}")
    return
  
  # Run layers in sequence
  for layer_num in layers_to_run:
    script_name = layer_scripts.get(layer_num)
    if not script_name:
      logger.warning("No script defined for layer %d", layer_num)
      continue
    
    script_path = bootstrap_dir / script_name
    
    # Skip layers 0 and 1 as they're not implemented yet
    if layer_num in [0, 1]:
      logger.info("Skipping layer %d (not implemented)", layer_num)
      continue
    
    if not script_path.exists():
      logger.error("Layer script not found: %s", script_path)
      continue
    
    # Run the layer
    layer_args = ["-v"] if args.verbose else []
    new_state = run_layer(script_path, state, layer_args)
    
    if "error" in new_state:
      logger.error("Bootstrap failed at layer %d: %s", layer_num, new_state["error"])
      if args.output_state:
        new_state["failed_at_layer"] = layer_num
        with open(args.output_state, "w") as f:
          json.dump(new_state, f, indent=2)
      return 1
    
    # Update state for next layer
    state = new_state
  
  # Save final state if requested
  if args.output_state:
    with open(args.output_state, "w") as f:
      json.dump(state, f, indent=2)
    logger.info("Saved final state to %s", args.output_state)
  
  # Print summary
  print_summary(state)
  
  logger.info("Bootstrap complete")
  return 0


if __name__ == "__main__":
  sys.exit(main())