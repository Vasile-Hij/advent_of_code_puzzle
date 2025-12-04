import argparse
import logging
from termcolor import colored
from utils.config import ProjectPaths
from utils.pydantic_model import LineInput

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    _help = """
            1. Year 2025, day 01, part a: "-id 2501 -p a", second part: "-id 2502 -p b"
            2. For sample day test add "-s s".

            Run e.g.: "python3 main.py -id 2501 -p a -s s"
           """

    class Command:
        def cmd_arguments(self):
            parser = argparse.ArgumentParser(description="Run Advent of Code solution.")
            parser.add_argument("--script_id", "-id", type=int, help=_help)
            parser.add_argument("--part", "-p", type=str, help=_help)
            parser.add_argument("--sample", "-s", type=str, help=_help)
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

            if sample:
                input_file = ProjectPaths.get_content(
                    ProjectPaths.INPUT_DAY_SAMPLE,
                    year=year,
                    day=day,
                    sample=sample,
                    part=part,
                )
            else:
                input_file = ProjectPaths.get_content(ProjectPaths.INPUT_DAY, year=year, day=day)

            print(input_file)


Command().run()
