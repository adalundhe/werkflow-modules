from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class GlueStringColumnStatisticsData(BaseModel):
    MaximumLength: StrictInt | None = None
    AverageLength: StrictFloat | StrictInt | None = None
    NumberOfNulls: StrictInt | None = None
    NumberOfDistinctValues: StrictInt | None = None
