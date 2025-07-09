# Python Project Template Documentation

<div class="progress-tree">
<ul>
  <li class="current">
    <span class="icon">▶</span>
    <span class="step-name">Overview</span>
    <span class="time">(10 min)</span>
  </li>
  <li class="upcoming">
    <span class="icon">○</span>
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
- Execute complete development workflow within 45 minutes
- Configure Python development environment
- Submit code changes via pull request

## Prerequisites

| Requirement | Minimum Version | Verification |
|-------------|----------------|--------------|
| Operating System | Windows 10+, macOS 10.15+, Linux | See [System Check](#system-check) |
| Disk Space | 4GB free | See [Disk Check](#disk-check) |
| Internet | Stable connection | Download ~500MB |
| Access Rights | Administrator/sudo | Required for installation |

## Fast Track (5 minutes)

### Prerequisites Check (30 seconds)

=== "Windows"
    ```powershell
    git --version       # Required: 2.30+
    python --version    # Required: 3.10+
    ```

=== "macOS"
    ```bash
    git --version       # Required: 2.30+
    python3 --version   # Required: 3.10+
    ```

=== "Linux"
    ```bash
    git --version       # Required: 2.30+
    python3 --version   # Required: 3.10+
    ```

### Environment Setup (2 minutes)

#### Clone Repository

=== "Windows"
    ```powershell
    git clone https://github.com/pahansen95/py-project-tmpl.git; cd py-project-tmpl
    ```

=== "macOS"
    ```bash
    git clone https://github.com/pahansen95/py-project-tmpl.git && cd py-project-tmpl
    ```

=== "Linux"
    ```bash
    git clone https://github.com/pahansen95/py-project-tmpl.git && cd py-project-tmpl
    ```

#### Configure Git Identity

=== "Windows"
    ```powershell
    git config --global user.name "Your Name"
    git config --global user.email "your.email@example.com"
    ```

=== "macOS"
    ```bash
    git config --global user.name "Your Name"
    git config --global user.email "your.email@example.com"
    ```

=== "Linux"
    ```bash
    git config --global user.name "Your Name"
    git config --global user.email "your.email@example.com"
    ```

#### Install UV Package Manager

=== "Windows"
    ```powershell
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

#### Create Python Environment

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

### Submit Changes (2.5 minutes)

#### Create Feature Branch

=== "Windows"
    ```powershell
    git checkout -b feature/your-change
    ```

=== "macOS"
    ```bash
    git checkout -b feature/your-change
    ```

=== "Linux"
    ```bash
    git checkout -b feature/your-change
    ```

#### Make Changes

=== "Windows"
    ```powershell
    echo "# Your change" >> README.md
    ```

=== "macOS"
    ```bash
    echo "# Your change" >> README.md
    ```

=== "Linux"
    ```bash
    echo "# Your change" >> README.md
    ```

#### Commit and Push

=== "Windows"
    ```powershell
    git add README.md
    git commit -m "feat: Add your change"
    git push -u origin feature/your-change
    ```

=== "macOS"
    ```bash
    git add README.md
    git commit -m "feat: Add your change"
    git push -u origin feature/your-change
    ```

=== "Linux"
    ```bash
    git add README.md
    git commit -m "feat: Add your change"
    git push -u origin feature/your-change
    ```

**Output**: URL for creating pull request

## Navigation

| Section | Purpose | Time Investment |
|---------|---------|-----------------|
| [Setup](setup.md) | Detailed environment configuration | 15 minutes |
| [Workflow](workflow.md) | Complete development process | 20 minutes |
| [Reference](reference.md) | Commands and troubleshooting | As needed |

## System Requirements

### Supported Platforms
- **Windows**: 10/11 (64-bit), PowerShell 5.1+
- **macOS**: 10.15+ (Catalina or later)
- **Linux**: Ubuntu 20.04+, Debian 11+, Fedora 34+, RHEL 8+

### Required Tools
| Tool | Purpose | Installation Check |
|------|---------|-------------------|
| Git 2.30+ | Version control | See validation commands below |
| Python 3.10+ | Programming language | See validation commands below |
| UV 0.4+ | Package manager | See validation commands below |

## Validation Checkpoint

Execute validation sequence:

=== "Windows"
    ```powershell
    git --version; python --version; uv --version
    ```

=== "macOS"
    ```bash
    git --version && python3 --version && uv --version
    ```

=== "Linux"
    ```bash
    git --version && python3 --version && uv --version
    ```

**Expected**: All commands return version numbers  
**Time**: 30 seconds

## Common Errors

| Error | Solution | Time |
|-------|----------|------|
| `command not found` | Restart terminal or check PATH | 2 min |
| `permission denied` | Use sudo/admin privileges | 1 min |
| `SSL certificate error` | Configure proxy or update certs | 5 min |

---
**Next**: [Environment Setup](setup.md) • **Time Investment**: 15 minutes

## Appendix: System Verification Commands

### System Check

=== "Windows"
    ```powershell
    # Display Windows version
    [System.Environment]::OSVersion.Version
    # Or use:
    winver
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

### Disk Check

=== "Windows"
    ```powershell
    # Check available disk space
    Get-PSDrive -PSProvider FileSystem | Select-Object Name, @{Name="Free(GB)";Expression={[math]::Round($_.Free/1GB,2)}}
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