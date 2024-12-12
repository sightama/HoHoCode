from pathlib import Path
from advent_of_code_2024.day07 import AdventCode, DAY


def read_input_file(dest):
    txt = Path(dest).read_text()
    return txt


if __name__ == "__main__":
    test_input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""
    test_input = read_input_file(f"advent_of_code_2024/inputs/day{DAY}.txt")
    xmas = AdventCode()
    result = xmas.part1(test_input)
    print(f"Complete! Result = {result}")


# why is this value too low = 3350727455032
                            # 3351430525058
                            # 3351424676480
                            # 3351424676480
# REAL ANSWER  3312271365652