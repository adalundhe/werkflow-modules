from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueAggregateOperation(BaseModel):
    Column: list[StrictStr] | None = None
    AggFunc: StrictStr | None = None
