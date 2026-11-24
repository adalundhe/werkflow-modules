from __future__ import annotations
from pydantic import BaseModel, StrictInt


class GlueBooleanColumnStatisticsData(BaseModel):
    NumberOfTrues: StrictInt | None = None
    NumberOfFalses: StrictInt | None = None
    NumberOfNulls: StrictInt | None = None
