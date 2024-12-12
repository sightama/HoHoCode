from pathlib import Path
from advent_of_code_2024.day05 import AdventCode, DAY


def read_input_file(dest):
    txt = Path(dest).read_text()
    return txt


if __name__ == "__main__":
    test_input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""  # """0 1 10 99 999"""
    test_input = read_input_file(f"advent_of_code_2024/inputs/day{DAY}.txt")
    xmas = AdventCode()
    result = xmas.part2(test_input)
    print(f"Complete! Result = {result}")
