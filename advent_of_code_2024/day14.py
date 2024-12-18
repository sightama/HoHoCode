from collections import deque, defaultdict

DAY = 14


class AdventCode:

    def part1(self, inn: str):
        bots = {}
        rows = inn.split('\n')
        for i, row in enumerate(rows):
            splits = row.split(' ')
            p, v = splits[0], splits[1]
            p = p.split(',')
            x = int(p[0].split('=')[1])
            y = int(p[1])
            v = v.split(',')
            vx = int(v[0].split('=')[1])
            vy = int(v[1])
            bots[i] = {'p': (x, y), 'v': (vx, vy)}

        Y = 7  # 103
        X = 11  # 101
        steps = 100  # 100seconds
        matrix = [['.' for _ in range(X)] for _ in range(Y)]
        MAX_Y = len(matrix)
        MAX_X = len(matrix[0])

        bots = {10: bots[10]}
        for bot in bots.values():
            x, y = bot['p']
            dx, dy = bot['v']
            # move it.
            for i in range(100):
                new_x, new_y = x + dx, y + dy
                if new_x < 0 or new_y < 0 or new_x >= MAX_X-1 or new_y >= MAX_Y-1:
                    # means we need to do delta math on pacman style delta.
                    if new_x < 0:
                        new_x = MAX_X + new_x
                    elif new_x >= MAX_X:
                        new_x = MAX_X - new_x

                    if new_y < 0:
                        new_y = MAX_Y + new_y
                    elif new_y >= MAX_Y:
                        new_y = MAX_Y - new_y
                # we can move normally.
                x, y = new_x, new_y
                matrix[y][x] = 'X'  # Visual
                matrix[y][x] = '.'  # visual remove. 2nd iteration 6,5
