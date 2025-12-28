from utils.core import SolverBase

title = "--- Day 4: Printing Department ---"


class PuzzleSolver(SolverBase):
    @classmethod
    def get_accessible_positions(cls, grid):
        paper_roll = "@"
        max_allowed = 4

        def is_accessible(position):
            if grid[position] != paper_roll:
                return False

            count_neighbor = 0
            for dx, dy in grid.axis_directions:
                nx, ny = position[0] + dx, position[1] + dy
                if (nx, ny) in grid and grid[(nx, ny)] == paper_roll:
                    count_neighbor += 1

            return count_neighbor < max_allowed

        return [position for position in grid if is_accessible(position)]

    @classmethod
    def part_a(cls, puzzle_input):
        grid = cls.matrix_2d(grid=puzzle_input)
        return len(cls.get_accessible_positions(grid))

    @classmethod
    def part_b(cls, puzzle_input):
        grid = cls.matrix_2d(grid=puzzle_input)
        removed_string = "x"
        total_removed = 0

        while True:
            accessible_positions = cls.get_accessible_positions(grid)
            if not accessible_positions:
                break

            for position in accessible_positions:
                grid[position] = removed_string
                total_removed += 1

        return total_removed
