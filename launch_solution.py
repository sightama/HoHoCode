from pathlib import Path
from advent_of_code_2024.day13 import AdventCode, DAY


def read_input_file(dest):
    txt = Path(dest).read_text()
    return txt


if __name__ == "__main__":
    test_input = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""
    test_input = read_input_file(f"advent_of_code_2024/inputs/day{DAY}.txt")
    xmas = AdventCode()
    result = xmas.part2(test_input)
    print(f"Complete! Result = {result}")
# try asgain - 1538336