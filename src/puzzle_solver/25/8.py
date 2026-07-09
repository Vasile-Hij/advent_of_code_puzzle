import heapq
import math
from itertools import combinations

title = "--- Day 8: Playground ---"


class PuzzleSolver:
    @staticmethod
    def helper(puzzle_input):
        return [tuple(int(num) for num in line.split(",")) for line in puzzle_input]

    @classmethod
    def part_a(cls, puzzle_input, rows=1000, num=3):
        boxes = cls.helper(puzzle_input)
        electrical_circuits = cls.greedy_connect(boxes, rows).values()
        return math.prod(heapq.nlargest(num, map(len, set(electrical_circuits))))

    @classmethod
    def greedy_connect(cls, boxes, rows):
        circuits = {B: (B,) for B in boxes}
        for A, B in cls.closest_pairs(boxes, rows):
            if circuits[A] != circuits[B]:
                new_circuit = circuits[A] + circuits[B]
                for circuit in new_circuit:
                    circuits[circuit] = new_circuit
        return circuits

    @classmethod
    def closest_pairs(cls, points, rows):
        pairs = combinations(points, 2)
        return heapq.nsmallest(
            rows, pairs, key=lambda link: cls.distance_squared(*link)
        )

    @staticmethod
    def distance_squared(X, Y):
        return (X[0] - Y[0]) ** 2 + (X[1] - Y[1]) ** 2 + (X[2] - Y[2]) ** 2

    @classmethod
    def part_b(cls, puzzle_input):
        boxes = cls.helper(puzzle_input)
        return math.prod(cls.first_points(cls.last_connection(boxes, rows=1000)))

    @staticmethod
    def first_points(points):
        return tuple(point[0] for point in points)

    @classmethod
    def last_connection(cls, boxes, rows):
        circuits = {B: [B] for B in boxes}
        for A, B in cls.closest_pairs(boxes, rows):
            if circuits[A] is not circuits[B]:
                new_circuit = circuits[A] + circuits[B]
                if len(new_circuit) == len(boxes):
                    return (A, B)
                for circuit in new_circuit:
                    circuits[circuit] = new_circuit
        return cls.last_connection(boxes, 2 * rows)
