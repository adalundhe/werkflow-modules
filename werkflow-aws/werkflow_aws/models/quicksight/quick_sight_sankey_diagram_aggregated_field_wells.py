from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_dimension_field import QuickSightDimensionField
from .quick_sight_measure_field import QuickSightMeasureField


class QuickSightSankeyDiagramAggregatedFieldWells(BaseModel):
    Source: list[QuickSightDimensionField] | None = None
    Destination: list[QuickSightDimensionField] | None = None
    Weight: list[QuickSightMeasureField] | None = None
