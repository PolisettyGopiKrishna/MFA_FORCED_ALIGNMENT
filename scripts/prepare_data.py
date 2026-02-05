import os
import re

TRANSCRIPT_DIR = "./datasets/transcripts"

def clean_text(text):
    text = text.upper()
    text = re.sub(r"[^A-Z' ]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

if not os.path.exists(TRANSCRIPT_DIR):
    print("❌ Transcript folder not found:", TRANSCRIPT_DIR)
    exit()

files_found = False

for filename in os.listdir(TRANSCRIPT_DIR):
    if filename.endswith(".txt"):
        files_found = True
        path = os.path.join(TRANSCRIPT_DIR, filename)

        with open(path, "r", encoding="utf8") as f:
            content = f.read()

        cleaned = clean_text(content)

        new_filename = os.path.splitext(filename)[0] + ".lab"
        new_path = os.path.join(TRANSCRIPT_DIR, new_filename)

        with open(new_path, "w", encoding="utf8") as f:
            f.write(cleaned)

        print(f"✅ Converted {filename} → {new_filename}")

if not files_found:
    print("⚠️ No .txt files found in", TRANSCRIPT_DIR)
