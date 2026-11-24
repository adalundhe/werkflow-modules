from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_percentile_aggregation import QuickSightPercentileAggregation


class QuickSightNumericalAggregationFunction(BaseModel):
    SimpleNumericalAggregation: StrictStr | None = None
    PercentileAggregation: QuickSightPercentileAggregation | None = None
