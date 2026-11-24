from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class GlueBinaryColumnStatisticsData(BaseModel):
    MaximumLength: StrictInt | None = None
    AverageLength: StrictFloat | StrictInt | None = None
    NumberOfNulls: StrictInt | None = None
