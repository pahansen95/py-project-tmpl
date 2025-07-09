# Development Workflow

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
  <li class="current">
    <span class="icon">▶</span>
    <span class="step-name">Workflow</span>
    <span class="time">(20 min)</span>
  </li>
  <li class="upcoming">
    <span class="icon">○</span>
    <span class="step-name">Reference</span>
    <span class="time">(as needed)</span>
  </li>
</ul>
</div>

## On This Page
- [Daily Operations](#daily-operations) - 5 min
- [Branch Management](#branch-management) - 5 min  
- [Collaboration](#collaboration) - 5 min
- [Validation](#validation-checkpoints) - 5 min

## Objectives
- Execute standard Git workflow independently
- Create and manage feature branches
- Submit changes via pull request

## Prerequisites
| Requirement | Verification | Time |
|-------------|--------------|------|
| Environment configured | `.venv` activated | 0 min |
| Repository cloned | `git status` executes | 0 min |
| GitHub access | Repository visible online | 0 min |

## Daily Operations

### Start Work Session

=== "Windows"
    ```powershell
    git checkout main; git pull origin main; git checkout -b feature/task-name
    ```

=== "macOS/Linux"
    ```bash
    git checkout main && git pull origin main && git checkout -b feature/task-name
    ```

**Output**: `Switched to a new branch 'feature/task-name'`  
**Time**: 30 seconds

### Make Changes

#### Stage Changes

=== "Windows"
    ```powershell
    # Edit files with your preferred editor
    # Stage changes
    git add -A                    # All changes
    git add path/to/file.py      # Specific file
    ```

=== "macOS"
    ```bash
    # Edit files with your preferred editor
    # Stage changes
    git add -A                    # All changes
    git add path/to/file.py      # Specific file
    ```

=== "Linux"
    ```bash
    # Edit files with your preferred editor
    # Stage changes
    git add -A                    # All changes
    git add path/to/file.py      # Specific file
    ```

#### Review Staged Changes

=== "Windows"
    ```powershell
    git diff --staged
    ```

=== "macOS"
    ```bash
    git diff --staged
    ```

=== "Linux"
    ```bash
    git diff --staged
    ```

**Time**: Variable

### Commit Changes

=== "Windows"
    ```powershell
    git commit -m "type: Brief description"
    ```

=== "macOS"
    ```bash
    git commit -m "type: Brief description"
    ```

=== "Linux"
    ```bash
    git commit -m "type: Brief description"
    ```

**Types**: `feat` | `fix` | `docs` | `refactor` | `test` | `chore`  
**Time**: 1 minute

### Push to Remote

=== "Windows"
    ```powershell
    git push -u origin feature/task-name    # First push
    git push                                # Subsequent pushes
    ```

=== "macOS"
    ```bash
    git push -u origin feature/task-name    # First push
    git push                                # Subsequent pushes
    ```

=== "Linux"
    ```bash
    git push -u origin feature/task-name    # First push
    git push                                # Subsequent pushes
    ```

**Output**: URL for creating pull request  
**Time**: 30 seconds

## Branch Management

### Branch Operations

#### List Branches

=== "Windows"
    ```powershell
    # List branches
    git branch -v                    # Local branches
    git branch -r                    # Remote branches
    ```

=== "macOS"
    ```bash
    # List branches
    git branch -v                    # Local branches
    git branch -r                    # Remote branches
    ```

=== "Linux"
    ```bash
    # List branches
    git branch -v                    # Local branches
    git branch -r                    # Remote branches
    ```

#### Switch Branches

=== "Windows"
    ```powershell
    # Switch branches
    git checkout branch-name         # Existing branch
    git checkout -b new-branch       # Create and switch
    ```

=== "macOS"
    ```bash
    # Switch branches
    git checkout branch-name         # Existing branch
    git checkout -b new-branch       # Create and switch
    ```

=== "Linux"
    ```bash
    # Switch branches
    git checkout branch-name         # Existing branch
    git checkout -b new-branch       # Create and switch
    ```

#### Delete Branches

=== "Windows"
    ```powershell
    # Delete branches
    git branch -d merged-branch      # Safe delete
    git branch -D unmerged-branch    # Force delete
    git push origin --delete remote-branch
    ```

=== "macOS"
    ```bash
    # Delete branches
    git branch -d merged-branch      # Safe delete
    git branch -D unmerged-branch    # Force delete
    git push origin --delete remote-branch
    ```

=== "Linux"
    ```bash
    # Delete branches
    git branch -d merged-branch      # Safe delete
    git branch -D unmerged-branch    # Force delete
    git push origin --delete remote-branch
    ```

### Sync with Main

=== "Windows"
    ```powershell
    git checkout main; git pull
    git checkout feature/task-name
    git merge main                   # Or rebase: git rebase main
    ```

=== "macOS/Linux"
    ```bash
    git checkout main && git pull
    git checkout feature/task-name
    git merge main                   # Or rebase: git rebase main
    ```

**Time**: 2 minutes

## Collaboration

### Create Pull Request

**Command Line (GitHub CLI):**

=== "Windows"
    ```powershell
    gh pr create --title "Brief description" --body "Details"
    ```

=== "macOS"
    ```bash
    gh pr create --title "Brief description" --body "Details"
    ```

=== "Linux"
    ```bash
    gh pr create --title "Brief description" --body "Details"
    ```

**Manual Process:**
1. Push branch: `git push -u origin feature/task-name`
2. Visit URL in output
3. Click "Create pull request"
4. Fill template

### Address Review Feedback

=== "Windows"
    ```powershell
    # Make requested changes
    git add -A
    git commit -m "Address review: specific change"
    git push
    ```

=== "macOS"
    ```bash
    # Make requested changes
    git add -A
    git commit -m "Address review: specific change"
    git push
    ```

=== "Linux"
    ```bash
    # Make requested changes
    git add -A
    git commit -m "Address review: specific change"
    git push
    ```

### Resolve Conflicts

=== "Windows"
    ```powershell
    # Pull latest main
    git pull origin main
    
    # If conflicts occur:
    # 1. Open conflicted files
    # 2. Look for <<<<<<< markers
    # 3. Edit to resolve
    # 4. Remove all markers
    git add resolved-file.py
    git commit -m "Resolve merge conflicts"
    git push
    ```

=== "macOS"
    ```bash
    # Pull latest main
    git pull origin main
    
    # If conflicts occur:
    # 1. Open conflicted files
    # 2. Look for <<<<<<< markers
    # 3. Edit to resolve
    # 4. Remove all markers
    git add resolved-file.py
    git commit -m "Resolve merge conflicts"
    git push
    ```

=== "Linux"
    ```bash
    # Pull latest main
    git pull origin main
    
    # If conflicts occur:
    # 1. Open conflicted files
    # 2. Look for <<<<<<< markers
    # 3. Edit to resolve
    # 4. Remove all markers
    git add resolved-file.py
    git commit -m "Resolve merge conflicts"
    git push
    ```

**Time**: 5-15 minutes

### Post-Merge Cleanup

=== "Windows"
    ```powershell
    git checkout main
    git pull origin main
    git branch -d feature/task-name
    git remote prune origin
    ```

=== "macOS"
    ```bash
    git checkout main
    git pull origin main
    git branch -d feature/task-name
    git remote prune origin
    ```

=== "Linux"
    ```bash
    git checkout main
    git pull origin main
    git branch -d feature/task-name
    git remote prune origin
    ```

**Time**: 1 minute

## Validation Checkpoints

### Pre-Commit Checklist
- [ ] Correct branch: `git branch` shows feature branch
- [ ] Changes reviewed: `git diff` examined
- [ ] Tests pass: `pytest` succeeds
- [ ] Code quality: `ruff check .` passes
- [ ] No debug code: No print statements

### Pre-Push Verification
- [ ] Clean status: `git status` shows nothing to commit
- [ ] Commits logical: `git log --oneline -5` reviewed
- [ ] Branch current: `git pull origin main` completed

### PR Readiness
- [ ] Title descriptive: Starts with verb (Add, Fix, Update)
- [ ] Description complete: What/Why/How included
- [ ] Tests included: New tests for new code
- [ ] Documentation updated: If applicable
- [ ] CI passing: All checks green

## Common Errors

| Error | Command | Time |
|-------|---------|------|
| `divergent branches` | `git pull --rebase origin main` | 2 min |
| `nothing to commit` | `git status --porcelain` | 10 sec |
| `rejected push` | `git pull origin main` then push | 2 min |
| `detached HEAD` | `git checkout main` | 30 sec |

## Command Workflows

### Bug Fix Pattern

=== "Windows"
    ```powershell
    git checkout main; git pull
    git checkout -b fix/issue-description
    # Fix bug
    git add -A; git commit -m "fix: Resolve issue"
    git push -u origin fix/issue-description
    gh pr create --label "bug"
    ```

=== "macOS/Linux"
    ```bash
    git checkout main && git pull
    git checkout -b fix/issue-description
    # Fix bug
    git add -A && git commit -m "fix: Resolve issue"
    git push -u origin fix/issue-description
    gh pr create --label "bug"
    ```

### Feature Pattern

=== "Windows"
    ```powershell
    git checkout main; git pull
    git checkout -b feature/new-capability
    # Implement feature
    git add -A; git commit -m "feat: Add capability"
    # Additional commits as needed
    git push -u origin feature/new-capability
    gh pr create --label "enhancement"
    ```

=== "macOS/Linux"
    ```bash
    git checkout main && git pull
    git checkout -b feature/new-capability
    # Implement feature
    git add -A && git commit -m "feat: Add capability"
    # Additional commits as needed
    git push -u origin feature/new-capability
    gh pr create --label "enhancement"
    ```

### Documentation Pattern

=== "Windows"
    ```powershell
    git checkout -b docs/update-section
    # Update docs
    git add -A; git commit -m "docs: Update section"
    git push -u origin docs/update-section
    gh pr create --label "documentation"
    ```

=== "macOS/Linux"
    ```bash
    git checkout -b docs/update-section
    # Update docs
    git add -A && git commit -m "docs: Update section"
    git push -u origin docs/update-section
    gh pr create --label "documentation"
    ```

## Workflow Validation Summary

### Before Starting Work

=== "Windows"
    ```powershell
    git fetch --all; git status
    ```

=== "macOS/Linux"
    ```bash
    git fetch --all && git status
    ```

**Expected**: "Your branch is up to date", no uncommitted changes

### Before Committing

=== "Windows"
    ```powershell
    pytest; if ($LASTEXITCODE -eq 0) { ruff check . }; git diff
    ```

=== "macOS/Linux"
    ```bash
    pytest && ruff check . && git diff
    ```

**Expected**: All tests pass, no linting errors, changes reviewed

### Before Creating PR

=== "Windows"
    ```powershell
    git log origin/main..HEAD --oneline; git status --porcelain
    ```

=== "macOS/Linux"
    ```bash
    git log origin/main..HEAD --oneline && git status --porcelain
    ```

**Expected**: Commits listed, no uncommitted changes

### Health Check Script

=== "Windows"
    ```powershell
    # Save as check-health.ps1
    Write-Host "=== Git Health Check ==="
    
    # Check working directory
    if (!(git status --porcelain)) {
        Write-Host "✓ Clean working directory" -ForegroundColor Green
    } else {
        Write-Host "✗ Uncommitted changes" -ForegroundColor Red
    }
    
    # Check branch
    $branch = git rev-parse --abbrev-ref HEAD
    if ($branch -ne "main") {
        Write-Host "✓ On feature branch: $branch" -ForegroundColor Green
    } else {
        Write-Host "✗ On main branch" -ForegroundColor Red
    }
    
    # Run tests
    $testResult = pytest --quiet 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✓ Tests pass" -ForegroundColor Green
    } else {
        Write-Host "✗ Tests fail" -ForegroundColor Red
    }
    
    # Check code quality
    $ruffResult = ruff check . --quiet 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✓ Code quality good" -ForegroundColor Green
    } else {
        Write-Host "✗ Code issues found" -ForegroundColor Red
    }
    ```

=== "macOS/Linux"
    ```bash
    # Save as check-health.sh
    #!/bin/bash
    echo "=== Git Health Check ==="
    git status --porcelain && echo "✓ Clean working directory" || echo "✗ Uncommitted changes"
    git rev-parse --abbrev-ref HEAD | grep -v main && echo "✓ On feature branch" || echo "✗ On main branch"
    pytest --quiet && echo "✓ Tests pass" || echo "✗ Tests fail"
    ruff check . --quiet && echo "✓ Code quality good" || echo "✗ Code issues found"
    echo "=== Ready to commit: $([ $? -eq 0 ] && echo "YES" || echo "NO") ==="
    ```

---
**Next**: [Quick Reference](reference.md) • **Time Investment**: As needed