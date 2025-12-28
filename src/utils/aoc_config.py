from datetime import datetime


START_YEAR: int = 15
CURRENT_YEAR: int = datetime.now().year % 100

OLD_DAYS: int = 25
NEW_DAYS: int = 12

# in 2025 rules changed from 25 days to 12 days, so 2015-2024 with 25 days
YEAR_CHANGED: int = 25 - 1


SCRIPT_TEXT: str = """
title = ''

class PuzzleSolver:
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
