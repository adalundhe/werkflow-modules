from pydantic import BaseModel, StrictStr, Field
from .match_option_types import MatchOptionTypes


class TagValue(BaseModel):
    Key: StrictStr = Field(pattern=r'[\S\s]*')
    MatchOptions: list[MatchOptionTypes]
    Values: list[StrictStr] = Field(pattern=r'[\S\s]*')

    def dump(self):
        return self.model_dump()