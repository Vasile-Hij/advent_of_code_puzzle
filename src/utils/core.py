import logging
from collections import abc

logger = logging.getLogger(__name__)


class Matrix2D(dict):
    cardinal_directions = East, South, West, North = ((1, 0), (0, 1), (-1, 0), (0, -1))
    orthogonal_directions = SE, NE, SW, NW = ((1, 1), (1, -1), (-1, 1), (-1, -1))
    axis_directions = cardinal_directions + orthogonal_directions

    def __init__(self, grid=(), directions=None, skip=(), default=KeyError):
        super().__init__()
        self.directions = directions
        self.default = default

        if isinstance(grid, abc.Mapping):
            self.update(grid)
        else:
            if isinstance(grid, str):
                grid = grid.splitlines()
            self.update(
                {
                    (x, y): value
                    for y, row in enumerate(grid)
                    for x, value in enumerate(row)
                    if value not in skip
                }
            )


class SolverBase:
    matrix_2d = Matrix2D
