from typing import Any
from pydantic import BaseModel, Field, StrictStr
from .match_option_types import MatchOptionTypes


class CostCategory(BaseModel):
    Key: StrictStr = Field(
        min_length=1,
        max_length=50,
    )
    MatchOptions: list[MatchOptionTypes] | None = None
    Values: list[StrictStr] | None = None

    def dump(self) -> dict[str, Any]:
        return self.model_dump(exclude_none=True)
