"""Format code with Ruff."""

from __future__ import annotations

import argparse

from .utils import add_logging_args, configure_logging, logger, run_command


def main(argv: list[str] | None = None) -> None:
  parser = argparse.ArgumentParser(prog="format")
  add_logging_args(parser)
  parser.add_argument("paths", nargs=argparse.REMAINDER, help="Paths to format")
  args = parser.parse_args(argv)

  configure_logging(args.verbose, args.log_file)
  logger.debug("paths: %s", args.paths)
  run_command(["ruff", "format", *args.paths])


if __name__ == "__main__":
  main()
