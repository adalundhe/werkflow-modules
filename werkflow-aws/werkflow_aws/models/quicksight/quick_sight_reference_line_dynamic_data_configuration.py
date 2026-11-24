from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_aggregation_function import QuickSightAggregationFunction
from .quick_sight_column_identifier import QuickSightColumnIdentifier
from .quick_sight_numerical_aggregation_function import QuickSightNumericalAggregationFunction


class QuickSightReferenceLineDynamicDataConfiguration(BaseModel):
    Column: QuickSightColumnIdentifier | None = None
    MeasureAggregationFunction: QuickSightAggregationFunction | None = None
    Calculation: QuickSightNumericalAggregationFunction | None = None
