from pathlib import Path
from typing import Counter, Sequence
from util import aoc_utils

type LocationID = int
type Count = int

def get_similiary(left: Sequence[LocationID], right: Sequence[LocationID]):
    frequncy_map = Counter(right)

    total = 0
    for elem in left:
        print(elem, frequncy_map[elem])
        total += frequncy_map[elem] * elem
    return total

def get_total_distance(left: Sequence[LocationID], right: Sequence[LocationID]):
    left.sort()
    right.sort()
    
    distance = 0
    for l, r in zip(left, right):
        distance += abs(l - r)

    return distance

if __name__ == "__main__":
    path = Path("day1/input_day1.txt")

    entries =[entry.split("   ") for entry in aoc_utils.read_file(path)]
    left = [int(entry[0]) for entry in entries]
    right = [int(entry[1]) for entry in entries]
    
    result = get_total_distance(left, right)
    print(result)

    result = get_similiary(left, right)
    print(result)
    
