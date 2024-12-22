from pathlib import Path
import re
from util.aoc_utils import read_file

INSTRUCTION_PATTERN = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
CONDITIONAL_PATTERN = re.compile(r"(?<=do\(\))(.*?)(?:don't\(\)|$)")

def get_total_with_conditional(line:str):
    result = 0
    enabled = True

    # Modified pattern to only match 1-3 digit numbers
    pattern = r'(do\(\))|(don\'t\(\))|(mul\((\d{1,3}),(\d{1,3})\))'

    # Find all matches in order of appearance
    matches = re.finditer(pattern, line)

    # For debugging
    operations = []
    state_changes = []

    for match in matches:
        # TODO: Read up about matching groups.
        if match.group(1):  # do()
            enabled = True
            state_changes.append(("do()", enabled))
        elif match.group(2):  # don't()
            enabled = False
            state_changes.append(("don't()", enabled))
        elif match.group(3) and enabled:  # mul(x,y) when enabled
            try:
                num1 = int(match.group(4))
                num2 = int(match.group(5))
                # Additional check to ensure numbers are within range (though regex should handle this)
                if num1 > 999 or num2 > 999:
                    continue
                product = num1 * num2
                result += product
                operations.append((num1, num2, product, enabled))
            except ValueError:
                continue

    # Print summary
    print("\nState changes:")
    for op, state in state_changes[:10]:  # First 10 state changes
        print(f"{op} -> enabled={state}")

    print("\nFirst 10 multiplications:")
    for i, (n1, n2, prod, en) in enumerate(operations[:10]):
        print(f"mul({n1},{n2}) = {prod} (enabled={en})")

    print("\nLast 10 multiplications:")
    for n1, n2, prod, en in operations[-10:]:
        print(f"mul({n1},{n2}) = {prod} (enabled={en})")

    print(f"\nTotal multiplications counted: {len(operations)}")
    print(f"Total state changes: {len(state_changes)}")
    print(f"Final result: {result}")

    return result

def get_total(line:str):
    # print(line)
    matches = INSTRUCTION_PATTERN.findall(line)
    total = 0
    
    for match in matches:
        # print(match)
        numbers = match[4:-1].split(',') 
        num1 = int(numbers[0].strip())
        num2 = int(numbers[1].strip())
        # print(num1, num2)
        total += num1 * num2

    return total

if __name__ == "__main__":
    path = Path("day3/input_day3.txt")
    total = 0 
    for line in read_file(path):
        total += get_total(line)

    print(total)

    with open('day3/input_day3.txt', 'r') as file:
        puzzle_input = file.read().strip()
    
        answer = get_total_with_conditional(puzzle_input)
        print(answer)
    