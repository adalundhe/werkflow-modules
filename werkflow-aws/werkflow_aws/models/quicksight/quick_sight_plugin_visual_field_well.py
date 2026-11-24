from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_dimension_field import QuickSightDimensionField
from .quick_sight_measure_field import QuickSightMeasureField
from .quick_sight_unaggregated_field import QuickSightUnaggregatedField


class QuickSightPluginVisualFieldWell(BaseModel):
    AxisName: StrictStr | None = None
    Dimensions: list[QuickSightDimensionField] | None = None
    Measures: list[QuickSightMeasureField] | None = None
    Unaggregated: list[QuickSightUnaggregatedField] | None = None
