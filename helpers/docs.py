"""Build or serve documentation."""

import argparse

from .utils import (
  add_logging_args,
  configure_logging,
  logger,
  run_command,
)


def main(argv: list[str] | None = None) -> None:
  parser = argparse.ArgumentParser()
  add_logging_args(parser)
  parser.add_argument("action", choices=["build", "serve"])
  args = parser.parse_args(argv)

  configure_logging(args.verbose, args.log_file)
  logger.debug("docs action: %s", args.action)
  if args.action == "build":
    run_command("mkdocs build")
  else:
    run_command("mkdocs serve")


if __name__ == "__main__":
  main()
