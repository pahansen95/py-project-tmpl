# Environment Setup

<div class="progress-tree">
<ul>
  <li class="completed">
    <span class="icon">✓</span>
    <span class="step-name">Overview</span>
    <span class="time">(10 min)</span>
  </li>
  <li class="current">
    <span class="icon">▶</span>
    <span class="step-name">Setup</span>
    <span class="time">(15 min)</span>
  </li>
  <li class="upcoming">
    <span class="icon">○</span>
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

## Objectives
- Install Git, Python, and UV package manager
- Configure development environment
- Verify all tools function correctly

## Prerequisites
| Component | Requirement | Verification |
|-----------|-------------|--------------|
| OS | Windows 10+, macOS 10.15+, Linux | See [System Verification](#system-verification) |
| Access | Administrator/sudo | Required |
| Storage | 4GB free | See [Disk Space Check](#disk-space-check) |
| Internet | Stable connection | 500MB download |

## Automated Setup (5 minutes)

=== "Windows"
    ```powershell
    # PowerShell as Administrator
    Set-ExecutionPolicy Bypass -Scope Process -Force
    irm https://raw.githubusercontent.com/pahansen95/py-project-tmpl/main/scripts/setup-welcome.ps1 | iex
    ```

=== "macOS"
    ```bash
    curl -sSL https://raw.githubusercontent.com/pahansen95/py-project-tmpl/main/scripts/setup-welcome.sh | bash
    ```

=== "Linux"
    ```bash
    curl -sSL https://raw.githubusercontent.com/pahansen95/py-project-tmpl/main/scripts/setup-welcome.sh | bash
    ```

**Script Actions**: Installs Git/Python/UV, configures environment, creates virtual environment, installs dependencies.

## Manual Setup (15 minutes)

### Install Required Tools

#### Git Installation

=== "Windows"
    ```powershell
    winget install Git.Git
    # Or download from https://git-scm.com/download/win
    ```

=== "macOS"
    ```bash
    brew install git
    # Or: xcode-select --install
    ```

=== "Linux"
    ```bash
    # Ubuntu/Debian
    sudo apt install git
    
    # Fedora
    sudo dnf install git
    
    # Arch
    sudo pacman -S git
    ```

#### Python Installation

=== "Windows"
    ```powershell
    winget install Python.Python.3.12
    # Or download from python.org
    ```

=== "macOS"
    ```bash
    brew install python@3.12
    ```

=== "Linux"
    ```bash
    # Ubuntu/Debian
    sudo apt install python3.12 python3.12-venv
    
    # Fedora
    sudo dnf install python3.12
    
    # Arch
    sudo pacman -S python
    ```

#### UV Package Manager

=== "Windows"
    ```powershell
    # PowerShell
    irm https://astral.sh/uv/install.ps1 | iex
    ```

=== "macOS"
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

=== "Linux"
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

### Configure Git

=== "Windows"
    ```powershell
    git config --global user.name "Your Name"
    git config --global user.email "your.email@example.com"
    git config --global init.defaultBranch main
    ```

=== "macOS"
    ```bash
    git config --global user.name "Your Name"
    git config --global user.email "your.email@example.com"
    git config --global init.defaultBranch main
    ```

=== "Linux"
    ```bash
    git config --global user.name "Your Name"
    git config --global user.email "your.email@example.com"
    git config --global init.defaultBranch main
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

### Project Setup

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

#### Activate Environment

=== "Windows"
    ```powershell
    # PowerShell
    .venv\Scripts\activate
    ```
    
    **Git Bash Alternative:**
    ```bash
    source .venv/Scripts/activate
    ```

=== "macOS"
    ```bash
    source .venv/bin/activate
    ```

=== "Linux"
    ```bash
    source .venv/bin/activate
    ```

#### Install Dependencies

=== "Windows"
    ```powershell
    uv pip install -e ".[dev,docs]"
    ```

=== "macOS"
    ```bash
    uv pip install -e ".[dev,docs]"
    ```

=== "Linux"
    ```bash
    uv pip install -e ".[dev,docs]"
    ```

## Validation Checkpoint

Execute validation sequence (2 minutes):

### System Validation

=== "Windows"
    ```powershell
    # Check all tools (30 seconds)
    Write-Host "=== Tool Versions ===" -ForegroundColor Cyan
    git --version
    python --version
    uv --version
    Write-Host "✓ All tools installed" -ForegroundColor Green
    ```

=== "macOS"
    ```bash
    # Check all tools (30 seconds)
    echo "=== Tool Versions ===" && \
    git --version && \
    python3 --version && \
    uv --version && \
    echo "✓ All tools installed"
    ```

=== "Linux"
    ```bash
    # Check all tools (30 seconds)
    echo "=== Tool Versions ===" && \
    git --version && \
    python3 --version && \
    uv --version && \
    echo "✓ All tools installed"
    ```

### Configuration Validation

=== "Windows"
    ```powershell
    # Check Git config (30 seconds)
    Write-Host "=== Git Configuration ===" -ForegroundColor Cyan
    Write-Host "Name: $(git config --global user.name)"
    Write-Host "Email: $(git config --global user.email)"
    Write-Host "Branch: $(git config --global init.defaultBranch)"
    Write-Host "✓ Git configured" -ForegroundColor Green
    ```

=== "macOS"
    ```bash
    # Check Git config (30 seconds)
    echo "=== Git Configuration ===" && \
    echo "Name: $(git config --global user.name)" && \
    echo "Email: $(git config --global user.email)" && \
    echo "Branch: $(git config --global init.defaultBranch)" && \
    echo "✓ Git configured"
    ```

=== "Linux"
    ```bash
    # Check Git config (30 seconds)
    echo "=== Git Configuration ===" && \
    echo "Name: $(git config --global user.name)" && \
    echo "Email: $(git config --global user.email)" && \
    echo "Branch: $(git config --global init.defaultBranch)" && \
    echo "✓ Git configured"
    ```

### Environment Validation

=== "Windows"
    ```powershell
    # Check Python environment (30 seconds)
    Write-Host "=== Python Environment ===" -ForegroundColor Cyan
    python -c "import sys; print(f'Python: {sys.executable}')"
    $venvActive = python -c "import sys; print('.venv' in sys.executable)"
    if ($venvActive -eq "True") {
        Write-Host "✓ Venv active" -ForegroundColor Green
    } else {
        Write-Host "✗ Venv NOT active" -ForegroundColor Red
    }
    $hasPytest = uv pip list | Select-String -Pattern "pytest" -Quiet
    if ($hasPytest) {
        Write-Host "✓ Dependencies installed" -ForegroundColor Green
    }
    ```

=== "macOS"
    ```bash
    # Check Python environment (30 seconds)
    echo "=== Python Environment ===" && \
    python3 -c "import sys; print(f'Python: {sys.executable}')" && \
    python3 -c "import sys; print('✓ Venv active' if '.venv' in sys.executable else '✗ Venv NOT active')" && \
    uv pip list | grep -q pytest && echo "✓ Dependencies installed"
    ```

=== "Linux"
    ```bash
    # Check Python environment (30 seconds)
    echo "=== Python Environment ===" && \
    python3 -c "import sys; print(f'Python: {sys.executable}')" && \
    python3 -c "import sys; print('✓ Venv active' if '.venv' in sys.executable else '✗ Venv NOT active')" && \
    uv pip list | grep -q pytest && echo "✓ Dependencies installed"
    ```

### Project Validation

=== "Windows"
    ```powershell
    # Final check (30 seconds)
    if (Test-Path "pyproject.toml") {
        Write-Host "✓ Project files found" -ForegroundColor Green
    }
    if (Test-Path ".git") {
        Write-Host "✓ Git repository initialized" -ForegroundColor Green
    }
    $hasRemote = git remote -v | Select-String -Pattern "origin" -Quiet
    if ($hasRemote) {
        Write-Host "✓ Remote configured" -ForegroundColor Green
    }
    ```

=== "macOS"
    ```bash
    # Final check (30 seconds)
    test -f pyproject.toml && echo "✓ Project files found" && \
    test -d .git && echo "✓ Git repository initialized" && \
    git remote -v | grep -q origin && echo "✓ Remote configured"
    ```

=== "Linux"
    ```bash
    # Final check (30 seconds)
    test -f pyproject.toml && echo "✓ Project files found" && \
    test -d .git && echo "✓ Git repository initialized" && \
    git remote -v | grep -q origin && echo "✓ Remote configured"
    ```

**Expected**: All validations show ✓ checkmarks

## Common Issues

| Issue | Solution | Time |
|-------|----------|------|
| `command not found` | Restart terminal or add to PATH | 2 min |
| `permission denied` | Run as Administrator/sudo | 1 min |
| `SSL certificate error` | Set proxy or update certificates | 5 min |
| `venv activation fails` | Windows: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` | 2 min |

---
**Next**: [Development Workflow](workflow.md) • **Time Investment**: 20 minutes

## Appendix: Verification Commands

### System Verification

=== "Windows"
    ```powershell
    # Display Windows version
    [System.Environment]::OSVersion.Version
    # Or for detailed info:
    Get-ComputerInfo | Select-Object WindowsVersion, WindowsBuildLabEx, OsArchitecture
    ```

=== "macOS"
    ```bash
    # Display macOS version
    sw_vers -productVersion
    # Or full system info:
    uname -a
    ```

=== "Linux"
    ```bash
    # Display Linux distribution info
    cat /etc/os-release
    # Or kernel info:
    uname -a
    ```

### Disk Space Check

=== "Windows"
    ```powershell
    # Check available disk space
    Get-PSDrive -PSProvider FileSystem | 
        Select-Object Name, @{Name="Free(GB)";Expression={[math]::Round($_.Free/1GB,2)}}, 
                            @{Name="Total(GB)";Expression={[math]::Round(($_.Used+$_.Free)/1GB,2)}}
    ```

=== "macOS"
    ```bash
    # Check available disk space
    df -h | grep -E "^/dev/"
    ```

=== "Linux"
    ```bash
    # Check available disk space
    df -h | grep -E "^/dev/"
    ```