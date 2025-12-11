from __future__ import annotations
import json
import logging
from pathlib import Path
from typing import Literal, TextIO, List, Union


logger = logging.getLogger(__name__)


class FileManager:
    INPUT_YEAR = "input/{year}/"
    INPUT_DAY = "input/{year}/{day}.txt"
    INPUT_DAY_SAMPLE = "input/{year}/{day}_{sample}_{part}.txt"
    SCRIPT_PATH = "puzzle_solver.{year}.{day}"
    INIT_FILE = "__init__.py"
    RESULTS = "puzzle_solved/results.json"

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
    def read_input_file(cls, template: str, **kwargs):
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
            method: Literal["display_raw_sample", "display_raw_input_trim", "solve"] = (
                kwargs["method"]
            )
            match method:
                case "display_raw_sample":
                    return file.read()

                case "display_raw_input_trim":
                    lines = []
                    for _ in range(10):
                        try:
                            lines.append(next(file).rstrip())
                        except StopIteration:
                            break
                    return f"{'\n'.join(lines)}\n..."

                case "solve":
                    return tuple(line.rstrip("\n") for line in file)

                case _:
                    raise ValueError(f"Unknown method: {method}")

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

    @classmethod
    def get_json(cls) -> dict:
        path = Path(cls.RESULTS)
        if path.exists():
            with Path.open(path, "r") as f:
                return json.load(f)
        return {}

    @classmethod
    def save_json(cls, data: dict):
        path = Path(cls.RESULTS).parent
        path.mkdir(parents=True, exist_ok=True)
        with Path.open(cls.RESULTS, "w") as f:
            json.dump(data, f, indent=2)
