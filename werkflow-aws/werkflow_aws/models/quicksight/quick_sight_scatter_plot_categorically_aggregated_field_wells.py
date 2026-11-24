from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_dimension_field import QuickSightDimensionField
from .quick_sight_measure_field import QuickSightMeasureField


class QuickSightScatterPlotCategoricallyAggregatedFieldWells(BaseModel):
    XAxis: list[QuickSightMeasureField] | None = None
    YAxis: list[QuickSightMeasureField] | None = None
    Category: list[QuickSightDimensionField] | None = None
    Size: list[QuickSightMeasureField] | None = None
    Label: list[QuickSightDimensionField] | None = None
