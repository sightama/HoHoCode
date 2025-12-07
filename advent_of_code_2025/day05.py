from collections import deque, Counter
from copy import deepcopy

DAY = 5


class AdventCode:

    # (10min for brute force sol - input too large... 27 min for final solution below)
    @staticmethod
    def part1(inn: str):
        seen = set()
        fresh = 0
        fuckMark = inn.split('\n\n')
        ranges = fuckMark[0]
        fruits = fuckMark[1]
        fruits = deque(fruits.split('\n'))
        ranges = ranges.split('\n')
        while fruits:
            current = int(fruits.popleft())
            for thing in ranges:
                l, r = thing.split('-')
                if current < int(l) or current > int(r):
                    continue
                else:
                    fresh += 1
                    break
        return fresh

    @staticmethod
    # fresh day - did in 35 min
    def part2(inn: str):
        fresh = inn.split('\n\n')
        ranges = fresh[0]
        ranges = ranges.split('\n')
        new_ranges = []
        for x in ranges:
            l, r = x.split('-')
            new_ranges.append((int(l), int(r)))
        ranges = sorted(new_ranges, key=lambda tup: tup[0])
        queue = deepcopy(deque(ranges))

        seen = set()
        new_ranges = []
        fresh = 0
        while queue:
            cur_l, cur_r = queue.popleft()
            for l, r in ranges:  # check current against all cases, but since ordered should be fast af.
                if l == cur_l and r == cur_r:
                    continue
                if l <= cur_l <= r:
                    cur_l = l
                if l <= cur_r <= r:
                    cur_r = r
            # if the final ranges are already seen skip adding it. could probably optimize this.
            for prev_l, prev_r in deepcopy(seen):
                if (prev_l <= cur_l <= prev_r) and (prev_l <= cur_r <= prev_r):  # means within bounds of existing,skip.
                    seen.add((cur_l, cur_r))  # just add to set below so it gets skipped. could be the same but just in case its not...
            if (cur_l, cur_r) not in seen:
                seen.add((cur_l, cur_r))
                new_ranges.append((cur_l, cur_r))  # just for clarity...
                total = cur_r - cur_l + 1  # +1 because its inclusive of the number 5-3 = 2 (+1) is 3 - 3,4,5
                fresh += total
        return fresh

    # @staticmethod  # brute force method.
    # def part1(inn: str):
    #     seen = set()
    #     result = 0
    #     fuckMark = inn.split('\n\n')
    #     ranges = fuckMark[0]
    #     fruits = fuckMark[1]
    #     ranges = ranges.split('\n')
    #     for thing in ranges:
    #         l, r = thing.split('-')
    #         for x in range(int(l), int(r) + 1):
    #             seen.add(x)
    #     fruits = fruits.split('\n')
    #     for fruit in fruits:
    #         if int(fruit) in seen:
    #             result += 1
    #     return result