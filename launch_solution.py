from pathlib import Path
from advent_of_code_2024.day10 import AdventCode, DAY


def read_input_file(dest):
    txt = Path(dest).read_text()
    return txt


if __name__ == "__main__":
    test_input = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
    test_input = read_input_file(f"advent_of_code_2024/inputs/day{DAY}.txt")
    xmas = AdventCode()
    result = xmas.part2(test_input)
    print(f"Complete! Result = {result}")
