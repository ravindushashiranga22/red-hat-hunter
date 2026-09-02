"""Wordlist management module for RedHunter."""

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
