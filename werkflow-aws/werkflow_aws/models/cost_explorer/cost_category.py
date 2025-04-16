from pydantic import BaseModel, StrictStr, Field
from .match_option_types import MatchOptionTypes


class CostCategory(BaseModel):
    Key: StrictStr = Field(
        min_length=1,
        max_length=50,
    )
    MatchOptions: list[MatchOptionTypes]
    Values: list[StrictStr] = Field(pattern=r'[\S\s]*')

    def dump(self):
        return self.model_dump()
