from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_measure_field import QuickSightMeasureField


class QuickSightTotalAggregationComputation(BaseModel):
    ComputationId: StrictStr | None = None
    Name: StrictStr | None = None
    Value: QuickSightMeasureField | None = None
