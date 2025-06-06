"""Bootstrap module for layered environment setup.

This module can be executed as:
  python -m helpers.bootstrap
"""

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

# Export key functions for programmatic use
from .orchestrator import main as orchestrate, run_layer

__all__ = ["orchestrate", "run_layer", "LAYERS", "__version__"]