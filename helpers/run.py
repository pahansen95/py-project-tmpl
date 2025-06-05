"""Helper command dispatcher."""

import argparse
import sys

from .utils import add_logging_args, configure_logging, logger, run_command

COMMANDS = {
  "build": "helpers/build.py",
  "format": "helpers/format.py",
  "lint": "helpers/lint.py",
  "test": "helpers/test.py",
  "docs": "helpers/docs.py",
}


def main(argv: list[str] | None = None) -> None:
  parser = argparse.ArgumentParser(description="Run helper commands")
  add_logging_args(parser)
  parser.add_argument("command", choices=COMMANDS.keys())
  args, unknown = parser.parse_known_args(argv)

  configure_logging(args.verbose, args.log_file)
  logger.debug("dispatching %s", args.command)
  cmd = [sys.executable, COMMANDS[args.command], *unknown]
  run_command(cmd)


if __name__ == "__main__":
  main()
