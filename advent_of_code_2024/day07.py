from copy import deepcopy
from collections import deque, defaultdict
from typing import List
from itertools import product

DAY = 7


def generate_permutations(letters, edges):
    permutations = list(product(letters, repeat=edges))
    pretty = deque()
    for p in permutations:
        pretty.append(''.join(p))
    return pretty


class AdventCode:

    def part1(self, inn: str):
        operators = {}
        rows = inn.split('\n')
        # organize data
        for row in rows:
            vals = row.split(':')
            test_value = int(vals[0])
            vals = [int(x) for x in vals[1].strip().split()]
            operators[test_value] = vals

        # check all permutations and if one = test_value partay add to total
        total = 0
        for test_value, vals in operators.items():
            edges = len(vals) - 1
            permutations = generate_permutations(['m', 'a'], edges)

            # Check permutations
            og_first_value = vals[0]
            valid = False
            for current in permutations:
                a = og_first_value
                for op, num in zip(current, vals[1:]):  # not deep copying vals here fucked shit up..........gdi
                    if op == 'a':
                        a += num
                    elif op == 'm':
                        a *= num

                if a == test_value:
                    valid = True  # break early
                    break

            if valid:
                total += test_value

        return total
