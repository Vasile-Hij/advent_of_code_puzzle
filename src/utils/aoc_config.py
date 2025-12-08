from datetime import datetime


START_YEAR = 15
CURRENT_YEAR = datetime.now().year % 100

OLD_DAYS = 25
NEW_DAYS = 12

YEAR_CHANGED = (
    25 - 1
)  # in 2025 rules changed from 25 days to 12 days, so 2015-2024 with 25 days


SCRIPT_TEXT = """
from utils import SolverBase

title = ''

class PuzzleSolver(SolverBase):
    @classmethod
    def helper(cls, puzzle_input):
        return

    @classmethod
    def part_a(cls, puzzle_input):
        return

    @classmethod
    def part_b(cls, puzzle_input):
        return
"""
