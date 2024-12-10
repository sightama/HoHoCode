from collections import deque, defaultdict


class AdventCode:

    @staticmethod
    def part1(inn: str):
        final = 0
        inn = inn.strip()
        lines = inn.split('\n')
        for line in lines:
            result = 0
            breakaway = line.split('|')
            winning, cards = breakaway[0], breakaway[1].strip()
            winning = winning.split(':')[1].strip()
            winning = winning.strip().split(' ')
            winning = [x.strip() for x in winning if x != ""]
            cards = cards.split(' ')
            cards = [x.strip() for x in cards if x != ""]
            for card in cards:
                if card in winning:
                    if result:
                        result *= 2
                    else:
                        result = 1
            final += result
        return final

    @staticmethod
    def part2(inn: str):
        counter = 1
        card_map = defaultdict(int)
        card_map[1] = 1
        inn = inn.strip()
        lines = inn.split('\n')
        for line in lines:
            breakaway = line.split('|')
            winning, cards = breakaway[0], breakaway[1].strip()
            winning = winning.split(':')[1].strip()
            winning = winning.strip().split(' ')
            winning = [x.strip() for x in winning if x != ""]
            cards = cards.split(' ')
            cards = [x.strip() for x in cards if x != ""]

            if counter not in card_map:
                card_map[counter] = 1
            for i in range(card_map[counter]):
                matching = 0
                for card in cards:
                    if card in winning:
                        matching += 1

                for j in range(1, matching + 1):
                    next_num = j + counter
                    if next_num in card_map:
                        card_map[next_num] += 1
                    else:
                        card_map[next_num] = 2

            counter += 1

        return sum(card_map.values())
