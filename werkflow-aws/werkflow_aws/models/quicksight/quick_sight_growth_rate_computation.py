from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_dimension_field import QuickSightDimensionField
from .quick_sight_measure_field import QuickSightMeasureField


class QuickSightGrowthRateComputation(BaseModel):
    ComputationId: StrictStr | None = None
    Name: StrictStr | None = None
    Time: QuickSightDimensionField | None = None
    Value: QuickSightMeasureField | None = None
    PeriodSize: StrictInt | None = None
