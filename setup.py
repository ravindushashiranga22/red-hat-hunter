from setuptools import setup, find_packages

setup(
    name="redhunter",
    version="1.0.0",
    description="A password cracking and wordlist tool",
    author="RedHunter",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "redhunter=redhunter.cli:main",
        ],
    },
    install_requires=[
        "click",
        "requests",
    ],
    python_requires=">=3.8",
)
