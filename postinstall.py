#!/usr/bin/env python
"""Post-installation setup script for RedHunter."""

import os
import sys
import shutil
from pathlib import Path


def setup_environment():
    """Set up the RedHunter environment after installation."""
    print("\n" + "="*60)
    print("  RED HUNTER - Environment Setup")
    print("="*60 + "\n")
    
    # Get user's home directory
    home = Path.home()
    redhunter_dir = home / ".redhunter"
    wordlists_dir = redhunter_dir / "wordlists"
    
    # Create directories
    print("[*] Creating directories...")
    redhunter_dir.mkdir(parents=True, exist_ok=True)
    wordlists_dir.mkdir(parents=True, exist_ok=True)
    print(f"[+] Created: {redhunter_dir}")
    
    # Create config file
    config_content = """# RedHunter Configuration File
[paths]
wordlists_directory = ~/.redhunter/wordlists

[algorithms]
supported = md5, sha1, sha256

[defaults]
wordlist = /usr/share/wordlists/rockyou.txt
algorithm = md5
"""
    config_file = redhunter_dir / "config.txt"
    if not config_file.exists():
        with open(config_file, 'w') as f:
            f.write(config_content)
        print(f"[+] Created config: {config_file}")
    
    print("\n[+] Environment setup complete!")
    print(f"[*] Wordlist directory: {wordlists_dir}")
    print("[*] Next steps:")
    print("    1. Download wordlists: redhunter download")
    print("    2. Crack hashes: redhunter crack -h <hash> -a md5")
    print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    try:
        setup_environment()
    except Exception as e:
        print(f"[-] Error during setup: {e}", file=sys.stderr)
        sys.exit(1)
