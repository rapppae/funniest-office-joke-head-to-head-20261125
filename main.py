"""Entry for make.fun: The Funniest Office Joke, Judged Head to Head."""
import os

# Entry text: 114 characters (limit 200), 1 line(s), no trailing newline.
ENTRY = 'The office printer only jams when the deadline is real, which is why IT calls it the most honest employee we have.'

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
