from __future__ import annotations
from pydantic import BaseModel, StrictInt


class PrioritySchemeChangesWithoutMappings(BaseModel):
    ids: list[StrictInt] | None = None
