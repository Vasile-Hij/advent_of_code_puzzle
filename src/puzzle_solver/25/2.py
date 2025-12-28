import math

title = "Day 2: Gift Shop "


class PuzzleSolver:
    @classmethod
    def helper(cls, puzzle_input, func):
        puzzle_input = next(elem.split(",") for elem in puzzle_input)
        total = 0

        for string in puzzle_input:
            start, end = int(string.split("-")[0]), int(string.split("-")[1])
            for number in range(start, end + 1):
                if func(number):
                    total += number

        return total

    @classmethod
    def part_a(cls, number):
        def verify_two_half_numbers(number):
            digit_count = math.floor(math.log10(number)) + 1 if number > 0 else 1

            if digit_count % 2 != 0:
                return False

            string = str(number)
            mid = digit_count // 2
            return string[:mid] == string[mid:]

        return cls.helper(number, verify_two_half_numbers)

    @classmethod
    def part_b(cls, number):
        def verify_all_numbers(number):
            string = str(number)
            length = len(string)

            for index in range(1, length):
                if length % index == 0:
                    repetitions = length // index
                    if repetitions >= 2:
                        pattern = string[:index]
                        if pattern * repetitions == string:
                            return True
            return False

        return cls.helper(number, verify_all_numbers)
