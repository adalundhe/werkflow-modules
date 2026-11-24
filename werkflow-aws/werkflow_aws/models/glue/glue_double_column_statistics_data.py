from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class GlueDoubleColumnStatisticsData(BaseModel):
    MinimumValue: StrictFloat | StrictInt | None = None
    MaximumValue: StrictFloat | StrictInt | None = None
    NumberOfNulls: StrictInt | None = None
    NumberOfDistinctValues: StrictInt | None = None
