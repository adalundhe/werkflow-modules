from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_dimension_field import QuickSightDimensionField
from .quick_sight_measure_field import QuickSightMeasureField


class QuickSightMetricComparisonComputation(BaseModel):
    ComputationId: StrictStr | None = None
    Name: StrictStr | None = None
    Time: QuickSightDimensionField | None = None
    FromValue: QuickSightMeasureField | None = None
    TargetValue: QuickSightMeasureField | None = None
