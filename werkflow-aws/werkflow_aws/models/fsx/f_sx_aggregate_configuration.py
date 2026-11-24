from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class FSxAggregateConfiguration(BaseModel):
    Aggregates: list[StrictStr] | None = None
    TotalConstituents: StrictInt | None = None
