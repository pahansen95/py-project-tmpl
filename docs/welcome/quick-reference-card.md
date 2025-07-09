# Git Workflow Quick Reference Card

## Daily Workflow

### Start Work

=== "Windows"
    ```powershell
    git checkout main; git pull
    git checkout -b feature/task-name
    ```

=== "macOS"
    ```bash
    git checkout main && git pull
    git checkout -b feature/task-name
    ```

=== "Linux"
    ```bash
    git checkout main && git pull
    git checkout -b feature/task-name
    ```

### Make Changes & Commit

=== "Windows"
    ```powershell
    git add -A
    git commit -m "type: description"
    ```

=== "macOS"
    ```bash
    git add -A
    git commit -m "type: description"
    ```

=== "Linux"
    ```bash
    git add -A
    git commit -m "type: description"
    ```

### Share Work

=== "Windows"
    ```powershell
    git push -u origin feature/task-name
    gh pr create --title "Title" --body "Description"
    ```

=== "macOS"
    ```bash
    git push -u origin feature/task-name
    gh pr create --title "Title" --body "Description"
    ```

=== "Linux"
    ```bash
    git push -u origin feature/task-name
    gh pr create --title "Title" --body "Description"
    ```

## Essential Commands

### Setup

#### Clone Repository

=== "Windows"
    ```powershell
    git clone https://github.com/pahansen95/py-project-tmpl.git
    cd py-project-tmpl
    ```

=== "macOS"
    ```bash
    git clone https://github.com/pahansen95/py-project-tmpl.git
    cd py-project-tmpl
    ```

=== "Linux"
    ```bash
    git clone https://github.com/pahansen95/py-project-tmpl.git
    cd py-project-tmpl
    ```

#### Create & Activate Environment

=== "Windows"
    ```powershell
    uv venv
    .venv\Scripts\activate
    ```

=== "macOS"
    ```bash
    uv venv
    source .venv/bin/activate
    ```

=== "Linux"
    ```bash
    uv venv
    source .venv/bin/activate
    ```

#### Install Dependencies

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

### Branch Management

=== "Windows"
    ```powershell
    git branch -v                    # List branches
    git checkout -b new-branch       # Create & switch
    git checkout main               # Switch to main
    git branch -d old-branch        # Delete local
    git push origin --delete branch # Delete remote
    ```

=== "macOS"
    ```bash
    git branch -v                    # List branches
    git checkout -b new-branch       # Create & switch
    git checkout main               # Switch to main
    git branch -d old-branch        # Delete local
    git push origin --delete branch # Delete remote
    ```

=== "Linux"
    ```bash
    git branch -v                    # List branches
    git checkout -b new-branch       # Create & switch
    git checkout main               # Switch to main
    git branch -d old-branch        # Delete local
    git push origin --delete branch # Delete remote
    ```

### Common Fixes

#### Wrong Branch

=== "Windows"
    ```powershell
    git stash; git checkout correct-branch; git stash pop
    ```

=== "macOS"
    ```bash
    git stash && git checkout correct-branch && git stash pop
    ```

=== "Linux"
    ```bash
    git stash && git checkout correct-branch && git stash pop
    ```

#### Undo Last Commit

=== "Windows"
    ```powershell
    git reset --soft HEAD~1
    ```

=== "macOS"
    ```bash
    git reset --soft HEAD~1
    ```

=== "Linux"
    ```bash
    git reset --soft HEAD~1
    ```

#### Resolve Conflicts

=== "Windows"
    ```powershell
    git pull origin main
    # Edit files, remove <<<, ===, >>>
    git add .; git commit -m "Resolve conflicts"
    ```

=== "macOS"
    ```bash
    git pull origin main
    # Edit files, remove <<<, ===, >>>
    git add . && git commit -m "Resolve conflicts"
    ```

=== "Linux"
    ```bash
    git pull origin main
    # Edit files, remove <<<, ===, >>>
    git add . && git commit -m "Resolve conflicts"
    ```

#### Update Rejected Push

=== "Windows"
    ```powershell
    git pull --rebase origin main; git push
    ```

=== "macOS"
    ```bash
    git pull --rebase origin main && git push
    ```

=== "Linux"
    ```bash
    git pull --rebase origin main && git push
    ```

### Validation Commands

=== "Windows"
    ```powershell
    git status              # Check state
    git diff               # Review changes
    git log --oneline -5   # Recent commits
    pytest                 # Run tests
    ruff check .           # Check code
    ```

=== "macOS"
    ```bash
    git status              # Check state
    git diff               # Review changes
    git log --oneline -5   # Recent commits
    pytest                 # Run tests
    ruff check .           # Check code
    ```

=== "Linux"
    ```bash
    git status              # Check state
    git diff               # Review changes
    git log --oneline -5   # Recent commits
    pytest                 # Run tests
    ruff check .           # Check code
    ```

## Commit Types
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation
- `refactor:` Code restructuring
- `test:` Testing
- `chore:` Maintenance

## Time Estimates
- Clone & setup: 5 min
- Feature branch: 30 sec
- Commit cycle: 2 min
- Push & PR: 2 min
- Conflict resolution: 5-15 min

---
Print double-sided and keep at desk for quick reference.