#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "$0")" && pwd)"
root="$(cd "$script_dir/.." && pwd)"

venv_path="$root/.venv"

if [ -z "${VIRTUAL_ENV-}" ] && [ -d "$venv_path" ]; then
  # shellcheck disable=SC1090
  . "$venv_path/bin/activate"
fi

export PYTHONPATH="$root${PYTHONPATH+:$PYTHONPATH}"
exec python -m helpers.bootstrap "$@"
