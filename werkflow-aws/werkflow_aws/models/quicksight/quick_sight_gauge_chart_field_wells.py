from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_measure_field import QuickSightMeasureField


class QuickSightGaugeChartFieldWells(BaseModel):
    Values: list[QuickSightMeasureField] | None = None
    TargetValues: list[QuickSightMeasureField] | None = None
