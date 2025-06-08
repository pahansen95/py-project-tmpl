#!/usr/bin/env bash
set -euo pipefail

usage() {
  echo "Usage: $(basename \"$0\") [-C DIR] [-u REMOTE] [-b SRC[:DST]] [--push]" >&2
  echo "  -C DIR      Directory for new project (default: CWD)" >&2
  echo "  -u URL      Configure git remote \"origin\"" >&2
  echo "  -b SRC[:DST] Clone template branch SRC as local DST (default: trunk)" >&2
  echo "  --push      Push initial commit to remote" >&2
}

project_dir="."
remote_url=""
template_branch="trunk"
local_branch=""
push_remote=false
branch_spec=""

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
    -b|--branch)
      branch_spec="$2"
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

# Determine template and local branch names
if [ -n "$branch_spec" ]; then
  if [[ "$branch_spec" == *:* ]]; then
    template_branch="${branch_spec%%:*}"
    local_branch="${branch_spec#*:}"
  else
    template_branch="$branch_spec"
    local_branch="$branch_spec"
  fi
else
  local_branch="$template_branch"
fi

template_repo="${QUICKSTART_TEMPLATE_REPO:-https://github.com/pahansen95/py-project-tmpl.git}"

# Clone the template into the target directory

git clone --depth 1 --branch "$template_branch" "$template_repo" "$project_dir"

# Remove template git history and the quickstart script itself
rm -rf "$project_dir/.git"
rm -f "$project_dir/quickstart.sh"

cd "$project_dir"

# Initialize a new repository and commit the template files

git init -b "$local_branch"

git add .
git commit -m "Initial commit from template"

# Remove any untracked files created during setup
git clean -fd > /dev/null

# Configure remote if provided
if [ -n "$remote_url" ]; then
  git remote add origin "$remote_url"
  if [ "$push_remote" = true ]; then
    git push -u origin HEAD || true
  fi
fi
