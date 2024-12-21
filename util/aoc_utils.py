from pathlib import Path

def read_file(path: Path):
    with open(path, "r", encoding="utf8") as f:
        for line in f:
            line = line.rstrip()
            if line:
                yield line
