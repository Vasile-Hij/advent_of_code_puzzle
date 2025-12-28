title = "Day 1: Secret Entrance"


class PuzzleSolver:
    @classmethod
    def helper(cls, puzzle_input):
        return tuple((elem[0], int(elem[1:])) for elem in puzzle_input)

    @classmethod
    def part_a(cls, puzzle_input):
        puzzle_input = cls.helper(puzzle_input)
        counter = 0
        indicator = 50
        limit = 100  # range(0, 99)

        for direction, moves in puzzle_input:
            if indicator == 0:
                counter += 1
            if direction == "R":
                indicator = (indicator + moves) % limit
            else:
                indicator = (indicator - moves) % limit
        return counter

    @classmethod
    def part_b(cls, puzzle_input):
        puzzle_input = cls.helper(puzzle_input)
        counter = 0
        indicator = 50
        limit = 100

        for direction, moves in puzzle_input:
            if direction == "R":
                counter += (indicator + moves) // limit
                indicator = (indicator + moves) % limit
            else:
                new_indicator = (indicator - moves) % limit

                if indicator == 0:
                    counter += moves // limit
                elif moves > indicator:
                    counter += ((moves - indicator - 1) // limit) + 1
                    if new_indicator == 0:
                        counter += 1
                elif moves == indicator:
                    counter += 1

                indicator = new_indicator

        return counter
