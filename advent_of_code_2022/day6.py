from collections import deque, Counter
from advent_of_code_2022.utils import read_input_file
from string import ascii_lowercase, ascii_uppercase


class AdventOfCode:
    def part1(self, stream):
        counter = 0
        current_seq = deque([])
        queue = deque(list(stream))
        while queue:
            current = queue.popleft()
            if len(current_seq) < 4:
                counter += 1
                current_seq.append(current)
                continue

            if len(current_seq) == len(set(current_seq)):
                return counter
            else:
                current_seq.popleft()
                current_seq.append(current)
            counter += 1

    def part2(self, stream):
        counter = 0
        current_seq = deque([])
        queue = deque(list(stream))
        while queue:
            current = queue.popleft()
            if len(current_seq) < 14:
                counter += 1
                current_seq.append(current)
                continue

            if len(current_seq) == len(set(current_seq)):
                return counter
            else:
                current_seq.popleft()
                current_seq.append(current)
            counter += 1


if __name__ == "__main__":
    # https://adventofcode.com/2022/day/6 - p quick this one not bad
    test = AdventOfCode()
    actions_input = \
"""mjqjpqmgbljsphdztnvjfqwrcgsmlb"""
    # answer = test.part1(actions_input)
    # print(answer)

    # actual_data = read_input_file("./inputs/day6.txt")
    # answer = test.part1(actual_data)
    # print(answer)

    ###### PART TWO ######

    # actions_input = \
    #     """
    #     2-4,6-8
    #     2-3,4-5
    #     5-7,7-9
    #     2-8,3-7
    #     6-6,4-6
    #     2-6,4-8
    #     """
    # answer = test.part2(actions_input)
    # print(answer)

    # actual_data = read_input_file("./inputs/day6.txt")
    # answer = test.part2(actual_data)
    # print(answer)
