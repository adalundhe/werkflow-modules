from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SuggestedMappingsForPrioritiesRequestBean(BaseModel):
    add: list[StrictInt] | None = None
    remove: list[StrictInt] | None = None
