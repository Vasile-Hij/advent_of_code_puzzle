from collections import Counter

title = "--- Day 7: Laboratories ---"


class PuzzleSolver:
    @classmethod
    def helper(cls, puzzle_input):
        return puzzle_input[0].index("S")

    @classmethod
    def part_a(cls, puzzle_input):
        starting_point = cls.helper(puzzle_input)
        beams = {starting_point}
        split_counter = 0

        for row in puzzle_input[1:]:
            for beam in list(beams):
                if row[beam] == "^":
                    split_counter += 1
                    beams.remove(beam)
                    beams.update({beam - 1, beam + 1})

        return split_counter

    @classmethod
    def part_b(cls, puzzle_input):
        starting_point = cls.helper(puzzle_input)
        beams = Counter({starting_point})

        for row in puzzle_input[1:]:
            for beam, num in list(beams.items()):
                if row[beam] == "^":
                    beams[beam - 1] += num
                    beams[beam] -= num
                    beams[beam + 1] += num

        return sum(beams.values())
