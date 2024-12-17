from collections import deque, defaultdict, Counter
from copy import deepcopy

DAY = 12

 # NOTE: Giving up for now....it works on ALL 3 SAMPLE CASES, idk what the edge case is where it doesnt work but here we are....

class AdventCode:
    perimeter = defaultdict(list)
    regions = {}
    matrix = []

    def build_matrix(self, inn: str):
        matrix = inn.split('\n')
        matrix = [list(x) for x in matrix]
        return matrix

    def part1(self, inn: str):
        # total up all counts of all things in the map. This is the AREA
        letters = dict(Counter(inn))  # ....lmfao this doesnt work. its per region area not all lettesr...
        del letters['\n']
        matrix = self.build_matrix(inn)
        self.matrix = matrix
        for x in letters:
            # find all regions for a given letter, and then calculate perimter
            self.find_region(matrix, x)
            self.find_perimeter(matrix, x)
        # finally calculate perimeter * area for all and sum.
        total = 0
        for letter in letters:
            for perimeter, pts_n_area in zip(self.perimeter[letter], self.regions[letter]):
                pts, ar = pts_n_area  # in order
                fence_pricing = ar * perimeter
                total += fence_pricing
        return total

    def find_perimeter(self, matrix, letter, skip_inner: bool = False):
        # get largest corner piece and make everything slightly bigger - new matrix with just region and periods.
        for region, _ in self.regions[letter]:
            total_letter_perimeter = 0
            largest_y = 0
            largest_x = 0
            smallest_x = 1e99
            smallest_x_y = None
            smallest_y = 1e99
            for x, y in region:
                if x > largest_x:
                    largest_x = x
                if y > largest_y:
                    largest_y = y
                if x < smallest_x:
                    smallest_x = x
                    smallest_x_y = y
                if y < smallest_y:
                    smallest_y = y
                #  add + 2 to both y and z s.t. lil man can walk around perim.
            tmp_mat = [['.' for _ in range(largest_x - smallest_x + 3)] for _ in
                       range(largest_y - smallest_y + 3)]  # make matrix + 3 bigger each side for walker
            # populate temp map
            for x, y in region:
                tmp_mat[y - smallest_y + 1][x - smallest_x + 1] = letter
            # for y in range(len(self.matrix)):
            #     for x in range(len(self.matrix[0])):
            #         if y < 0 or x < 0 or y >= len(tmp_mat) or x >= len(tmp_mat[0]):
            #             continue  # outofbounds, otherwise add actual values....
            #         tmp_mat[y + 1][x + 1] = matrix[y][x]

            # let lil man walk around now. start at first spot in deque
            delta = {'u': (0, -1), 'd': (0, 1), 'l': (-1, 0), 'r': (1, 0)}
            switch = {'u': 'r', 'r': 'd', 'd': 'l', 'l': 'u'}
            start_x, start_y = next(iter(region))  # we pivoted region +1, so walk around from here...
            start_x = 0
            start_y = smallest_x_y - smallest_y + 1  # just start one off of random node in region.
            queue = deque([(start_x, start_y, 'u')])
            while queue:
                x, y, direction = queue.popleft()
                if tmp_mat[y][x] == '#' and (x, y) == (start_x, start_y):
                    break  # we've reached out backend of path!
                if tmp_mat[y][x] != letter:
                    tmp_mat[y][x] = '#'

                # check if surrounded by 3 elements, if so turn around. see I, (4,9)
                u_x, u_y = delta[direction]
                u_x, u_y = u_x + x, u_y + y
                side_x, side_y = delta[switch[direction]]
                side_x, side_y = side_x + x, side_y + y
                o_side_x, o_side_y = delta[switch[switch[switch[direction]]]]
                o_side_x, o_side_y = o_side_x + x, o_side_y + y
                if not (u_x < 0 or u_y < 0 or side_x < 0 or side_y < 0 or o_side_x < 0 or o_side_y < 0 or o_side_y >= len(tmp_mat)-1 or side_y >= len(tmp_mat)-1 or u_y >= len(tmp_mat)-1 or o_side_x >= len(tmp_mat[0])-1 or side_x >= len(tmp_mat[0])-1 or u_x >= len(tmp_mat[0])-1):
                    if tmp_mat[o_side_y][o_side_x] == letter and tmp_mat[side_y][side_x] == letter and tmp_mat[u_y][u_x] == letter:
                        # in a CORNER. turn the fuck around. u -> d
                        direction = switch[switch[direction]]
                        total_letter_perimeter += 2  # we turn around so we add + 2 for the turn aroudn edges


                # check that right most element is out letter
                side_x, side_y = delta[switch[direction]]
                right_x, right_y = side_x + x, side_y + y
                if tmp_mat[right_y][right_x] == letter:
                    # keep going same direction - ALSO MAKE SURE ELEMENT INFRONT IS NOT IT.
                    dx, dy = delta[direction]
                    new_x, new_y = dx + x, dy + y
                    if tmp_mat[new_y][new_x] == letter:
                        # this means we hit an L bend in the region. Instead do inverse of right guy
                        direction = switch[switch[switch[direction]]]  # ie if going d and normally right, go l.
                        total_letter_perimeter += 1  # concave edge, add two instead ;)
                        dx, dy = delta[direction]
                        new_x, new_y = dx + x, dy + y

                    queue.append((new_x, new_y, direction))
                    total_letter_perimeter += 1
                else:
                    # that means switch direction and iterate - decide which direction
                    direction = switch[direction]  # ie r
                    dx, dy = delta[direction]
                    new_x, new_y = dx + x, dy + y
                    if tmp_mat[new_y][new_x] == letter:  # means we hit our letter so there is a turn opposite.
                        other_direction = switch[switch[direction]]  # ie l
                        dx, dy = delta[other_direction]
                        new_x, new_y = dx + x, dy + y
                    queue.append((new_x, new_y, direction))

            if not skip_inner:
                # now inverse the array to see final edges if there is concave edges inside region...
                tmp_set_region = set()
                for y in range(len(tmp_mat)):
                    for x in range(len(tmp_mat[0])):
                        if tmp_mat[y][x] in [letter, '#']:
                            tmp_mat[y][x] = 0
                        else:  # this is internal hole in region for a different region(s)
                            for d, (dx, dy) in delta.items():
                                new_x, new_y = dx + x, dy + y
                                if new_y < 0 or new_x < 0 or y >= len(tmp_mat) - 1 or x >= len(tmp_mat[0]) - 1:
                                    continue  # outofbounds
                                if tmp_mat[new_y][new_x] == letter:
                                    tmp_set_region.add((x, y))
                                    tmp_mat[y][x] = 1
                                    break
                            else:
                                tmp_mat[y][x] = 0
                if any(tmp_mat[y][x] == 1 for x in range(len(tmp_mat[0])) for y in range(len(tmp_mat))):
                    # there is inner edges. recurse once.
                    # make subregions based on if they are next to each other
                    connected_sets = get_connected_sets(tmp_set_region)
                    for r in connected_sets:
                        self.regions[1] = [(r, len(r))]  # ok to overwrite, this is per each letter needed.
                        matt = deepcopy(tmp_mat)
                        inner_edges = self.find_perimeter(matt, 1, True)
                        total_letter_perimeter += inner_edges
            self.perimeter[letter].append(total_letter_perimeter)
        return total_letter_perimeter  # only used for subregioning

    def find_region(self, matrix, letter):
        visited = set()
        self.regions[letter] = []
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                node = matrix[y][x]
                if letter == node and (x, y) not in visited:  # new region
                    # start in one direction, when we reach same node that is full perimeter
                    newly_visited = self.explore(matrix, x, y, set())
                    self.regions[letter].append(
                        (newly_visited, len(newly_visited)))  # LENGTH HERE IS AREA OF REGION WEE
                    visited = visited | newly_visited

    def explore(self, matrix, x, y, visited):
        visited.add((x, y))
        delta = {'u': (0, -1), 'd': (0, 1), 'l': (-1, 0), 'r': (1, 0)}
        for direct, (dx, dy) in delta.items():
            new_x, new_y = dx + x, dy + y
            if new_x < 0 or new_y < 0 or new_x >= len(matrix[0]) or new_y >= len(matrix):
                # outofbounds
                continue
            if matrix[y][x] == matrix[new_y][new_x] and (new_x, new_y) not in visited:
                # another piece of a "region", attached to it.
                visited = visited | self.explore(matrix, new_x, new_y, visited)

        return visited


# below is gpt, im lazy get over it
def get_neighbors(point, point_set):
    # List of possible directions (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = set()

    for dx, dy in directions:
        neighbor = (point[0] + dx, point[1] + dy)
        if neighbor in point_set:
            neighbors.add(neighbor)

    return neighbors


def get_connected_sets(point_set):
    visited = set()  # To keep track of visited points
    connected_sets = []

    for point in point_set:
        if point not in visited:
            # Start a new group with this point
            stack = [point]
            current_group = set()

            while stack:
                current_point = stack.pop()
                if current_point not in visited:
                    visited.add(current_point)
                    current_group.add(current_point)

                    # Add neighbors to the stack
                    neighbors = get_neighbors(current_point, point_set)
                    for neighbor in neighbors:
                        if neighbor not in visited:
                            stack.append(neighbor)

            # Add the group to the list of connected sets
            connected_sets.append(current_group)

    return connected_sets
