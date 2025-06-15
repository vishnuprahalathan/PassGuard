# PassGuard: Password Strength Analyzer and Custom Wordlist Generator

import argparse
import datetime
import os
import re
from zxcvbn import zxcvbn
from tkinter import Tk, Label, Entry, Button, Text, filedialog

# -----------------------------
# Leetspeak conversion mapping
# -----------------------------
leetspeak_map = {
    'a': ['a', '@', '4'],
    'e': ['e', '3'],
    'i': ['i', '1', '!'],
    'o': ['o', '0'],
    's': ['s', '$', '5'],
    't': ['t', '7']
}

# -----------------------------
# Password Strength Analyzer
# -----------------------------
def analyze_password_strength(password):
    result = zxcvbn(password)
    score = result['score']
    feedback = result['feedback']
    return score, feedback

# -----------------------------
# Custom Wordlist Generator
# -----------------------------
def generate_wordlist(name, dob, pet):
    base_words = [name, dob, pet]
    variations = set()
    common_suffixes = ["123", "@123", "2025", "!"]

    for word in base_words:
        word = word.lower()
        variations.add(word)
        variations.add(word[::-1])  # Reversed
        for suffix in common_suffixes:
            variations.add(word + suffix)
        for char in word:
            if char in leetspeak_map:
                for replacement in leetspeak_map[char]:
                    variations.add(word.replace(char, replacement))

    return sorted(variations)

# -----------------------------
# Save Wordlist to File
# -----------------------------
def save_wordlist_to_file(wordlist):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"custom_wordlist_{timestamp}.txt"
    with open(filename, "w") as file:
        for word in wordlist:
            file.write(word + "\n")
    print(f"Wordlist saved to {filename}")

# -----------------------------
# CLI Interface
# -----------------------------
def cli_mode():
    parser = argparse.ArgumentParser(description="PassGuard - Password Strength Analyzer and Wordlist Generator")
    parser.add_argument("--password", help="Password to analyze", required=True)
    parser.add_argument("--name", help="Your name")
    parser.add_argument("--dob", help="Your date of birth (e.g., 1998)")
    parser.add_argument("--pet", help="Your pet name")
    args = parser.parse_args()

    score, feedback = analyze_password_strength(args.password)
    print(f"Password Strength Score: {score} (0=Weak, 4=Strong)")
    print("Feedback:", feedback['warning'] or "Good password!", feedback['suggestions'])

    if args.name and args.dob and args.pet:
        wordlist = generate_wordlist(args.name, args.dob, args.pet)
        save_wordlist_to_file(wordlist)
    else:
        print("Wordlist generation skipped (name, dob, pet not fully provided).")

# -----------------------------
# GUI Interface (tkinter)
# -----------------------------
def gui_mode():
    def run_tool():
        password = password_entry.get()
        name = name_entry.get()
        dob = dob_entry.get()
        pet = pet_entry.get()

        score, feedback = analyze_password_strength(password)
        result_output.delete("1.0", "end")
        result_output.insert("end", f"Score: {score}/4\n")
        result_output.insert("end", f"Feedback: {feedback['warning']}\nSuggestions: {feedback['suggestions']}\n")

        if name and dob and pet:
            wordlist = generate_wordlist(name, dob, pet)
            save_wordlist_to_file(wordlist)
            result_output.insert("end", f"\nWordlist generated and saved.")

    root = Tk()
    root.title("PassGuard GUI")

    Label(root, text="Password:").pack()
    password_entry = Entry(root, show="*")
    password_entry.pack()

    Label(root, text="Name:").pack()
    name_entry = Entry(root)
    name_entry.pack()

    Label(root, text="Date of Birth (e.g., 1998):").pack()
    dob_entry = Entry(root)
    dob_entry.pack()

    Label(root, text="Pet Name:").pack()
    pet_entry = Entry(root)
    pet_entry.pack()

    Button(root, text="Analyze + Generate Wordlist", command=run_tool).pack()

    result_output = Text(root, height=10, width=50)
    result_output.pack()

    root.mainloop()

# -----------------------------
# Main Execution
# -----------------------------
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        cli_mode()
    else:
        gui_mode()
