"""Build distribution packages."""

from __future__ import annotations

import argparse

from .utils import add_logging_args, configure_logging, logger, run_command


def main(argv: list[str] | None = None) -> None:
  parser = argparse.ArgumentParser(prog="build")
  add_logging_args(parser)
  parser.add_argument("extra", nargs=argparse.REMAINDER, help="Extra args for python -m build")
  args = parser.parse_args(argv)

  configure_logging(args.verbose, args.log_file)
  logger.debug("extra args: %s", args.extra)
  run_command(["python", "-m", "build", *args.extra])


if __name__ == "__main__":
  main()
