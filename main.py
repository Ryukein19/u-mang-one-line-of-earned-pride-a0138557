import os
# One-liner entry (max 240 chars): the single line below is the entire submission.
# Output goes to /output/entry.txt.
LINE = "He practised the same scale for eleven years, and the night the hall finally went quiet, every note landed exactly where he had promised himself it would."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
