"""Bootstrap the development environment."""

from __future__ import annotations

import argparse

from .utils import add_logging_args, configure_logging, logger, run_command


def main(argv: list[str] | None = None) -> None:
  """Install dependencies and setup pre-commit."""
  parser = argparse.ArgumentParser(prog="bootstrap")
  add_logging_args(parser)
  parser.add_argument(
    "--ci",
    action="store_true",
    help="Run in CI mode with no prompts",
  )
  args = parser.parse_args(argv)

  configure_logging(args.verbose, args.log_file)
  logger.debug("ci mode: %s", args.ci)
  run_command("uv venv", check=False)
  run_command("uv pip install -r uv.lock", check=False)
  run_command("pre-commit install", check=False)


if __name__ == "__main__":
  main()
