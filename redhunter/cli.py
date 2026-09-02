"""Command-line interface for RedHunter."""

import os
import sys
import click
from redhunter.banner import print_banner, print_info, print_success, print_error, print_warning
from redhunter.wordlists import WordlistManager
from redhunter.cracker import PasswordCracker


def get_default_wordlist():
    """Get the default wordlist path based on OS."""
    # Try common locations
    common_paths = [
        "/usr/share/wordlists/rockyou.txt",  # Linux
        "/usr/share/dict/rockyou.txt",  # Some Linux variants
        "/usr/local/share/wordlists/rockyou.txt",
        os.path.expanduser("~/.redhunter/wordlists/rockyou.txt"),  # User wordlist dir
        os.path.expanduser("~/.redhunter/wordlists/common.txt"),
    ]
    
    for path in common_paths:
        if os.path.exists(path):
            return path
    
    # Return the preferred default even if it doesn't exist
    return "/usr/share/wordlists/rockyou.txt"


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """RedHunter - Advanced Password Cracking Tool."""
    if ctx.invoked_subcommand is None:
        print_banner()
        print()
        ctx.invoke(help)


@cli.command()
def download():
    """Download wordlists for cracking."""
    print_banner()
    print()
    print_info("Fetching wordlists from remote sources...")
    print()
    
    manager = WordlistManager()
    wordlists = {
        "rockyou.txt": "https://github.com/priyankacoumar/rockyou.txt/raw/main/rockyou.txt",
        "common.txt": "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10k-most-common.txt",
    }
    
    for filename, url in wordlists.items():
        print_info(f"Downloading {filename}...")
        if manager.download_wordlist(url, filename):
            print_success(f"{filename} downloaded successfully")
        else:
            print_error(f"Failed to download {filename}")
    
    print()
    print_info("Download complete!")


@cli.command()
@click.option("--hash", "-h", required=True, help="The hash to crack")
@click.option("--wordlist", "-w", default=None, help="Path to wordlist file (default: rockyou.txt)")
@click.option("--algorithm", "-a", default="md5", type=click.Choice(["md5", "sha1", "sha256"]), help="Hash algorithm")
def crack(hash, wordlist, algorithm):
    """Crack a password hash using a wordlist.
    
    Example:
        redhunter crack -h 5f4dcc3b5aa765d61d8327deb882cf99 -a md5
        redhunter crack -h 5f4dcc3b5aa765d61d8327deb882cf99 -w /path/to/wordlist.txt -a md5
    """
    print_banner()
    print()
    
    # Use default wordlist if not provided
    if not wordlist:
        wordlist = get_default_wordlist()
        print_info(f"Using default wordlist: {wordlist}")
    
    # Check if wordlist exists
    if not os.path.exists(wordlist):
        print_error(f"Wordlist not found: {wordlist}")
        print_info(f"Run 'redhunter download' to download wordlists")
        print()
        sys.exit(1)
    
    print_info(f"Starting attack...")
    print_info(f"Hash: {hash[:16]}... (Algorithm: {algorithm.upper()})")
    print_info(f"Wordlist: {wordlist}")
    print()
    
    cracker = PasswordCracker()
    password = cracker.crack_password(hash, wordlist, algorithm)
    
    print()
    if password:
        print_success(f"Password found: {password}")
    else:
        print_error(f"Password not found in wordlist")


@cli.command()
def list_wordlists():
    """List all available wordlists."""
    print_banner()
    print()
    manager = WordlistManager()
    wordlists = manager.list_wordlists()
    
    if wordlists:
        print_info("Available wordlists:")
        for i, wl in enumerate(wordlists, 1):
            size = os.path.getsize(os.path.join(manager.wordlists_dir, wl)) / (1024*1024)
            print(f"  {i}. {wl} ({size:.2f} MB)")
    else:
        print_warning("No wordlists found.")
        print_info("Run 'redhunter download' to download wordlists")
    
    print()
    print_info(f"Default wordlist location: {get_default_wordlist()}")


def main():
    """Main entry point."""
    cli()


if __name__ == "__main__":
    main()
