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

# Dry run handler
dryrun() { [ "$dry_run" = true ] && printf "${YELLOW}[DRY RUN]${RESET} %s\n" "$*"; }
execute() {
  if [ "$dry_run" = true ]; then
    dryrun "$*"
    return 0
  else
    "$@"
  fi
}

usage() {
  cat >&2 <<EOF
Usage: $(basename "$0") [-C DIR] [-u REMOTE] [-b BRANCH] [--ref REF] [--push] [--dry-run] [--no-cleanup]
  -C DIR        Directory for new project (default: CWD)
  -u URL        Configure git remote "origin"
  -b BRANCH     Branch name for new project (default: main)
  --ref REF     Git ref to checkout from template (branch/tag/commit, default: trunk)
  --push        Push initial commit to remote
  --dry-run     Show what would be done without executing
  --no-cleanup  Keep project directory on failure
EOF
}

# Defaults
project_dir="."; remote_url=""; template_ref="trunk"
local_branch="main"; push_remote=false; cleanup_on_fail=true; dry_run=false

# Parse arguments
while [ $# -gt 0 ]; do
  case "$1" in
    -C) project_dir="$2"; shift 2 ;;
    -u) remote_url="$2"; shift 2 ;;
    -b) local_branch="$2"; shift 2 ;;
    --ref) template_ref="$2"; shift 2 ;;
    --push|-p) push_remote=true; shift ;;
    --dry-run) dry_run=true; shift ;;
    --no-cleanup) cleanup_on_fail=false; shift ;;
    -h|--help) usage; exit 0 ;;
    --) shift; break ;;
    *) usage; exit 1 ;;
  esac
done

template_repo="${QUICKSTART_TEMPLATE_REPO:-https://github.com/pahansen95/py-project-tmpl.git}"

# Cleanup handler
project_created=false
cleanup() {
  if [ "$cleanup_on_fail" = true ] && [ "$project_created" = true ] && [ $? -ne 0 ] && [ "$dry_run" = false ]; then
    warning "Cleaning up failed initialization..."
    rm -rf "$project_dir"
  fi
}
trap cleanup EXIT

# Clone template
info "Cloning template from ${BOLD}$template_repo${RESET} (ref: ${BOLD}$template_ref${RESET})..."

if [ "$dry_run" = true ]; then
  dryrun "git clone --branch $template_ref $template_repo $project_dir"
  project_created=true
  clone_status=0
else
  # Detect if ref looks like a commit SHA
  if [[ "$template_ref" =~ ^[0-9a-f]{7,40}$ ]]; then
    # Full clone needed for commit SHAs
    { clone_output=$(git clone "$template_repo" "$project_dir" 2>&1); clone_status=$?; } || true
    if [ $clone_status -eq 0 ]; then
      project_created=true
      cd "$project_dir"
      if ! git checkout "$template_ref" 2>/dev/null; then
        cd - >/dev/null
        cat >&2 <<EOF
${RED}✗${RESET} Failed to checkout commit ${BOLD}$template_ref${RESET}
${RED}✗${RESET} The commit may not exist or may not be reachable from any branch
${RED}✗${RESET} Verify the commit SHA is correct and exists in the repository
EOF
        exit 1
      fi
      cd - >/dev/null
    fi
  else
    # Shallow clone for branches/tags
    { clone_output=$(git clone --depth 1 --branch "$template_ref" "$template_repo" "$project_dir" 2>&1); clone_status=$?; } || true
    [ $clone_status -eq 0 ] && project_created=true
  fi
fi

if [ $clone_status -ne 0 ]; then
  # Analyze error for specific guidance
  if echo "$clone_output" | grep -q "Repository not found\|repository does not exist"; then
    cat >&2 <<EOF
${RED}✗${RESET} Repository not found: ${BOLD}$template_repo${RESET}
${RED}✗${RESET} Check that the repository URL is correct and accessible
${RED}✗${RESET} If using SSH, ensure you have access permissions
EOF
  elif echo "$clone_output" | grep -q "Remote branch .* not found\|couldn't find remote ref"; then
    cat >&2 <<EOF
${RED}✗${RESET} Reference not found: ${BOLD}$template_ref${RESET}
${RED}✗${RESET} The branch, tag, or commit does not exist in the repository
${RED}✗${RESET} Available branches can be listed with:
${RED}✗${RESET}   git ls-remote --heads $template_repo
EOF
  elif echo "$clone_output" | grep -q "Permission denied\|Authentication failed"; then
    cat >&2 <<EOF
${RED}✗${RESET} Authentication failed for ${BOLD}$template_repo${RESET}
${RED}✗${RESET} Check your SSH keys or credentials
${RED}✗${RESET} For SSH URLs, verify your key is added: ssh-add -l
${RED}✗${RESET} For HTTPS URLs, check your access token
EOF
  elif echo "$clone_output" | grep -q "Could not resolve host\|Name or service not known"; then
    cat >&2 <<EOF
${RED}✗${RESET} Network error: cannot reach ${BOLD}$template_repo${RESET}
${RED}✗${RESET} Check your internet connection
${RED}✗${RESET} Verify the repository hostname is correct
EOF
  else
    cat >&2 <<EOF
${RED}✗${RESET} Failed to clone template repository
${RED}✗${RESET} Error: $(echo "$clone_output" | grep -i "fatal:" | head -1 | sed 's/fatal: //')
${RED}✗${RESET} Repository: $template_repo
${RED}✗${RESET} Reference: $template_ref
EOF
  fi
  exit 1
fi
[ "$dry_run" = false ] && success "Template cloned successfully"

# Cleanup
info "Cleaning up template files..."
execute rm -rf "$project_dir/.git" "$project_dir/quickstart.sh"
execute rm -f "$project_dir/tests/test_quickstart.py"
execute rm -rf "$project_dir/tests/helpers" "$project_dir/meta/kb/contributor-guide"

# Initialize repository
[ "$dry_run" = false ] && cd "$project_dir"
info "Initializing new git repository with branch ${BOLD}$local_branch${RESET}..."
execute git init -b "$local_branch"
execute git add .
execute git commit -m "Initial commit from template"
execute git clean -fd
[ "$dry_run" = false ] && success "Repository initialized"

# Configure remote
if [ -n "$remote_url" ]; then
  info "Configuring remote ${BOLD}origin${RESET} -> ${BOLD}$remote_url${RESET}"
  execute git remote add origin "$remote_url"
  [ "$dry_run" = false ] && success "Remote configured"
  
  if [ "$push_remote" = true ]; then
    info "Pushing to remote..."
    if [ "$dry_run" = true ]; then
      dryrun "git push -u origin HEAD"
    else
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
fi

# Return to original directory
[ "$dry_run" = false ] && cd - >/dev/null

# Summary
if [ "$dry_run" = true ]; then
  cat <<EOF

${YELLOW}${BOLD}🔍 Dry run complete!${RESET}

This would have:
  📁 Created project in: ${BOLD}$project_dir${RESET}
  🌿 Initialized branch: ${BOLD}$local_branch${RESET}
  📦 Cloned from: ${BOLD}$template_repo${RESET} (ref: ${BOLD}$template_ref${RESET})
$([ -n "$remote_url" ] && printf "  🔗 Configured remote: ${BOLD}%s${RESET}\n" "$remote_url")
$([ "$push_remote" = true ] && printf "  📤 Pushed to remote\n")

No changes were made. Remove --dry-run to execute.
EOF
else
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
fi

# Mark successful completion to prevent cleanup
trap - EXIT
exit 0