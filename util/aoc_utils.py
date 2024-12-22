from pathlib import Path
from typing import Callable, Generator, List

def read_file(path: Path) -> Generator[str, None, None]:
    with open(path, "r", encoding="utf8") as f:
        for line in f:
            line = line.rstrip()
            if line:
                yield line

def read_file_into_list[T](path: Path, mapper: Callable[[str], T] = int) -> Generator[List[T], None, None]:
    with open(path, "r", encoding="utf8") as f:
        for line in f:
            line = line.rstrip()
            if line:
                yield [mapper(elem) for elem in line.split(" ")]

