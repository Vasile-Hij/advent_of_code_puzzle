import argparse
import logging
from termcolor import colored
from utils.config import FileManager
from utils.solver import Solver
from utils.pydantic_model import LineInput

logger = logging.getLogger(__name__)

HELP_TEXT = """
1. Year 2025, day 01, part a: "-id 2501 -p a", second part: "-id 2502 -p b"
2. For sample day test add "-s s".
Run e.g.: "python3 main.py -id 2501 -p a -s s"
"""


class Command:
    def cmd_arguments(self):
        parser = argparse.ArgumentParser(description="Run Advent of Code solution.")
        parser.add_argument("--script_id", "-id", type=int, help=HELP_TEXT)
        parser.add_argument("--part", "-p", type=str, help=HELP_TEXT)
        parser.add_argument("--sample", "-s", type=str, help=HELP_TEXT)
        args = parser.parse_args()

        return {
            "script_id": args.script_id,
            "part": args.part,
            "sample": args.sample,
        }

    def run(self):
        cmds = self.cmd_arguments()
        cmds_obj = LineInput(**cmds)

        year, day = cmds_obj.year, cmds_obj.day
        part = cmds_obj.part
        sample = cmds_obj.sample
        self.display_input(year, day, sample, part)
        self.display_solved(year, day, sample, part)

    def display_input(self, year, day, sample, part):
        text = self.get_input(year, day, sample, part, method="display_raw")

        print("-->")
        print(colored(text, "green"))
        print("<--")

    def display_solved(self, year, day, sample, part):
        input_file = self.get_input(year, day, sample, part, method="solve")
        result = Solver.get_result(input_file, year, day, part)
        print(colored(f"Result: {result}", "blue"))

    def get_input(self, year, day, sample, part, method):
        file_manager = FileManager
        kwargs = {"year": year, "day": day, "method": method}

        if sample:
            kwargs.update({"sample": sample, "part": part})
            return file_manager.read_input_file(file_manager.INPUT_DAY_SAMPLE, **kwargs)
        else:
            return file_manager.read_input_file(file_manager.INPUT_DAY, **kwargs)


if __name__ == "__main__":
    Command().run()
