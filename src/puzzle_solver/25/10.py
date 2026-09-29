from itertools import chain, combinations
from math import inf

title = "--- Day 10: Factory ---"


class PuzzleSolver:
    @staticmethod
    def parse_line(puzzle_input):
        buttons = []
        parts = puzzle_input.split()

        lights = [light == "#" for light in parts[0][1:-1]]

        for part in parts[1:-1]:
            num = part[1:-1].split(",")
            buttons.append([int(n) for n in num])

        return lights, buttons

    @staticmethod
    def press(combo, num_lights):
        on = set()

        for button in combo:
            on ^= set(button)

        return [num in on for num in range(num_lights)]

    @classmethod
    def min_presses(cls, lights, buttons):
        all_combos = chain.from_iterable(
            combinations(buttons, size) for size in range(len(lights) + 1)
        )

        for combo in all_combos:
            if cls.press(combo, len(lights)) == lights:
                return len(combo)
        return inf

    @classmethod
    def part_a(cls, puzzle_input):
        total = 0

        for line in puzzle_input:
            lights, buttons = cls.parse_line(line)
            total += cls.min_presses(lights, buttons)

        return total

    @classmethod
    def part_b(cls, puzzle_input):
        return
