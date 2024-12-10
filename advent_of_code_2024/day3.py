import re
from collections import deque
from typing import List
from copy import copy

DAY = 3

DO = 'do()'
DONT = "don't()"


class AdventCode:

    @staticmethod
    def part1(inn: str):
        total = 0
        potential_cases = inn.split('mul(')
        queue = deque(potential_cases)
        queue.popleft()  # first one has nothing.
        while queue:
            current = queue.popleft()
            each_char = list(current)
            good_case = False
            comma_reached = False
            first_num = ''
            second_num = ''
            for char in each_char:
                if char.isnumeric() and not comma_reached:
                    first_num += char
                elif char.isnumeric() and comma_reached:
                    second_num += char
                elif char == ',':
                    comma_reached = True
                    continue
                elif char == ')' and comma_reached:
                    # done!
                    good_case = True
                    break
                else:
                    # means something else and we should fail. BAD
                    break
            if good_case:
                total += (int(first_num) * int(second_num))
        return total

    @staticmethod
    def part2(inn: str):
        total = 0
        potential_cases = inn.split('mul(')
        ignore_execution = False
        queue = deque(potential_cases)
        queue.popleft()  # first one has nothing.
        while queue:
            current = queue.popleft()
            each_char = list(current)
            comma_reached = False
            first_num = ''
            second_num = ''
            for char in each_char:
                if char.isnumeric() and not comma_reached:
                    first_num += char
                elif char.isnumeric() and comma_reached:
                    second_num += char
                elif char == ',':
                    comma_reached = True
                    continue
                elif char == ')' and comma_reached and not ignore_execution:
                    # done!
                    total += (int(first_num) * int(second_num))
                    break
                else:
                    # means something else and we should fail. BAD
                    break
            if DO in current:
                ignore_execution = False
            if DONT in current:
                ignore_execution = True
        return total
