from collections import deque

class adventOfCode:
    def dayone(self, calories):
        calories = calories.strip()
        elfs = calories.split('\n')
        queue = deque(elfs)
        max_cals = -1e99
        current_elf = 0
        while queue:
            current = queue.popleft()
            current = current.strip()

            if not current:
                current_elf = 0
                continue

            current_elf = current_elf + int(current)
            if current_elf > max_cals:
                max_cals = current_elf
        return max_cals

    def dayoneparttwo(self, calories):
        calories = calories.strip()
        elfs = calories.split('\n')
        queue = deque(elfs)
        elf_totals = []
        # max_cals = -1e99
        current_elf = 0
        while queue:
            current = queue.popleft()
            current = current.strip()

            if not current:
                elf_totals.append(current_elf)
                current_elf = 0
                continue

            current_elf = current_elf + int(current)

        elf_totals.sort(reverse=True)
        return elf_totals[0] + elf_totals[1] + elf_totals[2]
        #     if current_elf > max_cals:
        #         max_cals = current_elf
        # return max_cals





if __name__ == "__main__":
    # https://adventofcode.com/2022/day/1
    test = adventOfCode()
    day1_input_test = \
        """
        1000
        2000
        3000
        
        4000
        
        5000
        6000
        
        7000
        8000
        9000
        
        10000
        """

    day1_real_input = "REDACTED"
    # day1 = test.dayone(day1_real_input)
    #print(day1)
    day1_parttwo = test.dayoneparttwo(day1_real_input)
    print(day1_parttwo)
