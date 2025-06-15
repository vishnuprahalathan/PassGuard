# PassGuard: Password Strength Analyzer & Wordlist Generator

PassGuard is a Python-based cybersecurity tool that helps users evaluate the strength of their passwords using entropy and pattern analysis (`zxcvbn`), while also generating a personalized wordlist for ethical hacking or security auditing purposes.

## 🔐 Features
- Analyze password strength using entropy score.
- Generate wordlists using user-specific inputs (Name, DOB, Pet Name).
- Includes leetspeak, reversed strings, and suffix-based permutations.
- CLI support using argparse.
- GUI support using tkinter.
- Wordlist export with timestamp.
- Lightweight and portable — no external server or network needed.

## 📂 Folder Structure
```
PassGuard-Password-Analyzer/
├── passguard.py
├── README.md
├── requirements.txt
├── sample_output/
├── screenshots/
└── report.pdf
```

## 🚀 How to Run

### CLI Mode
```bash
python passguard.py --password "YourPassword" --name "Alice" --dob "1999" --pet "Fluffy"
```

### GUI Mode
```bash
python passguard.py
```

## 🛠️ Tech Stack
- Python
- zxcvbn
- argparse
- tkinter

## 📦 Output
- Wordlist saved as `.txt` with timestamp
- Password strength score from 0 (weak) to 4 (strong)

## 📸 Screenshots
_Add GUI screenshots in the `screenshots/` folder_

