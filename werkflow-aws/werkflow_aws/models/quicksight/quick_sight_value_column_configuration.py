from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_data_prep_aggregation_function import QuickSightDataPrepAggregationFunction


class QuickSightValueColumnConfiguration(BaseModel):
    AggregationFunction: QuickSightDataPrepAggregationFunction | None = None
