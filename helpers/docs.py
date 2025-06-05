"""Build or serve documentation."""

import argparse

from .utils import run_command


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["build", "serve"])
    args = parser.parse_args()

    if args.action == "build":
        run_command("mkdocs build")
    else:
        run_command("mkdocs serve")


if __name__ == "__main__":
    main()
