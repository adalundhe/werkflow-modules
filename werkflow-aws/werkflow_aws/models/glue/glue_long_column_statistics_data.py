from __future__ import annotations
from pydantic import BaseModel, StrictInt


class GlueLongColumnStatisticsData(BaseModel):
    MinimumValue: StrictInt | None = None
    MaximumValue: StrictInt | None = None
    NumberOfNulls: StrictInt | None = None
    NumberOfDistinctValues: StrictInt | None = None
