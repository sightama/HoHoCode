from pathlib import Path
from advent_of_code_2025.day05 import AdventCode, DAY


def read_input_file(dest):
    txt = Path(dest).read_text()
    return txt


if __name__ == "__main__":
    test_input = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""
    test_input = read_input_file(f"advent_of_code_2025/inputs/day{DAY}.txt")
    xmas = AdventCode()
    result = xmas.part2(test_input)
    print(f"Complete! Result = {result}")
