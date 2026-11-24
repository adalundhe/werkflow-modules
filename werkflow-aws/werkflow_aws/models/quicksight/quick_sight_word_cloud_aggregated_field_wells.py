from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_dimension_field import QuickSightDimensionField
from .quick_sight_measure_field import QuickSightMeasureField


class QuickSightWordCloudAggregatedFieldWells(BaseModel):
    GroupBy: list[QuickSightDimensionField] | None = None
    Size: list[QuickSightMeasureField] | None = None
