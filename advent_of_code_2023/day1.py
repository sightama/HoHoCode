from collections import deque


test_input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""


class AdventCode:

    num_map = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
                "six": 6, "seven": 7, "eight": 8, "nine": 9}

    @staticmethod
    def dayone(cd: str):
        cd = cd.strip()
        calibrate_lines = cd.split('\n')
        all_nums = []
        for line in calibrate_lines:
            left = 0
            right = len(line) - 1
            left_val, right_val = None, None
            while left_val is None or right_val is None:
                if not left_val:
                    if line[left].isdigit():
                        left_val = line[left]
                    else:
                        left += 1
                if not right_val:
                    if line[right].isdigit():
                        right_val = line[right]
                    else:
                        right -= 1

            all_nums.append(int(left_val + right_val))
        return sum(all_nums)

    def dayoneparttwo(self, cd: str):
        cd = cd.strip()
        calibrate_lines = cd.split('\n')
        all_nums = []
        words = sorted(list(self.num_map.keys()), key=len)
        words = [(word, len(word)) for word in words]
        for line in calibrate_lines:
            ll, lr = 0, 0
            rr, rl = len(line) - 1, len(line) - 1
            left_val, right_val = None, None
            while left_val is None or right_val is None:
                if not left_val:
                    if line[ll].isdigit():
                        left_val = line[ll]
                    else:
                        # here we check sliding window cases
                        for word, length in words:
                            lr = ll + length
                            if lr < len(line) and ll < len(line):
                                capture = line[ll:lr]
                                if word == capture:
                                    left_val = word
                                    break
                        ll += 1
                if not right_val:
                    if line[rr].isdigit():
                        right_val = line[rr]
                    else:
                        # here we check sliding window cases
                        for word, length in words:
                            rl = rr + 1 - length
                            if rl >= 0 and rr >= 0:
                                capture = line[rl:rr + 1]
                                if word == capture:
                                    right_val = word
                                    break
                        rr -= 1

            all_nums.append(int(self.coerce_nums(left_val) + self.coerce_nums(right_val)))
        return sum(all_nums)

    def coerce_nums(self, val):
        if val in self.num_map:
            return str(self.num_map[val])
        else:
            return val
