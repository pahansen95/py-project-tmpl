#!/usr/bin/env bash
set -euo pipefail

usage() {
  echo "Usage: $(basename "$0") [-C DIR] [-u REMOTE]" >&2
  echo "  -C DIR   Directory for new project (default: CWD)" >&2
  echo "  -u URL   Configure git remote \"origin\"" >&2
}

project_dir="."
remote_url=""

while getopts ":C:u:h" opt; do
  case "${opt}" in
    C) project_dir="${OPTARG}" ;;
    u) remote_url="${OPTARG}" ;;
    h) usage; exit 0 ;;
    *) usage; exit 1 ;;
  esac
done
shift $((OPTIND - 1))

template_repo="${QUICKSTART_TEMPLATE_REPO:-https://github.com/pahansen95/py-project-tmpl.git}"

# Clone the template into the target directory

git clone --depth 1 --branch trunk "$template_repo" "$project_dir"

# Remove template git history
rm -rf "$project_dir/.git"

cd "$project_dir"

# Initialize a new repository and commit the template files

git init -b trunk

git add .
git commit -m "Initial commit from template"

# Configure remote if provided
if [ -n "$remote_url" ]; then
  git remote add origin "$remote_url"
fi
