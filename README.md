# 🔴 RED HUNTER v1.0.0

**Advanced Password Cracking Tool** - Like jwt_tool but for hash cracking with dictionary attacks

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🚀 Quick Start

### Installation from GitHub

```bash
# Clone the repository
git clone https://github.com/ravindushashiranga22/red-hat-hunter.git
cd red-hat-hunter

# Install the package
pip install -e .

# Run post-install setup (auto-creates environment)
python postinstall.py

# Download wordlists
redhunter download
```

### Docker Installation (Optional)
```bash
docker build -t redhunter .
docker run -it redhunter redhunter --help
```

---

## 📖 Usage

### Show Banner & Help
```bash
redhunter
redhunter --help
```

### Crack MD5 Hash (with default wordlist)
```bash
redhunter crack -h 5f4dcc3b5aa765d61d8327deb882cf99 -a md5
```

### Crack with Custom Wordlist
```bash
redhunter crack -h 5f4dcc3b5aa765d61d8327deb882cf99 \
                -w /usr/share/wordlists/rockyou.txt \
                -a md5
```

### Crack SHA1 Hash
```bash
redhunter crack -h aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d \
                -a sha1
```

### Download Wordlists
```bash
redhunter download
```

### List Available Wordlists
```bash
redhunter list-wordlists
```

---

## ✨ Features

- ✅ **Multiple Hash Algorithms**: MD5, SHA1, SHA256
- ✅ **Auto Environment Setup**: Directories created on first run
- ✅ **Smart Wordlist Detection**: Auto-finds system wordlists (/usr/share/wordlists/)
- ✅ **CLI-First Design**: Like jwt_tool but for password cracking
- ✅ **Cross-Platform**: Linux, macOS, Windows
- ✅ **Wordlist Management**: Download and manage wordlists
- ✅ **Progress Reporting**: Real-time cracking status

---

## 🛠️ Requirements

- Python 3.8+
- click (CLI framework)
- requests (for downloading wordlists)

---

## 📝 Examples

### Example 1: Crack a known MD5 hash
```bash
$ redhunter crack -h 5f4dcc3b5aa765d61d8327deb882cf99 -a md5
[*] Using default wordlist: /usr/share/wordlists/rockyou.txt
[*] Starting attack...
[*] Hash: 5f4dcc3b5a... (Algorithm: MD5)
[+] Password found: password
```

### Example 2: Use custom wordlist
```bash
$ redhunter crack -h 827ccb0eea8a706c4c34a16891f84e7b \
                  -w ~/my_wordlist.txt \
                  -a md5
[*] Using wordlist: ~/my_wordlist.txt
[*] Starting attack...
[+] Password found: admin
```

### Example 3: Batch processing (create script)
```bash
#!/bin/bash
while read hash; do
  redhunter crack -h "$hash" -a md5
done < hashes.txt
```

---

## 🎯 Supported Algorithms

| Algorithm | Example Hash |
|-----------|---|
| MD5 | `5f4dcc3b5aa765d61d8327deb882cf99` |
| SHA1 | `aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d` |
| SHA256 | `5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8` |

---

## 📦 Default Wordlist Locations

The tool automatically searches for wordlists in:
- `/usr/share/wordlists/rockyou.txt` (Linux)
- `~/.redhunter/wordlists/` (User directory)
- Custom paths via `-w` option

---

## 🔧 Configuration

After installation, configuration is stored at:
- **Linux/macOS**: `~/.redhunter/`
- **Windows**: `%USERPROFILE%\.redhunter\`

---

## ⚙️ Installation Troubleshooting

### Python Path Issue (Windows)
```powershell
$python = "C:\Users\<YourUsername>\AppData\Local\Python\python3.14\python.exe"
& $python -m redhunter --help
```

### Wordlist Not Found
```bash
# Download wordlists
redhunter download

# Or create symlink to system wordlist
ln -s /usr/share/wordlists/rockyou.txt ~/.redhunter/wordlists/rockyou.txt
```

### Permission Denied
```bash
chmod +x postinstall.py
python postinstall.py
```

---

## 📄 License

MIT License - See LICENSE file for details

---

## 👨‍💻 Contributing

Pull requests welcome! Please follow PEP 8 style guide.

---

## 🐛 Reporting Issues

Found a bug? Open an issue on GitHub: [red-hat-hunter/issues](https://github.com/ravindushashiranga22/red-hat-hunter/issues)
