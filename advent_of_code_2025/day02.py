from collections import deque, Counter
from copy import deepcopy

DAY = 2


class AdventCode:
    # (24 min)
    @staticmethod
    def part1(inn: str):
        # invalid ids = cut string in half they match.
        # edge cases - no leading zeroes
        total = 0
        ranges = inn.strip().split(',')
        queue = deque()
        for x in ranges:
            cur = x.split('-')
            queue.append((cur[0], cur[1]))
        while queue:
            l, r = queue.popleft()
            for x in range(int(l), int(r) + 1):
                str_x = str(x)
                length = len(str_x)
                if length % 2 != 0:
                    continue
                # now split n compare.
                length = length // 2
                left = str_x[length:]
                right = str_x[:length]
                if left == right:
                    total += x
        return total

    @staticmethod # 15 minutes time
    def part2(inn: str):
        # edge cases -
        # all values are the same for whole str (prime case)
        # basically check pattern for all sections if divisible by any of our main numbesr 1-9
        total = 0
        ranges = inn.strip().split(',')
        queue = deque()
        for x in ranges:
            cur = x.split('-')
            queue.append((cur[0], cur[1]))
        while queue:
            l, r = queue.popleft()
            seen = set()
            for x in range(int(l), int(r) + 1):
                for modulo in range(1, 10):
                    str_x = str(x)
                    length = len(str_x)
                    if length % modulo != 0:
                        continue
                    # now split n compare.
                    mod_length = length // modulo
                    vals = []
                    for z in range(0, length, mod_length):
                        vals.append(str_x[z:z+mod_length])
                    if len(set(vals)) == 1 and len(vals) > 1 and x not in seen:
                        seen.add(x)
                        total += x
        return total
