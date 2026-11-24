from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class FSxCreateAggregateConfiguration(BaseModel):
    Aggregates: list[StrictStr] | None = None
    ConstituentsPerAggregate: StrictInt | None = None
