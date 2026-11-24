from typing import Any
from pydantic import BaseModel, Field, StrictStr
from .match_option_types import MatchOptionTypes


class TagValue(BaseModel):
    Key: StrictStr | None = Field(default=None, pattern=r'[\S\s]*')
    MatchOptions: list[MatchOptionTypes] | None = None
    Values: list[StrictStr] | None = None

    def dump(self) -> dict[str, Any]:
        return self.model_dump(exclude_none=True)
