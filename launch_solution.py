from pathlib import Path
from advent_of_code_2024.day12 import AdventCode, DAY


def read_input_file(dest):
    txt = Path(dest).read_text()
    return txt


if __name__ == "__main__":
    test_input = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""
    # test_input = read_input_file(f"advent_of_code_2024/inputs/day{DAY}.txt")
    xmas = AdventCode()
    result = xmas.part1(test_input)
    print(f"Complete! Result = {result}")
