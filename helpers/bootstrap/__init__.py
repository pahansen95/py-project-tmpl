"""Bootstrap module for layered environment setup."""

from __future__ import annotations

# Version of the bootstrap system
__version__ = "1.0.0"

# Layer definitions for reference
LAYERS = {
    0: "Foundation (OS, architecture, network)",
    1: "Prerequisites (shell, git, base Python)",
    2: "Managed Tools (uv, pyenv, Python)",
    3: "Project Environment (venv, dependencies)",  
    4: "Developer Experience (git hooks, IDE)"
}

# Export main entry point
from .orchestrator import main as orchestrate

__all__ = ["orchestrate", "LAYERS"]