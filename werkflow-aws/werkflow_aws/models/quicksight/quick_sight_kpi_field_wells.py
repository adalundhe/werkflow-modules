from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_dimension_field import QuickSightDimensionField
from .quick_sight_measure_field import QuickSightMeasureField


class QuickSightKPIFieldWells(BaseModel):
    Values: list[QuickSightMeasureField] | None = None
    TargetValues: list[QuickSightMeasureField] | None = None
    TrendGroups: list[QuickSightDimensionField] | None = None
