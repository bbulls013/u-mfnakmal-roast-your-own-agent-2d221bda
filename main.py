#!/usr/bin/env python3
import os

LINE = "My agent burns 40k tokens of context to say 'yes', then bills me for summarizing the summary."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
