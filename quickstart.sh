#!/usr/bin/env bash
set -euo pipefail

# Color support
if [ -t 1 ] && command -v tput >/dev/null 2>&1; then
  RED=$(tput setaf 1); GREEN=$(tput setaf 2); YELLOW=$(tput setaf 3)
  BLUE=$(tput setaf 4); BOLD=$(tput bold); RESET=$(tput sgr0)
else
  RED=""; GREEN=""; YELLOW=""; BLUE=""; BOLD=""; RESET=""
fi

# Progress indicators
info() { printf "${BLUE}ℹ${RESET} %s\n" "$*"; }
success() { printf "${GREEN}✓${RESET} %s\n" "$*"; }
warning() { printf "${YELLOW}⚠${RESET} %s\n" "$*" >&2; }
error() { printf "${RED}✗${RESET} %s\n" "$*" >&2; }

usage() {
  cat >&2 <<EOF
Usage: $(basename "$0") [-C DIR] [-u REMOTE] [-b BRANCH] [--ref REF] [--push]
  -C DIR      Directory for new project (default: CWD)
  -u URL      Configure git remote "origin"
  -b BRANCH   Branch name for new project (default: main)
  --ref REF   Git ref to checkout from template (branch/tag/commit, default: trunk)
  --push      Push initial commit to remote
EOF
}

# Defaults
project_dir="."; remote_url=""; template_ref="trunk"
local_branch="main"; push_remote=false

# Parse arguments
while [ $# -gt 0 ]; do
  case "$1" in
    -C) project_dir="$2"; shift 2 ;;
    -u) remote_url="$2"; shift 2 ;;
    -b) local_branch="$2"; shift 2 ;;
    --ref|-r) template_ref="$2"; shift 2 ;;
    --push|-p) push_remote=true; shift ;;
    -h|--help) usage; exit 0 ;;
    --) shift; break ;;
    *) usage; exit 1 ;;
  esac
done

template_repo="${QUICKSTART_TEMPLATE_REPO:-https://github.com/pahansen95/py-project-tmpl.git}"

# Clone template
info "Cloning template from ${BOLD}$template_repo${RESET} (ref: ${BOLD}$template_ref${RESET})..."
if ! git clone --depth 1 --branch "$template_ref" "$template_repo" "$project_dir" 2>/dev/null; then
  cat >&2 <<EOF
${RED}✗${RESET} Failed to clone template repository
${RED}✗${RESET} Please check the repository URL and ref name
EOF
  exit 1
fi
success "Template cloned successfully"

# Cleanup
info "Cleaning up template files..."
rm -rf "$project_dir/.git" "$project_dir/quickstart.sh"
rm -f "$project_dir/tests/test_quickstart.py"
rm -rf "$project_dir/tests/helpers" "$project_dir/meta/kb/contributor-guide"

# Initialize repository
cd "$project_dir"
info "Initializing new git repository with branch ${BOLD}$local_branch${RESET}..."
git init -b "$local_branch"
git add . && git commit -m "Initial commit from template"
git clean -fd > /dev/null
success "Repository initialized"

# Configure remote
if [ -n "$remote_url" ]; then
  info "Configuring remote ${BOLD}origin${RESET} -> ${BOLD}$remote_url${RESET}"
  git remote add origin "$remote_url"
  success "Remote configured"
  
  if [ "$push_remote" = true ]; then
    info "Pushing to remote..."
    if ! git push -u origin HEAD 2>/dev/null; then
      cat >&2 <<EOF
${YELLOW}⚠${RESET} Failed to push to remote. You may need to:
${YELLOW}⚠${RESET}   - Check your authentication credentials
${YELLOW}⚠${RESET}   - Ensure the remote repository exists
${YELLOW}⚠${RESET}   - Run: git push -u origin HEAD
EOF
    else
      success "Successfully pushed to remote"
    fi
  fi
fi

# Summary
cat <<EOF

${GREEN}${BOLD}✨ Project initialized successfully!${RESET}

📁 Location: ${BOLD}$project_dir${RESET}
🌿 Branch: ${BOLD}$local_branch${RESET}
$([ -n "$remote_url" ] && printf "🔗 Remote: ${BOLD}%s${RESET}\n" "$remote_url")

Next steps:
  ${BOLD}cd $project_dir${RESET}
  ${BOLD}helpers/bootstrap.sh${RESET}  # Set up development environment

EOF
success "Happy coding! 🚀"