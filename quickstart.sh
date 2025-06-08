#!/usr/bin/env bash
set -euo pipefail

usage() {
  echo "Usage: $(basename "$0") [-C DIR] [-u REMOTE] [--push]" >&2
  echo "  -C DIR    Directory for new project (default: CWD)" >&2
  echo "  -u URL    Configure git remote \"origin\"" >&2
  echo "  --push    Push initial commit to remote" >&2
}

project_dir="."
remote_url=""
push_remote=false

while [ $# -gt 0 ]; do
  case "$1" in
    -C)
      project_dir="$2"
      shift 2
      ;;
    -u)
      remote_url="$2"
      shift 2
      ;;
    --push|-p)
      push_remote=true
      shift 1
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    --)
      shift
      break
      ;;
    *)
      usage
      exit 1
      ;;
  esac
done

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
  if [ "$push_remote" = true ]; then
    git push -u origin HEAD || true
  fi
fi
