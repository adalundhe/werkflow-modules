from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_data_prep_aggregation_function import QuickSightDataPrepAggregationFunction


class QuickSightAggregation(BaseModel):
    AggregationFunction: QuickSightDataPrepAggregationFunction | None = None
    NewColumnName: StrictStr | None = None
    NewColumnId: StrictStr | None = None
