"""Command-line interface for RedHunter."""

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
