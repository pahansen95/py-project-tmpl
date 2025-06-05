"""Run tests."""

from __future__ import annotations

import argparse

from .utils import add_logging_args, configure_logging, logger, run_command


def main(argv: list[str] | None = None) -> None:
  parser = argparse.ArgumentParser(prog="test")
  add_logging_args(parser)
  parser.add_argument("extra", nargs=argparse.REMAINDER, help="Extra args for pytest")
  args = parser.parse_args(argv)

  configure_logging(args.verbose, args.log_file)
  logger.debug("extra args: %s", args.extra)
  run_command(["pytest", *args.extra])


if __name__ == "__main__":
  main()
