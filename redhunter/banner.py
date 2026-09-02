"""Banner and display utilities for RedHunter."""

import os


def print_banner():
    """Print the RedHunter banner with styled output."""
    banner = """
    ╔═══════════════════════════════════════════════════════╗
    ║                                                       ║
    ║          🔴  RED HUNTER v1.0.0  🔴                  ║
    ║                                                       ║
    ║         Advanced Password Cracking Tool              ║
    ║                                                       ║
    ║  JWT | Hash | Dictionary | Brute Force               ║
    ║                                                       ║
    ╚═══════════════════════════════════════════════════════╝
    """
    print(banner)


def print_info(message):
    """Print info message with styling."""
    print(f"[*] {message}")


def print_success(message):
    """Print success message with styling."""
    print(f"[+] {message}")


def print_error(message):
    """Print error message with styling."""
    print(f"[-] {message}")


def print_warning(message):
    """Print warning message with styling."""
    print(f"[!] {message}")
