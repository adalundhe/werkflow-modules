from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt


class SearchAutoCompleteFilter(BaseModel):
    includeCollapsedFields: StrictBool | None = None
    projectIds: list[StrictInt] | None = None
