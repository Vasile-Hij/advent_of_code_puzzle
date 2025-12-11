from __future__ import annotations
from pathlib import Path
from importlib import import_module
from termcolor import colored
import logging

from utils.aoc_config import SCRIPT_TEXT
from utils.config import FileManager

logger = logging.getLogger(__name__)


class Solver:
    file_manager = FileManager

    @classmethod
    def get_script(cls, year: int, day: int):
        module_path = cls.file_manager.SCRIPT_PATH.format(year=year, day=day)

        try:
            return import_module(module_path)
        except (ModuleNotFoundError, ImportError) as e:
            logger.warning(f"Module {module_path} not found, creating template: {e}")

            script_dir = Path("puzzle_solver") / str(year)
            cls.file_manager.create_directory(script_dir)  # pyright: ignore[reportAttributeAccessIssue]

            script_file = script_dir / f"{day}.py"
            FileManager.generate_text(script_file, SCRIPT_TEXT)
            logger.info(
                colored("New script was successfully populated!", "magenta", "on_black")
            )

            return import_module(module_path)

    @staticmethod
    def get_result(input_file, year, day, part):
        script = Solver.get_script(year, day)

        if hasattr(script, "PuzzleSolver"):
            solver_class = script.PuzzleSolver

            if part == "a":
                return solver_class.part_a(input_file)
            elif part == "b":
                return solver_class.part_b(input_file)
            else:
                logger.error(f"Invalid part: {part}")
                return None
        else:
            logger.error(f'Script for {year}/day{day} missing "PuzzleSolver" class')
            return None
