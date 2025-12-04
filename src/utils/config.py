from __future__ import annotations  # Enables postponed evaluation of annotations
from enum import Enum
from pathlib import Path
from typing import TextIO


class ProjectPaths(Enum):
    INPUT_YEAR = "input/{year}/"
    INPUT_DAY = "input/{year}/day{day}.txt"
    INPUT_DAY_SAMPLE = "input/{year}/day{day}_{sample}_{part}.txt"
    SCRIPT_EXAMPLE = "py/script_example.txt"

    def path(self, **kwargs) -> Path:
        return Path(self.value.format(**kwargs))

    def retrieve(self, **kwargs) -> TextIO:
        path = self.path(**kwargs)
        if not path.exists():
            raise FileNotFoundError(f"Missing input file: {path}")
        return path.open("r")

    @classmethod
    def get_content(cls, path_enum: ProjectPaths, **kwargs) -> str:
        with path_enum.retrieve(**kwargs) as file:
            return file.read()
