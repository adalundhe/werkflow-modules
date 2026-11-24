from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_dimension_field import QuickSightDimensionField
from .quick_sight_measure_field import QuickSightMeasureField


class QuickSightGeospatialMapAggregatedFieldWells(BaseModel):
    Geospatial: list[QuickSightDimensionField] | None = None
    Values: list[QuickSightMeasureField] | None = None
    Colors: list[QuickSightDimensionField] | None = None
