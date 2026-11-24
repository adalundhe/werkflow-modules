from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .glue_decimal_number import GlueDecimalNumber


class GlueDecimalColumnStatisticsData(BaseModel):
    MinimumValue: GlueDecimalNumber | None = None
    MaximumValue: GlueDecimalNumber | None = None
    NumberOfNulls: StrictInt | None = None
    NumberOfDistinctValues: StrictInt | None = None
