from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_dimension_field import QuickSightDimensionField
from .quick_sight_measure_field import QuickSightMeasureField


class QuickSightTreeMapAggregatedFieldWells(BaseModel):
    Groups: list[QuickSightDimensionField] | None = None
    Sizes: list[QuickSightMeasureField] | None = None
    Colors: list[QuickSightMeasureField] | None = None
