"""Password cracking module for RedHunter."""

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
