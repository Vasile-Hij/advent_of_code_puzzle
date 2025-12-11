import argparse
import logging
import sys
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
        parser.add_argument("--results", "-r", type=int, help=HELP_TEXT)
        args = parser.parse_args()

        return {
            "script_id": args.script_id,
            "part": args.part,
            "sample": args.sample,
            "results": args.results,
        }

    def run(self):
        cmds = self.cmd_arguments()
        cmds_obj = LineInput(**cmds)

        year, day = cmds_obj.year, cmds_obj.day
        part = cmds_obj.part
        sample = cmds_obj.sample
        need_results = cmds_obj.results

        if need_results:
            print(f"Printing results: {self.save_results(year, day)}")
            sys.exit("Success")

        self.display_input(year, day, sample, part)
        self.display_solved(year, day, sample, part)

    def display_input(self, year, day, sample, part):
        if sample:
            text = self.get_input(year, day, sample, part, method="display_raw_sample")
        else:
            text = self.get_input(
                year, day, sample, part, method="display_raw_input_trim"
            )

        print("-->")
        print(colored(text, "green"))
        print("<--")

    def display_solved(self, year, day, sample, part):
        result = self.get_solved(year, day, sample, part)
        print(colored(f"Result: {result}", "blue"))

    def get_input(self, year, day, sample, part, method):
        file_manager = FileManager
        kwargs = {"year": year, "day": day, "method": method}

        if sample:
            kwargs.update({"sample": sample, "part": part})
            return file_manager.read_input_file(file_manager.INPUT_DAY_SAMPLE, **kwargs)
        else:
            return file_manager.read_input_file(file_manager.INPUT_DAY, **kwargs)

    def get_solved(self, year, day, sample, part):
        input_file = self.get_input(year, day, sample, part, method="solve")
        return Solver.get_result(input_file, year, day, part)

    def save_results(self, year, day):
        results = FileManager.get_json()

        year = str(year)
        day = str(day)

        if year not in results:
            results[year] = {}
        if str(day) not in results[year]:
            results[year][day] = {}

        day_data = results[year][day]
        for sample, part in [("s", "a"), ("s", "b"), (None, "a"), (None, "b")]:
            key = f"{'sample' if sample else 'input'}_{part}"
            day_data[key] = self.get_solved(year, day, sample, part)

        FileManager.save_json(results)
        return results


if __name__ == "__main__":
    Command().run()
