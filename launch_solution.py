from pathlib import Path
from advent_of_code_2025.day06 import AdventCode, DAY


def read_input_file(dest):
    txt = Path(dest).read_text()
    return txt


if __name__ == "__main__":
    test_input = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """
    test_input = read_input_file(f"advent_of_code_2025/inputs/day{DAY}.txt")
    xmas = AdventCode()
    result = xmas.part2(test_input)
    print(f"Complete! Result = {result}")
