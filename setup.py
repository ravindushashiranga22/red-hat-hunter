from setuptools import setup, find_packages
from pathlib import Path

# Read README with UTF-8 encoding
readme_path = Path(__file__).parent / "README.md"
try:
    long_description = readme_path.read_text(encoding='utf-8') if readme_path.exists() else ""
except UnicodeDecodeError:
    long_description = ""

setup(
    name="redhunter",
    version="1.0.0",
    description="Advanced password cracking and wordlist management tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="RedHunter",
    author_email="",
    url="https://github.com/ravindushashiranga22/red-hat-hunter",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "redhunter=redhunter.cli:main",
        ],
    },
    install_requires=[
        "click>=8.0.0",
        "requests>=2.25.0",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    keywords="password cracking hashing wordlist security",
    project_urls={
        "Bug Reports": "https://github.com/ravindushashiranga22/red-hat-hunter/issues",
        "Source": "https://github.com/ravindushashiranga22/red-hat-hunter",
    },
)
