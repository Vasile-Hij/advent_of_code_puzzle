from itertools import combinations

title = "--- Day 9: Movie Theater ---"


Point = tuple[int, ...]
Rectangle = tuple[Point, Point]


class PuzzleSolver:
    @classmethod
    def helper(cls, puzzle_input):
        return [tuple(int(num) for num in line.split(",")) for line in puzzle_input]

    @classmethod
    def surface_area(cls, rectangle: Rectangle):
        (x1, y1), (x2, y2) = rectangle
        dx, dy = abs(x1 - x2), abs(y1 - y2)
        return (dx + 1) * (dy + 1)

    @classmethod
    def part_a(cls, puzzle_input):
        points = cls.helper(puzzle_input)
        return max(map(cls.surface_area, combinations(points, 2)))

    @classmethod
    def part_b(cls, puzzle_input):
        return
