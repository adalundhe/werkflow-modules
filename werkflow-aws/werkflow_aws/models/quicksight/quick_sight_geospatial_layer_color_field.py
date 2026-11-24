from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_dimension_field import QuickSightDimensionField
from .quick_sight_measure_field import QuickSightMeasureField


class QuickSightGeospatialLayerColorField(BaseModel):
    ColorDimensionsFields: list[QuickSightDimensionField] | None = None
    ColorValuesFields: list[QuickSightMeasureField] | None = None
