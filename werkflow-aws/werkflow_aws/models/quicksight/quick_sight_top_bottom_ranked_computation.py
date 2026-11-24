from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_dimension_field import QuickSightDimensionField
from .quick_sight_measure_field import QuickSightMeasureField


class QuickSightTopBottomRankedComputation(BaseModel):
    ComputationId: StrictStr | None = None
    Name: StrictStr | None = None
    Category: QuickSightDimensionField | None = None
    Value: QuickSightMeasureField | None = None
    ResultSize: StrictInt | None = None
    Type: StrictStr | None = None
