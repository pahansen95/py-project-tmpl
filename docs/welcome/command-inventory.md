# Command Inventory for Platform-Specific Documentation

This inventory catalogs all command blocks found in the `/docs/welcome/` directory and identifies which ones need platform-specific variations.

## Summary of Files Analyzed

1. **index.md** - Main welcome page with fast track setup
2. **setup.md** - Detailed environment setup instructions
3. **workflow.md** - Development workflow guide
4. **reference.md** - Command reference tables
5. **quick-reference-card.md** - Printable quick reference
6. **setup-welcome.sh** - Bash setup script (macOS/Linux)
7. **setup-welcome.ps1** - PowerShell setup script (Windows)

## Command Categories

### 1. Shell Commands (Platform-Specific)

#### Virtual Environment Activation
**Location**: Multiple files
**Current Commands**:
- Linux/macOS: `source .venv/bin/activate`
- Windows: `.venv\Scripts\activate`

**Files Containing**:
- setup.md (lines 66-67)
- index.md (lines 44-45)
- workflow.md (implied but not shown)
- quick-reference-card.md (line 24)
- setup-welcome.sh (line 249)
- setup-welcome.ps1 (line 283)

#### Script Execution
**Location**: setup.md
**Current Commands**:
- Windows: `irm https://raw.githubusercontent.com/pahansen95/py-project-tmpl/main/scripts/setup-welcome.ps1 | iex`
- macOS/Linux: `curl -sSL https://raw.githubusercontent.com/pahansen95/py-project-tmpl/main/scripts/setup-welcome.sh | bash`

### 2. Path References (Platform-Specific)

#### Home Directory References
**Location**: setup-welcome scripts
**Current Usage**:
- Linux/macOS: `$HOME/.venv.d/`, `$HOME/.cache/`, `~/.ssh/`
- Windows: `$env:USERPROFILE\.venv.d\`, `$env:USERPROFILE\.cache\`

**Files Containing**:
- setup-welcome.sh (lines 229-230)
- setup-welcome.ps1 (lines 193-194)
- reference.md (line 55 - SSH key path)

#### UV Installation Path
**Location**: setup-welcome scripts
**Current Usage**:
- Linux/macOS: `$HOME/.cargo/bin`
- Windows: `$env:USERPROFILE\.cargo\bin`

### 3. Package Managers (Platform-Specific)

#### System Package Managers
**Location**: setup.md, setup-welcome scripts
**Commands by Platform**:
- Windows: `winget install [package]`
- macOS: `brew install [package]`
- Linux (Debian): `apt install [package]`
- Linux (RedHat): `dnf install [package]`
- Linux (Arch): `pacman -S [package]`

**Files Containing**:
- setup.md (lines 42-45)
- setup-welcome.sh (lines 103-116)
- setup-welcome.ps1 (lines 103-107, 121-125)

#### UV Installation Commands
**Location**: setup.md, index.md
**Platform Variations**:
- Windows: `irm https://astral.sh/uv/install.ps1 | iex`
- macOS/Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`

### 4. Directory Separators (Platform-Specific)

**Location**: Throughout documentation
**Current Usage**:
- Most paths use forward slashes (/)
- Windows-specific commands use backslashes (\)

**Files Needing Attention**:
- All command examples with file paths
- Virtual environment activation paths

### 5. Admin Privileges (Platform-Specific)

#### Privilege Elevation
**Location**: setup-welcome scripts
**Commands**:
- Linux/macOS: `sudo` prefix
- Windows: `#Requires -RunAsAdministrator` (PowerShell)

**Files Containing**:
- setup-welcome.sh (lines 78-87)
- setup-welcome.ps1 (line 1)

### 6. Git Configuration (Platform-Specific)

#### Line Ending Configuration
**Location**: Multiple files
**Commands**:
- Windows: `git config --global core.autocrlf true`
- macOS/Linux: `git config --global core.autocrlf input`

**Files Containing**:
- setup.md (lines 52-53)
- reference.md (lines 105-106)
- setup-welcome.sh (line 219)
- setup-welcome.ps1 (line 183)

## Universal Commands (No Platform Variation Needed)

### Git Commands
All git commands are universal across platforms:
- `git clone [url]`
- `git checkout -b [branch]`
- `git add .`
- `git commit -m "[message]"`
- `git push`
- `git pull`
- `git status`
- `git log`
- `git diff`
- `git branch`
- `git merge`
- `git rebase`
- `git reset`
- `git stash`

### Python/UV Commands
Once UV is installed, these commands are universal:
- `uv venv`
- `uv pip install [package]`
- `uv pip list`
- `uv --version`

### Python Commands
- `python --version`
- `pytest`
- `ruff format .`
- `ruff check .`

## Recommendations for Platform-Specific Documentation

### 1. Commands Requiring Immediate Platform Variants

1. **Virtual Environment Activation** - Critical for all workflows
2. **UV Installation** - Required for setup
3. **Package Manager Commands** - Needed for tool installation
4. **Path Separators** - Important for clarity
5. **Home Directory References** - Used in configuration

### 2. Documentation Structure Suggestions

1. Use tabs or collapsible sections for platform variants
2. Default to the most common platform (likely macOS/Linux)
3. Clearly mark Windows-specific variations
4. Consider a platform detection script for automated selection

### 3. Files Requiring Updates

Priority files for platform-specific updates:
1. **setup.md** - Most comprehensive setup instructions
2. **index.md** - First file new users see
3. **quick-reference-card.md** - Quick lookup reference
4. **workflow.md** - Daily development tasks

### 4. Command Block Format Recommendation

```markdown
<!-- Universal command -->
```bash
git status
```

<!-- Platform-specific command -->
```bash
# macOS/Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

<!-- Or using tabs -->
=== "macOS/Linux"
    ```bash
    source .venv/bin/activate
    ```

=== "Windows"
    ```powershell
    .venv\Scripts\activate
    ```
```

## Next Steps

1. Update all virtual environment activation commands
2. Add platform tabs to setup.md
3. Create platform detection snippet for documentation
4. Update quick reference card with platform variants
5. Test all commands on each platform
6. Add platform indicators to command blocks