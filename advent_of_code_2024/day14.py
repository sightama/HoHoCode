DAY = 14


class AdventCode:

    def part1(self, inn: str):
        bots = {}
        rows = inn.split('\n')
        # parse input
        for i, row in enumerate(rows):  # you hideous child you kek
            splits = row.split(' ')
            p, v = splits[0], splits[1]
            p = p.split(',')
            x = int(p[0].split('=')[1])
            y = int(p[1])
            v = v.split(',')
            vx = int(v[0].split('=')[1])
            vy = int(v[1])
            bots[i] = {'p': (x, y), 'v': (vx, vy)}
        # set size of table wide long
        Y = 103  # 7  #
        X = 101  # 11  #
        # how many "seconds/steps"
        steps = 100
        matrix = [['.' for _ in range(X)] for _ in range(Y)]
        MAX_Y = len(matrix)
        MAX_X = len(matrix[0])

        bots_pos = {}
        for w, bot in bots.items():
            x, y = bot['p']
            dx, dy = bot['v']
            # move it.
            for i in range(100):
                new_x, new_y = x + dx, y + dy
                if new_x < 0 or new_y < 0 or new_x >= MAX_X - 1 or new_y >= MAX_Y - 1:
                    # means we need to do delta math on pacman style delta.
                    if new_x < 0:
                        new_x = MAX_X + new_x
                    elif new_x >= MAX_X:
                        new_x = new_x - MAX_X

                    if new_y < 0:
                        new_y = MAX_Y + new_y
                    elif new_y >= MAX_Y:
                        new_y = new_y - MAX_Y
                # we can move normally.
                x, y = new_x, new_y
                # matrix[y][x] = 'X'  # Visual
                # matrix[y][x] = '.'  # visual remove. 2nd iteration 6,5
            # this x,y are final state for this bot. place now.
            bots_pos[w] = (x, y)

        for (x, y) in bots_pos.values():  # fill table with where bots are now
            if isinstance(matrix[y][x], int):
                matrix[y][x] += 1
            else:
                matrix[y][x] = 1

        # Guaranteed table is an odd number so we can build quadrants
        mid_x = MAX_X // 2
        mid_y = MAX_Y // 2
        top_left = [row[:mid_x] for row in matrix[:mid_y]]
        top_right = [row[mid_x + 1:] for row in matrix[:mid_y]]
        bottom_left = [row[:mid_x] for row in matrix[mid_y + 1:]]
        bottom_right = [row[mid_x + 1:] for row in matrix[mid_y + 1:]]

        # now iterate quadrants, get total bots, add to list and multiply each otehr
        kek = []
        for q in [top_left, top_right, bottom_left, bottom_right]:
            bot_total_count = 0
            for y in range(len(q)):
                for x in range(len(q[0])):
                    if isinstance(q[y][x], int):
                        bot_total_count += q[y][x]
                    # otherewise just a '.' and move on.
            kek.append(bot_total_count)
        result = 1
        for x in kek:
            result *= x
        return result

    def part2(self, inn: str):
        bots = {}
        rows = inn.split('\n')
        # parse input
        for i, row in enumerate(rows):  # you hideous child you kek
            splits = row.split(' ')
            p, v = splits[0], splits[1]
            p = p.split(',')
            x = int(p[0].split('=')[1])
            y = int(p[1])
            v = v.split(',')
            vx = int(v[0].split('=')[1])
            vy = int(v[1])
            bots[i] = {'p': (x, y), 'v': (vx, vy)}
        # set size of table wide long
        Y = 103  # 7  #
        X = 101  # 11  #
        # how many "seconds/steps"
        steps = 100
        matrix = [['.' for _ in range(X)] for _ in range(Y)]  # all 0s
        MAX_Y = len(matrix)
        MAX_X = len(matrix[0])

        bots_pos = {}

        for bot in bots.values():
            x, y = bot['p']
            matrix[y][x] = '#'

        for i in range(100000000000000000):
            # INSPECT HERE :)
            # find casese where >= 15 connected pieces and print those (adj list))
            print(f"NOW PRINTING STEP {i} \n")
            if has_large_connected_components(matrix, bots, 20):
                for row in matrix:
                    print("".join(row))
                import time
                time.sleep(3)
            # if i >= 7200:
            #     print(f"NOW PRINTING STEP {i} \n")
            #     for row in matrix:
            #         print("".join(row))
            #     import time
            #     time.sleep(0.1)
            for w in bots.keys():
                bot = bots[w]
                x, y = bot['p']
                dx, dy = bot['v']
                # move it.
                new_x, new_y = x + dx, y + dy
                if new_x < 0 or new_y < 0 or new_x >= MAX_X - 1 or new_y >= MAX_Y - 1:
                    # means we need to do delta math on pacman style delta.
                    if new_x < 0:
                        new_x = MAX_X + new_x
                    elif new_x >= MAX_X:
                        new_x = new_x - MAX_X

                    if new_y < 0:
                        new_y = MAX_Y + new_y
                    elif new_y >= MAX_Y:
                        new_y = new_y - MAX_Y

                # remove old pos, add new pos
                matrix[y][x] = '.'

                x, y = new_x, new_y
                matrix[y][x] = '#'  # new spot
                bots[w]['p'] = (x, y)

        for (x, y) in bots_pos.values():  # fill table with where bots are now
            if isinstance(matrix[y][x], int):
                matrix[y][x] += 1
            else:
                matrix[y][x] = 1


# ---------chatgpt below----------#

def create_adjacency_list(matrix, bots):
    # Extract positions from bots into a set
    points = {bot_data['p'] for bot_data in bots.values() if 'p' in bot_data}

    adjacency_list = {}
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    # Directions for adjacency (8 directions: cardinal + diagonal)
    directions = [
        (-1, 0), (1, 0),  # up, down
        (0, -1), (0, 1),  # left, right
        (-1, -1), (-1, 1),  # diagonals
        (1, -1), (1, 1)
    ]

    for x, y in points:
        adjacency_list[(x, y)] = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) in points:
                adjacency_list[(x, y)].append((nx, ny))

    return adjacency_list


def find_connected_components(adjacency_list):
    visited = set()
    components = []

    def dfs(node, component):
        visited.add(node)
        component.append(node)
        for neighbor in adjacency_list.get(node, []):
            if neighbor not in visited:
                dfs(neighbor, component)

    for node in adjacency_list:
        if node not in visited:
            component = []
            dfs(node, component)
            components.append(component)

    return components


def has_large_connected_components(matrix, bots, threshold=10):
    adjacency_list = create_adjacency_list(matrix, bots)
    connected_components = find_connected_components(adjacency_list)
    # Check if any connected component exceeds the threshold size
    for component in connected_components:
        if len(component) > threshold:
            return True
    return False
