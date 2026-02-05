import os

TRANSCRIPT_DIR = "./datasets/transcripts"
OOV_LIST = "oov_words.txt"

words = set()

for file in os.listdir(TRANSCRIPT_DIR):
    if file.endswith(".lab"):
        with open(os.path.join(TRANSCRIPT_DIR, file), "r") as f:
            for w in f.read().split():
                words.add(w)

with open(OOV_LIST, "w") as f:
    for w in sorted(words):
        f.write(w + "\n")

print("OOV word list created:", OOV_LIST)
