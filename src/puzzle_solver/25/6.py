title = "--- Day 6: Trash Compactor ---"


class PuzzleSolver:
    @classmethod
    def part_a(cls, puzzle_input):
        rows = [row.split() for row in puzzle_input if row.strip()]
        *value_rows, math_row = rows

        total = 0

        for *values, math_sign in zip(*value_rows, math_row):
            nums = list(map(int, values))

            if math_sign == "+":
                total += sum(nums)
            else:
                prod = 1
                for num in nums:
                    prod *= num
                total += prod

        return total

    @classmethod
    def part_b(cls, puzzle_input):
        return
