from utils.core import SolverBase
from collections import deque

title = "--- Day 3: Lobby ---"


class PuzzleSolver(SolverBase):
    @classmethod
    def helper(cls, puzzle_input):
        return

    @classmethod
    def part_a(cls, puzzle_input):
        total = 0

        for row in puzzle_input:
            digits = deque(int(char) for char in row)
            max_joltage = 0

            while len(digits) >= 2:
                first = digits.popleft()
                for second in digits:
                    joltage = (first * 10) + second
                    max_joltage = max(max_joltage, joltage)

            total += max_joltage
        return total

    @classmethod
    def part_b(cls, puzzle_input):
        def find_max_joltage(row, keep_digits=12):
            number = len(row)
            to_remove = number - keep_digits
            stack = deque()

            for char in row:
                digit = int(char)

                while stack and stack[-1] < digit and to_remove > 0:
                    stack.pop()
                    to_remove -= 1
                stack.append(digit)

            while to_remove > 0:
                stack.pop()
                to_remove -= 1

            return int("".join(map(str, stack)))

        total = 0
        for row in puzzle_input:
            joltage = find_max_joltage(row, keep_digits=12)
            total += joltage
        return total
