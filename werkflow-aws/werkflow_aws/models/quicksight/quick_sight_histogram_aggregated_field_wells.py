from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_measure_field import QuickSightMeasureField


class QuickSightHistogramAggregatedFieldWells(BaseModel):
    Values: list[QuickSightMeasureField] | None = None
