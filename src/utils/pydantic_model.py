from pydantic import (
    BaseModel,
    field_validator,
    StrictStr,
    StrictInt,
)

from utils import aoc_config


class LineInput(BaseModel):
    script_id: StrictInt
    part: StrictStr
    sample: StrictStr | None

    @field_validator("script_id", mode="before")
    @classmethod
    def validate_code(cls, value: str) -> str:
        if not value or len(str(value)) != 4:
            raise ValueError(
                f'{value=} is not accepted! Try something like: "-id 2501"'
            )

        year = value // 100
        days = value % 100

        if not (aoc_config.START_YEAR <= year <= aoc_config.CURRENT_YEAR):
            raise ValueError(
                f"{year=} must be between {aoc_config.START_YEAR}-{aoc_config.CURRENT_YEAR}!"
            )
        if not (1 <= days <= aoc_config.OLD_DAYS) and (
            aoc_config.CURRENT_YEAR < aoc_config.YEAR_CHANGED
        ):
            raise ValueError(f"{days=} are not accepted, between 1 and 25 only!")

        if not (1 <= days <= aoc_config.NEW_DAYS) and (
            aoc_config.CURRENT_YEAR > aoc_config.YEAR_CHANGED
        ):
            raise ValueError(f"{days=} are not accepted, between 1 and 15 only!")

        return value

    @field_validator("part", mode="before")
    @classmethod
    def validate_part(cls, value: str) -> str:
        if value not in ("a", "b"):
            raise ValueError('Last character must be either "a" or "b"')
        return value

    @field_validator("sample", mode="before")
    @classmethod
    def validate_sample(cls, value: str) -> str:
        if value is not None and value != "s":
            raise ValueError('Sample should be "s"')
        return "sample" if value else value

    @property
    def year(self):
        return self.script_id // 100

    @property
    def day(self):
        return self.script_id % 100
