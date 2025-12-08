from __future__ import annotations
import logging
from pathlib import Path
from typing import TextIO, List, Union
from termcolor import colored


logger = logging.getLogger(__name__)


class FileManager:
    INPUT_YEAR = "input/{year}/"
    INPUT_DAY = "input/{year}/{day}.txt"
    INPUT_DAY_SAMPLE = "input/{year}/{day}_{sample}_{part}.txt"
    SCRIPT_PATH = "puzzle_solver.{year}.{day}"
    INIT_FILE = "__init__.py"

    @classmethod
    def get_path(cls, template: str, **kwargs) -> Path:
        return Path(template.format(**kwargs))

    @classmethod
    def retrieve(cls, template: str, **kwargs) -> TextIO:
        path_obj = cls.get_path(template, **kwargs)
        if not path_obj.exists():
            raise FileNotFoundError(
                f"File not found and could not be auto-created: {path_obj}"
            )
        return path_obj.open("r")

    @classmethod
    def read_input_file(cls, template: str, **kwargs) -> Union[str, List[str]]:
        year = kwargs["year"]
        input_dir = Path("input") / str(year)
        cls.create_directory(input_dir)

        file_path = cls.get_path(
            template, **{k: v for k, v in kwargs.items() if k != "method"}
        )
        if not file_path.exists():
            cls.generate_text(file_path, "")
            logger.info(f"Auto-created: {file_path}")

        with cls.retrieve(template, **kwargs) as file:
            if kwargs["method"] == "display_raw":
                return file.read()
            if kwargs["method"] == "solve":
                return [line.rstrip("\n") for line in file]

    @classmethod
    def create_directory(cls, dir_name: Union[str, Path]) -> None:
        dir_path = Path(dir_name)
        dir_path.mkdir(parents=True, exist_ok=True)

        init_path = dir_path / cls.INIT_FILE
        if not init_path.exists():
            init_path.write_text("")
            logger.debug(f"Created __init__.py in {dir_path}")

    @classmethod
    def generate_text(cls, path: Union[str, Path], text: str) -> None:
        file_path = Path(path)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(text)
        logger.debug(f"Generated file: {file_path}")
