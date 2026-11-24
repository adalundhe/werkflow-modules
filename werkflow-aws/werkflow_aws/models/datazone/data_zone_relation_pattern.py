from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt


class DataZoneRelationPattern(BaseModel):
    relationType: Literal['LINEAGE']
    relationDirection: Literal['IN', 'OUT']
    maxPathLength: StrictInt | None = None
