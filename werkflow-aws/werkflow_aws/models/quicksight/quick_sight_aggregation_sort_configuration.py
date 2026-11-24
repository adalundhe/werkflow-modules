from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_aggregation_function import QuickSightAggregationFunction
from .quick_sight_column_identifier import QuickSightColumnIdentifier


class QuickSightAggregationSortConfiguration(BaseModel):
    Column: QuickSightColumnIdentifier | None = None
    SortDirection: StrictStr | None = None
    AggregationFunction: QuickSightAggregationFunction | None = None
