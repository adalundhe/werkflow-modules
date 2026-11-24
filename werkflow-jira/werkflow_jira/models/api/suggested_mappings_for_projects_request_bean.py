from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SuggestedMappingsForProjectsRequestBean(BaseModel):
    add: list[StrictInt] | None = None
