from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_total_aggregation_function import QuickSightTotalAggregationFunction


class QuickSightTotalAggregationOption(BaseModel):
    FieldId: StrictStr | None = None
    TotalAggregationFunction: QuickSightTotalAggregationFunction | None = None
