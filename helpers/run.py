"""Helper command dispatcher."""

import argparse
import sys

from .utils import run_command

COMMANDS = {
    "format": "helpers/format.py",
    "lint": "helpers/lint.py",
    "test": "helpers/test.py",
    "docs": "helpers/docs.py",
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Run helper commands")
    parser.add_argument("command", choices=COMMANDS.keys())
    args, unknown = parser.parse_known_args()

    cmd = [sys.executable, COMMANDS[args.command], *unknown]
    run_command(cmd)


if __name__ == "__main__":
    main()
