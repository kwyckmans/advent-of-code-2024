from typing import Sequence
from util.aoc_utils import read_file_into_list


def is_strictly_uniform_direction(prev: int, cur: int, next: int):
    is_uniform_direction = prev > cur > next or prev < cur < next
    print(f"Is {prev} - {cur} - {next} uniform? - {is_uniform_direction}")
    return is_uniform_direction


def is_safe_with_skip(report: Sequence[int], skipped: bool = False):
    if is_safe(report):
        # Safe without removing anything
        return True

    for i in range(len(report)):
        reduced_report = report[:i] + report[i+1:]
        if is_safe(reduced_report):
            return True
        
    return False


def is_safe(report: Sequence[int]):
    if len(report) < 2:
        return True 
    
    is_increasing = True
    is_decreasing = True

    for i in range(1, len(report)):
        diff = report[i] - report[i-1]
        if diff <= 0:
            is_increasing = False
        if diff >= 0:
            is_decreasing = False
        if abs(diff) > 3 or diff == 0:
            return False

    return is_increasing or is_decreasing


if __name__ == "__main__":
    no_of_safe_reports = 0
    no_of_safe_reports_w_skip = 0
    for l in read_file_into_list("day2/input_day2.txt"):
        no_of_safe_reports += 1 if is_safe(l) else 0
        no_of_safe_reports_w_skip += 1 if is_safe_with_skip(l) else 0

    print(no_of_safe_reports)
    print(no_of_safe_reports_w_skip)
