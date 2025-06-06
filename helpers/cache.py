"""Manage project cache directory."""

from __future__ import annotations

import argparse
from pathlib import Path

from .utils import add_logging_args, configure_logging, logger


def ensure_cache(cache_dir: Path, cache_link: Path) -> None:
  """Create *cache_dir* and symlink *cache_link* if needed."""
  if cache_link.exists():
    return

  if not cache_dir.exists():
    logger.info("Initializing Cache")
    cache_dir.mkdir(parents=True, mode=0o755)

  logger.info("Symlinking Cache")
  cache_link.symlink_to(cache_dir)


def main(argv: list[str] | None = None) -> None:
  """Ensure cache directory exists and is linked."""
  parser = argparse.ArgumentParser(prog="cache")
  add_logging_args(parser)
  parser.add_argument("cache_dir", type=Path)
  parser.add_argument("cache_link", type=Path)
  args = parser.parse_args(argv)

  configure_logging(args.verbose, args.log_file)
  ensure_cache(args.cache_dir, args.cache_link)


if __name__ == "__main__":
  main()
