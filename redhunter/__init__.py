"""RedHunter - Advanced Password Cracking Tool."""

import os
from pathlib import Path

__version__ = "1.0.0"
__author__ = "RedHunter"
__description__ = "Advanced password cracking and wordlist management tool"

# Auto-initialize environment on first import
def _setup_environment():
    """Automatically set up the environment on first import."""
    try:
        home = Path.home()
        redhunter_dir = home / ".redhunter"
        wordlists_dir = redhunter_dir / "wordlists"
        
        # Create directories if they don't exist
        redhunter_dir.mkdir(parents=True, exist_ok=True)
        wordlists_dir.mkdir(parents=True, exist_ok=True)
    except Exception:
        pass  # Silently fail if we can't create directories

_setup_environment()
