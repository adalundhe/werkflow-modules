from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class QuickSightPercentileAggregation(BaseModel):
    PercentileValue: StrictFloat | StrictInt | None = None
