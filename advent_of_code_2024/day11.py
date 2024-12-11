from collections import deque, defaultdict

DAY = 11


class AdventCode:
    stones = defaultdict(int)
    seen = {}

    def part1(self, inn: str):
        blink = 25
        stones = inn.split(' ')
        stones = [int(x) for x in stones]
        for x in range(blink):
            print(f"Now processing my {x}th BLINK")
            queue = deque(stones)
            new_queue = deque()
            while queue:
                current = queue.popleft()
                if current in self.seen:
                    new_queue.extend(self.seen[current])
                else:
                    new_stones = self.stone_analyze(current)
                    self.seen[current] = new_stones
                    new_queue.extend(new_stones)

            stones = new_queue

        return len(stones)

    @staticmethod
    def stone_analyze(stone: int):
        if stone == 0:
            return [1]
        str_stone = str(stone)
        if len(list(str_stone)) % 2 == 0:
            a, b = str_stone[:len(str_stone) // 2], str_stone[len(str_stone) // 2:]  # i googled this one lol
            a, b = int(a), int(b)
            return [a, b]

        return [stone * 2024]

    def part2(self, inn: str):
        blinks = 75
        stones = inn.split(' ')
        stones = [int(x) for x in stones]

        # get list to dict initial...
        new_stones = defaultdict(int)
        for stone in stones:
            new_stones[stone] += 1
        for _ in range(blinks):
            stones = new_stones
            new_stones = defaultdict(int)
            for current, count in stones.items():
                # determine in any blink for all stones out of order in dict, the enext layer  of stones and counts.
                if current in self.seen:
                    future_stones = self.seen[current]
                else:
                    future_stones = self.stone_analyze(current)
                    self.seen[current] = future_stones

                for x in future_stones:
                    new_stones[x] += count

        return sum(new_stones.values())
