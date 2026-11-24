from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_dimension_field import QuickSightDimensionField
from .quick_sight_measure_field import QuickSightMeasureField


class QuickSightBoxPlotAggregatedFieldWells(BaseModel):
    GroupBy: list[QuickSightDimensionField] | None = None
    Values: list[QuickSightMeasureField] | None = None
