import math
from utils.core import SolverBase

title = "Day 2: Gift Shop "


class PuzzleSolver(SolverBase):
    @classmethod
    def helper(cls, puzzle_input, func):
        puzzle_input = next(elem.split(",") for elem in puzzle_input)
        numbers = []

        for string in puzzle_input:
            start, end = int(string.split("-")[0]), int(string.split("-")[1])
            for number in range(start, end + 1):
                if func(number):
                    numbers.append(number)

        return sum(numbers)

    @classmethod
    def part_a(cls, puzzle_input):
        def verify_two_numbers(number):
            digit_count = math.floor(math.log10(number)) + 1 if number > 0 else 1

            if digit_count % 2 != 0:
                return False

            string = str(number)
            mid = digit_count // 2

            return string[:mid] == string[mid:]

        return cls.helper(puzzle_input, verify_two_numbers)

    @classmethod
    def part_b(cls, puzzle_input):
        return
