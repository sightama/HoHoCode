from collections import deque, Counter
from advent_of_code_2022.utils import read_input_file
from string import ascii_lowercase, ascii_uppercase


class AdventOfCode:
    def part1(self, pairs):
        pairs = pairs.strip()
        pairs = pairs.split('\n')
        total = 0
        for pair in pairs:
            pair = pair.strip()
            decoupled = pair.split(',')
            decoupled = [x.split('-') for x in decoupled]
            x1, y1, x2, y2 = decoupled[0][0], decoupled[0][1], decoupled[1][0], decoupled[1][1]
            result = self.in_range(int(x1), int(y1), int(x2), int(y2))
            total += result
        return total

    def in_range(self, x1, y1, x2, y2):
        if x1 <= x2 and y1 >= y2:
            return 1
        elif x2 <= x1 and y2 >= y1:
            return 1
        else:
            return 0

    def overlap(self, x1, y1, x2, y2):
        if x1 <= x2:
            leftbound = x1
            while leftbound != y1+1:
                if leftbound == x2 or leftbound == y2:
                    return 1
                leftbound += 1
        if x2 <= x1:
            leftbound = x2
            while leftbound != y2+1:
                if leftbound == x1 or leftbound == y1:
                    return 1
                leftbound += 1
        return 0

    def part2(self, pairs):
        pairs = pairs.strip()
        pairs = pairs.split('\n')
        total = 0
        for pair in pairs:
            pair = pair.strip()
            decoupled = pair.split(',')
            decoupled = [x.split('-') for x in decoupled]
            x1, y1, x2, y2 = decoupled[0][0], decoupled[0][1], decoupled[1][0], decoupled[1][1]
            result = self.overlap(int(x1), int(y1), int(x2), int(y2))
            total += result
        return total


if __name__ == "__main__":
    # https://adventofcode.com/2022/day/4 - p1 20 minutes, lil mistakes such as using str not int comaprator
    # 20 minutes p2
    test = AdventOfCode()
    # actions_input = \
    #     """
    #     2-4,6-8
    #     2-3,4-5
    #     5-7,7-9
    #     2-8,3-7
    #     6-6,4-6
    #     2-6,4-8
    #     """
    # answer = test.part1(actions_input)
    # print(answer)
    #
    # actual_data = read_input_file("./inputs/day4.txt")
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

    actual_data = read_input_file("./inputs/day4.txt")
    answer = test.part2(actual_data)
    print(answer)
