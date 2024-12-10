from collections import deque
from typing import List
from copy import copy

DAY = 2


class AdventCode:

    @staticmethod
    def part1(inn: str):
        safeReports = 0
        inn = inn.split('\n')
        for report in inn:
            levels = report.split(' ')
            levels = [int(x) for x in levels]
            queue = deque(levels)
            # sneak into first two elements for direction
            if levels[1] > levels[0]:
                increasing = True
            else:
                increasing = False

            previous = None
            safe = True
            while queue:
                current = queue.popleft()
                if previous is None:  # first level
                    previous = current
                    continue
                # get all possible values based on increase/decrease
                if increasing:
                    possible_nums = [previous + x for x in range(1, 4)]
                else:
                    possible_nums = [previous - x for x in range(1, 4)]

                if current not in possible_nums:
                    safe = False
                previous = current

            if safe:
                safeReports += 1
        return safeReports

    def part2(self, inn: str):
        safeReports = 0
        inn = inn.split('\n')
        for report in inn:
            levels = report.split(' ')
            levels = [int(x) for x in levels]
            all_variations = []
            for x in range(len(levels)):
                variate = copy(levels)
                variate.pop(x)
                all_variations.append(variate)

            for variation in all_variations:
                safe = self.safe_or_not(variation)
                if safe:
                    safeReports += 1
                    break
        return safeReports

    def determine_holistic_direction(self, levels: List):
        increasing = 0
        decreasing = 0
        queue = deque(levels)
        previous = queue.popleft()
        while queue:
            current = queue.popleft()
            if current > previous:
                increasing += 1
            else:
                decreasing += 1
            previous = current
        return increasing > decreasing

    def safe_or_not(self, levels: List):
        increasing = self.determine_holistic_direction(levels)
        queue = deque(levels)
        previous = None
        safe = True
        while queue:
            current = queue.popleft()
            if previous is None:  # first level
                previous = current
                continue
            # get all possible values based on increase/decrease
            if increasing:
                possible_nums = [previous + x for x in range(1, 4)]
            else:
                possible_nums = [previous - x for x in range(1, 4)]

            if current not in possible_nums:
                safe = False
                break
            previous = current
        return safe
