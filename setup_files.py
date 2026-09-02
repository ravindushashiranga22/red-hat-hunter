#!/usr/bin/env python
"""Setup script to create all module files."""

import os

files_content = {
    'redhunter/__init__.py': '"""RedHunter - A password cracking and wordlist tool."""\n\n__version__ = "1.0.0"\n__author__ = "RedHunter"\n',
    
    'redhunter/__main__.py': '"""Entry point for running redhunter as a module."""\n\nfrom redhunter.cli import main\n\nif __name__ == "__main__":\n    main()\n',
    
    'redhunter/banner.py': '''"""Banner and display utilities for RedHunter."""


def print_banner():
    """Print the RedHunter banner."""
    banner = """
    ╔═══════════════════════════════════╗
    ║       RED HUNTER v1.0.0          ║
    ║   Password Cracking Tool          ║
    ╚═══════════════════════════════════╝
    """
    print(banner)
''',
    
    'redhunter/wordlists.py': '''"""Wordlist management module for RedHunter."""

import os
import requests


class WordlistManager:
    """Manages wordlists for password cracking."""

    def __init__(self):
        """Initialize the wordlist manager."""
        self.wordlists_dir = os.path.join(os.path.expanduser("~"), ".redhunter", "wordlists")
        os.makedirs(self.wordlists_dir, exist_ok=True)

    def download_wordlist(self, url, filename):
        """Download a wordlist from a URL."""
        try:
            filepath = os.path.join(self.wordlists_dir, filename)
            response = requests.get(url, stream=True)
            response.raise_for_status()

            with open(filepath, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            return True
        except Exception as e:
            print(f"Error downloading wordlist: {e}")
            return False

    def list_wordlists(self):
        """List all available wordlists."""
        if os.path.exists(self.wordlists_dir):
            return os.listdir(self.wordlists_dir)
        return []
''',
    
    'redhunter/cracker.py': '''"""Password cracking module for RedHunter."""

import hashlib


class PasswordCracker:
    """Handles password cracking operations."""

    def __init__(self):
        """Initialize the password cracker."""
        self.algorithms = ["md5", "sha1", "sha256"]

    def hash_password(self, password, algorithm="md5"):
        """Hash a password using the specified algorithm."""
        if algorithm not in self.algorithms:
            raise ValueError(f"Unsupported algorithm: {algorithm}")

        if algorithm == "md5":
            return hashlib.md5(password.encode()).hexdigest()
        elif algorithm == "sha1":
            return hashlib.sha1(password.encode()).hexdigest()
        elif algorithm == "sha256":
            return hashlib.sha256(password.encode()).hexdigest()

    def crack_password(self, hash_value, wordlist_path, algorithm="md5"):
        """Attempt to crack a password hash using a wordlist."""
        try:
            with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
                for password in f:
                    password = password.strip()
                    if self.hash_password(password, algorithm) == hash_value:
                        return password
        except FileNotFoundError:
            print(f"Wordlist file not found: {wordlist_path}")
        return None
''',
    
    'redhunter/cli.py': '''"""Command-line interface for RedHunter."""

import click
from redhunter.banner import print_banner
from redhunter.wordlists import WordlistManager
from redhunter.cracker import PasswordCracker


@click.group()
def cli():
    """RedHunter - Password Cracking Tool."""
    pass


@cli.command()
def download():
    """Download default wordlists."""
    print_banner()
    click.echo("Downloading wordlists...")
    
    manager = WordlistManager()
    wordlists = {
        "common.txt": "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100.txt",
    }
    
    for filename, url in wordlists.items():
        click.echo(f"Downloading {filename}...")
        if manager.download_wordlist(url, filename):
            click.echo(f"✓ {filename} downloaded successfully")
        else:
            click.echo(f"✗ Failed to download {filename}")


@cli.command()
@click.option("--hash", prompt="Enter the hash to crack", help="The hash value to crack")
@click.option("--wordlist", prompt="Enter the wordlist path", help="Path to the wordlist file")
@click.option("--algorithm", default="md5", help="Hash algorithm (md5, sha1, sha256)")
def crack(hash, wordlist, algorithm):
    """Crack a password hash."""
    print_banner()
    click.echo(f"Attempting to crack hash: {hash[:16]}...")
    
    cracker = PasswordCracker()
    password = cracker.crack_password(hash, wordlist, algorithm)
    
    if password:
        click.echo(f"✓ Password found: {password}")
    else:
        click.echo("✗ Password not found in wordlist")


@cli.command()
def list_wordlists():
    """List available wordlists."""
    print_banner()
    manager = WordlistManager()
    wordlists = manager.list_wordlists()
    
    if wordlists:
        click.echo("Available wordlists:")
        for wl in wordlists:
            click.echo(f"  - {wl}")
    else:
        click.echo("No wordlists found. Run 'redhunter download' to get started.")


def main():
    """Main entry point."""
    cli()


if __name__ == "__main__":
    main()
'''
}

for filepath, content in files_content.items():
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"✓ Created {filepath}")

print("\n✓ All Python files created successfully!")
