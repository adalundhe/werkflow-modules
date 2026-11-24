from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_data_prep_list_aggregation_function import QuickSightDataPrepListAggregationFunction
from .quick_sight_data_prep_simple_aggregation_function import QuickSightDataPrepSimpleAggregationFunction


class QuickSightDataPrepAggregationFunction(BaseModel):
    SimpleAggregation: QuickSightDataPrepSimpleAggregationFunction | None = None
    ListAggregation: QuickSightDataPrepListAggregationFunction | None = None
