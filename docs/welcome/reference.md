# Quick Reference

<div class="progress-tree">
<ul>
  <li class="completed">
    <span class="icon">✓</span>
    <span class="step-name">Overview</span>
    <span class="time">(10 min)</span>
  </li>
  <li class="completed">
    <span class="icon">✓</span>
    <span class="step-name">Setup</span>
    <span class="time">(15 min)</span>
  </li>
  <li class="completed">
    <span class="icon">✓</span>
    <span class="step-name">Workflow</span>
    <span class="time">(20 min)</span>
  </li>
  <li class="current">
    <span class="icon">▶</span>
    <span class="step-name">Reference</span>
    <span class="time">(as needed)</span>
  </li>
</ul>
</div>

## Navigation
[Commands](#command-tables) | [Platform Differences](#platform-differences) | [Troubleshooting](#troubleshooting) | [Configuration](#configuration) | [Emergency](#emergency-commands) | [Glossary](#glossary) | [Printable Card](quick-reference-card.md)

## Command Tables

### Git Operations

#### Clone Repository

=== "Windows"
    ```powershell
    git clone [url]
    ```

=== "macOS"
    ```bash
    git clone [url]
    ```

=== "Linux"
    ```bash
    git clone [url]
    ```

**Output**: Local repository created

#### Create Branch

=== "Windows"
    ```powershell
    git checkout -b [name]
    ```

=== "macOS"
    ```bash
    git checkout -b [name]
    ```

=== "Linux"
    ```bash
    git checkout -b [name]
    ```

**Output**: Switched to new branch

#### Stage Changes

=== "Windows"
    ```powershell
    git add .
    ```

=== "macOS"
    ```bash
    git add .
    ```

=== "Linux"
    ```bash
    git add .
    ```

**Output**: Changes staged

#### Commit Changes

=== "Windows"
    ```powershell
    git commit -m "[msg]"
    ```

=== "macOS"
    ```bash
    git commit -m "[msg]"
    ```

=== "Linux"
    ```bash
    git commit -m "[msg]"
    ```

**Output**: Commit created

#### Push Branch

=== "Windows"
    ```powershell
    git push -u origin [branch]
    ```

=== "macOS"
    ```bash
    git push -u origin [branch]
    ```

=== "Linux"
    ```bash
    git push -u origin [branch]
    ```

**Output**: Branch pushed, PR URL

#### Pull Changes

=== "Windows"
    ```powershell
    git pull origin main
    ```

=== "macOS"
    ```bash
    git pull origin main
    ```

=== "Linux"
    ```bash
    git pull origin main
    ```

**Output**: Local updated

#### Check Status

=== "Windows"
    ```powershell
    git status
    ```

=== "macOS"
    ```bash
    git status
    ```

=== "Linux"
    ```bash
    git status
    ```

**Output**: Working tree status

#### View Log

=== "Windows"
    ```powershell
    git log --oneline -10
    ```

=== "macOS"
    ```bash
    git log --oneline -10
    ```

=== "Linux"
    ```bash
    git log --oneline -10
    ```

**Output**: Recent commits

#### Show Differences

=== "Windows"
    ```powershell
    git diff
    ```

=== "macOS"
    ```bash
    git diff
    ```

=== "Linux"
    ```bash
    git diff
    ```

**Output**: Unstaged changes

### Python/UV Commands

#### Create Virtual Environment

=== "Windows"
    ```powershell
    uv venv
    ```

=== "macOS"
    ```bash
    uv venv
    ```

=== "Linux"
    ```bash
    uv venv
    ```

**Purpose**: New .venv directory

#### Activate Virtual Environment

=== "Windows"
    ```powershell
    .venv\Scripts\activate
    ```

=== "macOS"
    ```bash
    source .venv/bin/activate
    ```

=== "Linux"
    ```bash
    source .venv/bin/activate
    ```

**Purpose**: Enter virtual environment

#### Install Package

=== "Windows"
    ```powershell
    uv pip install [pkg]
    ```

=== "macOS"
    ```bash
    uv pip install [pkg]
    ```

=== "Linux"
    ```bash
    uv pip install [pkg]
    ```

**Purpose**: Add dependency

#### Install Project

=== "Windows"
    ```powershell
    uv pip install -e ".[dev]"
    ```

=== "macOS"
    ```bash
    uv pip install -e ".[dev]"
    ```

=== "Linux"
    ```bash
    uv pip install -e ".[dev]"
    ```

**Purpose**: Development mode

#### List Packages

=== "Windows"
    ```powershell
    uv pip list
    ```

=== "macOS"
    ```bash
    uv pip list
    ```

=== "Linux"
    ```bash
    uv pip list
    ```

**Purpose**: Show installed

#### Run Tests

=== "Windows"
    ```powershell
    pytest
    ```

=== "macOS"
    ```bash
    pytest
    ```

=== "Linux"
    ```bash
    pytest
    ```

**Purpose**: Execute test suite

#### Format Code

=== "Windows"
    ```powershell
    ruff format .
    ```

=== "macOS"
    ```bash
    ruff format .
    ```

=== "Linux"
    ```bash
    ruff format .
    ```

**Purpose**: Auto-format Python

#### Check Code

=== "Windows"
    ```powershell
    ruff check .
    ```

=== "macOS"
    ```bash
    ruff check .
    ```

=== "Linux"
    ```bash
    ruff check .
    ```

**Purpose**: Find issues

## Platform Differences

### Quick Reference
| Component | Windows | macOS/Linux |
|-----------|---------|-------------|
| Home Directory | `%USERPROFILE%` or `$env:USERPROFILE` | `~` or `$HOME` |
| Path Separator | `\` (backslash) | `/` (forward slash) |
| Shell | PowerShell, Git Bash | bash, zsh |
| Admin Mode | Run as Administrator | `sudo` prefix |
| Line Endings | CRLF (`\r\n`) | LF (`\n`) |
| Package Manager | `winget`, `choco` | `brew`, `apt`, `dnf` |

### Path Examples

#### SSH Directory

=== "Windows"
    ```powershell
    # PowerShell
    $env:USERPROFILE\.ssh\
    
    # Git Bash
    ~/.ssh/
    ```

=== "macOS"
    ```bash
    ~/.ssh/
    ```

=== "Linux"
    ```bash
    ~/.ssh/
    ```

#### Python Scripts

=== "Windows"
    ```powershell
    python script.py
    ```

=== "macOS"
    ```bash
    python3 script.py
    ```

=== "Linux"
    ```bash
    python3 script.py
    ```

### Branch Operations

#### List Local Branches

=== "Windows"
    ```powershell
    git branch -v
    ```

=== "macOS"
    ```bash
    git branch -v
    ```

=== "Linux"
    ```bash
    git branch -v
    ```

**Result**: Shows branches with last commit

#### List Remote Branches

=== "Windows"
    ```powershell
    git branch -r
    ```

=== "macOS"
    ```bash
    git branch -r
    ```

=== "Linux"
    ```bash
    git branch -r
    ```

**Result**: Shows origin branches

#### Switch Branch

=== "Windows"
    ```powershell
    git checkout [name]
    ```

=== "macOS"
    ```bash
    git checkout [name]
    ```

=== "Linux"
    ```bash
    git checkout [name]
    ```

**Result**: Changes active branch

#### Delete Local Branch

=== "Windows"
    ```powershell
    git branch -d [name]
    ```

=== "macOS"
    ```bash
    git branch -d [name]
    ```

=== "Linux"
    ```bash
    git branch -d [name]
    ```

**Result**: Removes merged branch

#### Delete Remote Branch

=== "Windows"
    ```powershell
    git push origin --delete [name]
    ```

=== "macOS"
    ```bash
    git push origin --delete [name]
    ```

=== "Linux"
    ```bash
    git push origin --delete [name]
    ```

**Result**: Removes from GitHub

#### Update Branch List

=== "Windows"
    ```powershell
    git fetch --prune
    ```

=== "macOS"
    ```bash
    git fetch --prune
    ```

=== "Linux"
    ```bash
    git fetch --prune
    ```

**Result**: Syncs branch list

## Troubleshooting

### Authentication
**SSH Key Setup**

=== "Windows"
    ```powershell
    # Generate key
    ssh-keygen -t ed25519 -C "email@example.com"
    
    # Start agent (Git Bash)
    eval "$(ssh-agent -s)"
    
    # Add key
    ssh-add ~/.ssh/id_ed25519
    
    # Display public key
    type $env:USERPROFILE\.ssh\id_ed25519.pub
    
    # Set remote URL
    git remote set-url origin git@github.com:USER/REPO.git
    ```

=== "macOS"
    ```bash
    # Generate key
    ssh-keygen -t ed25519 -C "email@example.com"
    
    # Start agent
    eval "$(ssh-agent -s)"
    
    # Add key
    ssh-add ~/.ssh/id_ed25519
    
    # Display public key
    cat ~/.ssh/id_ed25519.pub
    
    # Set remote URL
    git remote set-url origin git@github.com:USER/REPO.git
    ```

=== "Linux"
    ```bash
    # Generate key
    ssh-keygen -t ed25519 -C "email@example.com"
    
    # Start agent
    eval "$(ssh-agent -s)"
    
    # Add key
    ssh-add ~/.ssh/id_ed25519
    
    # Display public key
    cat ~/.ssh/id_ed25519.pub
    
    # Set remote URL
    git remote set-url origin git@github.com:USER/REPO.git
    ```

**Token Authentication**

=== "Windows"
    ```powershell
    # Create at github.com/settings/tokens
    git remote set-url origin https://[TOKEN]@github.com/[USER]/[REPO].git
    ```

=== "macOS"
    ```bash
    # Create at github.com/settings/tokens
    git remote set-url origin https://[TOKEN]@github.com/[USER]/[REPO].git
    ```

=== "Linux"
    ```bash
    # Create at github.com/settings/tokens
    git remote set-url origin https://[TOKEN]@github.com/[USER]/[REPO].git
    ```

### Merge Conflicts

=== "Windows"
    ```powershell
    git status                    # See conflicted files
    # Edit files to resolve
    # Remove <<<, ===, >>> markers
    git add [resolved-file]
    git commit -m "Resolve conflicts"
    git push
    ```

=== "macOS"
    ```bash
    git status                    # See conflicted files
    # Edit files to resolve
    # Remove <<<, ===, >>> markers
    git add [resolved-file]
    git commit -m "Resolve conflicts"
    git push
    ```

=== "Linux"
    ```bash
    git status                    # See conflicted files
    # Edit files to resolve
    # Remove <<<, ===, >>> markers
    git add [resolved-file]
    git commit -m "Resolve conflicts"
    git push
    ```

### Common Errors
| Error | Fix | Time |
|-------|-----|------|
| `rejected push` | `git pull origin main` first | 2 min |
| `divergent branches` | `git pull --rebase origin main` | 3 min |
| `detached HEAD` | `git checkout main` | 30 sec |
| `command not found` | Restart terminal | 1 min |
| `permission denied` | Check SSH: `ssh -T git@github.com` | 5 min |

### Wrong Branch Fixes

#### Uncommitted Changes on Wrong Branch

=== "Windows"
    ```powershell
    git stash
    git checkout correct-branch
    git stash pop
    ```

=== "macOS"
    ```bash
    git stash
    git checkout correct-branch
    git stash pop
    ```

=== "Linux"
    ```bash
    git stash
    git checkout correct-branch
    git stash pop
    ```

#### Committed to Wrong Branch

=== "Windows"
    ```powershell
    git branch correct-branch     # Create branch with commits
    git reset --hard HEAD~1       # Remove from current
    git checkout correct-branch   # Switch to new branch
    ```

=== "macOS"
    ```bash
    git branch correct-branch     # Create branch with commits
    git reset --hard HEAD~1       # Remove from current
    git checkout correct-branch   # Switch to new branch
    ```

=== "Linux"
    ```bash
    git branch correct-branch     # Create branch with commits
    git reset --hard HEAD~1       # Remove from current
    git checkout correct-branch   # Switch to new branch
    ```

## Configuration

### Git Setup

=== "Windows"
    ```powershell
    git config --global user.name "Your Name"
    git config --global user.email "email@example.com"
    git config --global init.defaultBranch main
    git config --global pull.rebase false
    git config --global push.default current
    ```

=== "macOS"
    ```bash
    git config --global user.name "Your Name"
    git config --global user.email "email@example.com"
    git config --global init.defaultBranch main
    git config --global pull.rebase false
    git config --global push.default current
    ```

=== "Linux"
    ```bash
    git config --global user.name "Your Name"
    git config --global user.email "email@example.com"
    git config --global init.defaultBranch main
    git config --global pull.rebase false
    git config --global push.default current
    ```

#### Line Ending Configuration

=== "Windows"
    ```powershell
    git config --global core.autocrlf true
    ```

=== "macOS"
    ```bash
    git config --global core.autocrlf input
    ```

=== "Linux"
    ```bash
    git config --global core.autocrlf input
    ```

### Useful Aliases

=== "Windows"
    ```powershell
    git config --global alias.st "status -sb"
    git config --global alias.co checkout
    git config --global alias.br branch
    git config --global alias.cm commit
    git config --global alias.unstage "reset HEAD --"
    git config --global alias.last "log -1 HEAD"
    git config --global alias.visual "log --graph --oneline --all"
    ```

=== "macOS"
    ```bash
    git config --global alias.st "status -sb"
    git config --global alias.co checkout
    git config --global alias.br branch
    git config --global alias.cm commit
    git config --global alias.unstage "reset HEAD --"
    git config --global alias.last "log -1 HEAD"
    git config --global alias.visual "log --graph --oneline --all"
    ```

=== "Linux"
    ```bash
    git config --global alias.st "status -sb"
    git config --global alias.co checkout
    git config --global alias.br branch
    git config --global alias.cm commit
    git config --global alias.unstage "reset HEAD --"
    git config --global alias.last "log -1 HEAD"
    git config --global alias.visual "log --graph --oneline --all"
    ```

## Emergency Commands

### Undo Operations

=== "Windows"
    ```powershell
    git reset --soft HEAD~1      # Undo commit, keep changes
    git reset --hard HEAD~1      # Undo commit, discard changes
    git checkout -- .            # Discard all changes
    git clean -fd               # Remove untracked files
    git rm --cached file.txt    # Untrack file
    ```

=== "macOS"
    ```bash
    git reset --soft HEAD~1      # Undo commit, keep changes
    git reset --hard HEAD~1      # Undo commit, discard changes
    git checkout -- .            # Discard all changes
    git clean -fd               # Remove untracked files
    git rm --cached file.txt    # Untrack file
    ```

=== "Linux"
    ```bash
    git reset --soft HEAD~1      # Undo commit, keep changes
    git reset --hard HEAD~1      # Undo commit, discard changes
    git checkout -- .            # Discard all changes
    git clean -fd               # Remove untracked files
    git rm --cached file.txt    # Untrack file
    ```

### Recovery

=== "Windows"
    ```powershell
    git reflog                  # Find lost commits
    git checkout -b recovery [hash]  # Restore commit
    git fsck --lost-found       # Find dangling objects
    ```

=== "macOS"
    ```bash
    git reflog                  # Find lost commits
    git checkout -b recovery [hash]  # Restore commit
    git fsck --lost-found       # Find dangling objects
    ```

=== "Linux"
    ```bash
    git reflog                  # Find lost commits
    git checkout -b recovery [hash]  # Restore commit
    git fsck --lost-found       # Find dangling objects
    ```

### Reset to Remote

=== "Windows"
    ```powershell
    git fetch origin
    git reset --hard origin/main
    git clean -fd
    ```

=== "macOS"
    ```bash
    git fetch origin
    git reset --hard origin/main
    git clean -fd
    ```

=== "Linux"
    ```bash
    git fetch origin
    git reset --hard origin/main
    git clean -fd
    ```

## Glossary

**Branch** - Independent development line  
**Clone** - Local copy of repository  
**Commit** - Saved snapshot of changes  
**Conflict** - Competing changes requiring resolution  
**Fork** - Personal copy of another's repository  
**HEAD** - Pointer to current commit  
**Merge** - Combine branches  
**Origin** - Default remote name  
**Pull** - Fetch and merge remote changes  
**Push** - Upload commits to remote  
**PR** - Pull Request for code review  
**Rebase** - Reapply commits on new base  
**Remote** - Repository on server  
**Repository** - Project with version history  
**Stage** - Mark changes for commit  
**Stash** - Temporary storage for changes  

---
**Keyboard Shortcuts**: VS Code (`Ctrl+Shift+G` Git panel), Terminal (`Ctrl+R` search history)