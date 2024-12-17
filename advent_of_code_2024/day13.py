from collections import deque, defaultdict
import numpy as np

DAY = 13


class AdventCode:

    def parse_inn(self, inn: str):
        # parse all one by one,  each 3 lines separated by double newline i believe
        # each machine in-order id = 0 -> N
        final = {}
        prizes = inn.split('\n\n')
        for i, x in enumerate(prizes):
            rows = x.split('\n')
            aa = rows[0]
            aa = aa.split(',')
            ax = int([s for s in aa[0].split('+') if s.isdigit()][0])
            ay = int([s for s in aa[1].split('+') if s.isdigit()][0])
            bb = rows[1]
            bb = bb.split(',')
            bx = int([s for s in bb[0].split('+') if s.isdigit()][0])
            by = int([s for s in bb[1].split('+') if s.isdigit()][0])

            cc = rows[2]
            cc = cc.split(',')
            px = int([s for s in cc[0].split('=') if s.isdigit()][0])
            py = int([s for s in cc[1].split('=') if s.isdigit()][0])
            final[i] = {'a': (ax, ay), 'b': (bx, by), 'p': (px, py)}
        return final

    def part1(self, inn: str):
        # note: each button will be pressed NO MORE THAN 100x. A = 3 tokens, B = 1 token.
        # so for each B starting at 100-whatever it takes to be beelow the x,y of each. then do a+n, and eventually b-N
        min_tokens = 0
        prizes = self.parse_inn(inn)
        for _, prize in prizes.items():
            a, b = 100, 100  # start b -> 100, a -> 0
            cases = set()  # cases where an A,B would cause = prize locatyion X,Y
            queue = deque([(a, b)])
            visited = set()
            while queue:
                a, b = queue.popleft()
                if (a, b) in visited:
                    continue
                else:
                    visited.add((a, b))
                # a & b must always be under 100.
                b_x, b_y = prize['b'][0] * b, prize['b'][1] * b
                if b_x > prize['p'][0] or b_y > prize['p'][1]:
                    queue.append((a, b - 1))  # B is too big
                    continue  # skip rest til we below amount.

                a_x, a_y = prize['a'][0] * a, prize['a'][1] * a
                if a_x > prize['p'][0] or a_y > prize['p'][1]:
                    queue.append((a - 1, b))  # A is too big.
                    continue

                tot_x, tot_y = a_x + b_x, a_y + b_y
                if tot_x == prize['p'][0] and tot_y == prize['p'][1]:
                    cases.add((a, b))  # case where B = N and A = N - all success cases here.
                    break  # TODO: better way to check if 100x100for all cases?

                if tot_x > prize['p'][0] or tot_y > prize['p'][1]:
                    for xx in [(a - 1, b - 1), (a - 1, b), (a, b - 1)]:
                        if xx not in visited:
                            queue.append(xx)  # both too big together.  try all variations if not seen.
                    continue

            if cases:
                compare = set()
                for x, y in cases:
                    total = 0
                    total += x * 3
                    total += y * 1
                    compare.add(total)
                min_needed = min(compare)
                min_tokens += min_needed

        return min_tokens

    def parse_inn_2(self, inn: str):
        # parse all one by one,  each 3 lines separated by double newline i believe
        # each machine in-order id = 0 -> N
        final = {}
        prizes = inn.split('\n\n')
        for i, x in enumerate(prizes):
            rows = x.split('\n')
            aa = rows[0]
            aa = aa.split(',')
            ax = int([s for s in aa[0].split('+') if s.isdigit()][0])
            ay = int([s for s in aa[1].split('+') if s.isdigit()][0])
            bb = rows[1]
            bb = bb.split(',')
            bx = int([s for s in bb[0].split('+') if s.isdigit()][0])
            by = int([s for s in bb[1].split('+') if s.isdigit()][0])

            cc = rows[2]
            cc = cc.split(',')
            px = int([s for s in cc[0].split('=') if s.isdigit()][0]) + 10000000000000
            py = int([s for s in cc[1].split('=') if s.isdigit()][0]) + 10000000000000
            final[i] = {'a': (ax, ay), 'b': (bx, by), 'p': (px, py)}
        return final

    def part2(self, inn: str):
        min_tokens = 0
        prizes = self.parse_inn_2(inn)
        for _, prize in prizes.items():
            cases = set()  # cases where an A,B would cause = prize locatyion X,Y
            matrix = np.array([[prize['a'][0], prize['b'][0]], [prize['a'][1], prize['b'][1]]])  # coefficient matrix
            constants = np.array([prize['p'][0], prize['p'][1]])
            det = np.linalg.det(matrix)
            if det == 0:
                continue  # matrix is NOT invertible as per deeterminant

            # Compute the floating-point solution
            new_a_b = np.linalg.solve(matrix, constants)

            whole_nums = [round(new_a_b[0]), round(new_a_b[1])]  # round up & check combos

            # Verify the rounded solution
            a, b = whole_nums
            if (prize['a'][0] * a + prize['b'][0] * b == prize['p'][0] and prize['a'][1] * a + prize['b'][1] * b ==
                    prize['p'][1]):
                cases.add((a, b))

            # If rounding doesn't yield valid results, try nearby integers
            for a in range(whole_nums[0] - 1, whole_nums[0] + 2):
                for b in range(whole_nums[1] - 1, whole_nums[1] + 2):
                    if (prize['a'][0] * a + prize['b'][0] * b == prize['p'][0] and prize['a'][1] * a + prize['b'][
                        1] * b == prize['p'][1]):
                        cases.add((a, b))  # double hits but its a set who cares

            # nothing, therefore move on

            if cases:
                compare = set()
                for x, y in cases:
                    total = 0
                    total += x * 3
                    total += y * 1
                    compare.add(total)
                min_needed = min(compare)
                min_tokens += min_needed

        return min_tokens
