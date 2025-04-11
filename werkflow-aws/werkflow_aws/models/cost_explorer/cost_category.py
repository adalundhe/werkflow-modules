from pydantic import BaseModel, StrictStr, Field
from .match_option_types import MatchOptionTypes


class CostCategory(BaseModel):
    Key: StrictStr = Field(
        pattern=r'^(?! )[\p{L}\p{N}\p{Z}-_]*(?<! )$',
        min_length=1,
        max_length=50,
    )
    MatchOptions: MatchOptionTypes
    Values: list[StrictStr] = Field(pattern=r'[\S\s]*')

    def dump(self):
        return self.model_dump()
