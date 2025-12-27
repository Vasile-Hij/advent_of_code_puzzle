from typing import Any, Optional
from pydantic import (
    BaseModel,
    Field,
    StrictBool,
    field_validator,
    StrictStr,
    StrictInt,
    model_validator,
)

from utils import aoc_config

ALLOWED_PATTERNS = {
    ("id", "p"),  # -id 2025 -p a
    ("id", "p", "s"),  # -id 2025 -p a -s s
    ("id", "r"),  # -id 2025 -r 1
}


class LineInput(BaseModel):
    script_id: StrictInt
    part: StrictStr | None = None
    sample: StrictStr | None
    results: Optional[int] = None

    @field_validator("script_id", mode="before")
    @classmethod
    def validate_script_id(cls, value: int) -> StrictInt:
        if not value or len(str(value)) != 4:
            raise ValueError(
                f'{value=} is not accepted! Try something like: "-id 2501"'
            )
        value = int(value)

        year = value // 100
        days = value % 100

        if not (int(aoc_config.START_YEAR) <= year <= int(aoc_config.CURRENT_YEAR)):
            raise ValueError(
                f"{year=} must be between {aoc_config.START_YEAR}-{aoc_config.CURRENT_YEAR}!"
            )
        if not (1 <= days <= int(aoc_config.OLD_DAYS)) and (
            int(aoc_config.CURRENT_YEAR) < int(aoc_config.YEAR_CHANGED)
        ):
            raise ValueError(f"{days=} are not accepted, between 1 and 25 only!")

        if not (1 <= days <= int(aoc_config.NEW_DAYS)) and (
            int(aoc_config.CURRENT_YEAR) > int(aoc_config.YEAR_CHANGED)
        ):
            raise ValueError(f"{days=} are not accepted, between 1 and 15 only!")

        return value

    @field_validator("part", mode="before")
    @classmethod
    def validate_part(cls, value: Any) -> Optional[StrictStr]:
        if value is None:
            return None

        if value not in ("a", "b"):
            raise ValueError('Last character must be either "a" or "b"')
        return value

    @field_validator("sample", mode="before")
    @classmethod
    def validate_sample(cls, value: Optional[str]) -> Optional[StrictStr]:
        if value is not None and value != "s":
            raise ValueError('Sample should be "s"')
        return "sample" if value == "s" else None

    @field_validator("results", mode="before")
    @classmethod
    def validate_results(cls, value: Any) -> bool:
        if value is None:
            return False

        if isinstance(value, int) and value == 1:
            return True

        raise ValueError(f"{value} is not accepted, only -r 1")

    @property
    def year(self) -> int:
        return self.script_id // 100

    @property
    def day(self) -> int:
        return self.script_id % 100

    @model_validator(mode="after")
    def check_pattern(self):
        if self.part and self.results == 1:
            raise ValueError(f"{ALLOWED_PATTERNS=} only")

        return self
