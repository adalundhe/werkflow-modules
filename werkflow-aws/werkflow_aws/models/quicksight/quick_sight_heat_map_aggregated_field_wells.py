from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_dimension_field import QuickSightDimensionField
from .quick_sight_measure_field import QuickSightMeasureField


class QuickSightHeatMapAggregatedFieldWells(BaseModel):
    Rows: list[QuickSightDimensionField] | None = None
    Columns: list[QuickSightDimensionField] | None = None
    Values: list[QuickSightMeasureField] | None = None
