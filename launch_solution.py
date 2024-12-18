from pathlib import Path
from advent_of_code_2024.day18 import AdventCode, DAY


def read_input_file(dest):
    txt = Path(dest).read_text()
    return txt


if __name__ == "__main__":
    test_input = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""
    test_input = read_input_file(f"advent_of_code_2024/inputs/day{DAY}.txt")
    xmas = AdventCode()
    result = xmas.part2(test_input)
    print(f"Complete! Result = {result}")