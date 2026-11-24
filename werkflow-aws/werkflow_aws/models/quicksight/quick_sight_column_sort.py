from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_aggregation_function import QuickSightAggregationFunction
from .quick_sight_column_identifier import QuickSightColumnIdentifier


class QuickSightColumnSort(BaseModel):
    SortBy: QuickSightColumnIdentifier | None = None
    Direction: StrictStr | None = None
    AggregationFunction: QuickSightAggregationFunction | None = None
