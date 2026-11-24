from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneTermRelations(BaseModel):
    isA: list[StrictStr] | None = None
    classifies: list[StrictStr] | None = None
