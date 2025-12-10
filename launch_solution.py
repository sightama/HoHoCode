from pathlib import Path
from advent_of_code_2025.day10  import AdventCode, DAY


def read_input_file(dest):
    txt = Path(dest).read_text()
    return txt


if __name__ == "__main__":
    test_input = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""
    test_input = read_input_file(f"advent_of_code_2025/inputs/day{DAY}.txt")
    xmas = AdventCode()
    result = xmas.part1(test_input)
    print(f"Complete! Result = {result}")
