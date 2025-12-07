from collections import deque, Counter
from copy import deepcopy

DAY = 5


class AdventCode:

    # (10 - solved but not for actual input too large. 27 min for final solution below)
    # @staticmethod
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
    # fresh day try again 12/07 @ 11:16am
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
        prev_l, prev_r = None, None
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

    # (hour and 10 minute thus far no luck today :() - answer i got = 357135405057452 - too high
    # @staticmethod
    # def part2(inn: str):
    #     # goal: find all UNIQUE numbers within all these ranges
    #     seen = set()
    #     fresh = 0
    #     fuckMark = inn.split('\n\n')
    #     ranges = fuckMark[0]
    #     ranges = deque(ranges.split('\n'))
        # # sort the ranges in tuples and start from the middle.
        # new_ranges = []
        # for x in ranges:
        #     l, r = x.split('-')
        #     new_ranges.append((int(l), int(r)))
        # ranges = sorted(new_ranges)
        # while ranges:
        #     current = ranges.popleft()
        #     l, r = current.split('-')
        #     for x in range(int(l) ,int(r)+1):
        #         if x in seen:
        #             continue
        #         else:
        #             fresh += 1
        #             seen.add(x)
        # return fresh
    # @staticmethod
    # def part2(inn: str):
    #     fresh = 0
    #     fuck = inn.split('\n\n')
    #     ranges = fuck[0]
    #     ranges = ranges.split('\n')
    #     # sort the ranges in tuples and start from the middle.
    #     new_ranges = []
    #     for x in ranges:
    #         l, r = x.split('-')
    #         new_ranges.append((int(l), int(r)))
    #     ranges = sorted(new_ranges)
    #     finalist = []
    #     overlap =  True
    #     while overlap:
    #         finalist = []
    #         overlap = False
    #         for x in range(len(ranges)):
    #             skip = 0
    #             yl, yr = ranges[x][0], ranges[x][1]
    #             l, r = ranges[x][0], ranges[x][1]
    #             if x+1 == len(ranges):
    #                  break
    #             xl, xr = ranges[x+1+skip][0], ranges[x+1+skip][1]
    #             if xl <= l < xr:
    #                 yl = xl
    #             if xl <= r < xr:
    #                 yr = xr
    #             if l <= xl < r:
    #                 yl = l
    #             if l <= xr < r:
    #                 yr = r
    #             if yl == l and r == yr:  # no overlap wit neighbor
    #                 finalist.append((yl, yr))
    #             else:
    #                 skip += 1
    #                 overlap = True
    #                 finalist.append((yl, yr))
    #         if overlap:
    #             ranges = finalist
    #         else:
    #             pass
    #     total = 0
    #     for x,y in ranges:
    #         total += y-x + 1
    #     return total  # 551290235649751 - answer too high.
    #




        # queue = deque(deepcopy(ranges))
        #seen = set()  # these are ranges that have been combined already
        # find overlaps and make them one range instead of brute force.
        # while queue:
        #     current = queue.popleft()
        #     og_l, og_r = current.split('-')
        #     cur_l, cur_r = int(og_l), int(og_r)
        #     if (cur_l, cur_r) in seen:
        #         continue
        #     seen.add((cur_l, cur_r))
        #
        #     for thing in ranges:
        #         l, r = thing.split('-')
        #         l, r = int(l), int(r)
        #         if (l, r) in seen:
        #             continue
        #         if l <= cur_l <= r:
        #             cur_l = l
        #             seen.add((l, r))
        #         if l <= cur_r <= r:
        #             cur_r = r
        #             seen.add((l, r))
        #     total = cur_r - cur_l
        #     fresh += total

                    # subtract -= (r - cur_l)
        #     # check if any overlap - figure it out if so otherwise just add the difference
        #     for thing in ranges:
        #         l, r = thing.split('-')
        #         l, r = int(l), int(r)
        #         if l==cur_l and r==cur_r:
        #             continue
        #         if l <= cur_l <= r:
        #             subtract -= (r - cur_l)
        #         elif l <= cur_r <= r:
        #             subtract += (cur_r - l)
        #     fresh += cur_r - cur_l
        # fresh -= subtract
        # return fresh
