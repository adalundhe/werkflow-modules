from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_attribute_aggregation_function import QuickSightAttributeAggregationFunction
from .quick_sight_numerical_aggregation_function import QuickSightNumericalAggregationFunction


class QuickSightAggregationFunction(BaseModel):
    NumericalAggregationFunction: QuickSightNumericalAggregationFunction | None = None
    CategoricalAggregationFunction: StrictStr | None = None
    DateAggregationFunction: StrictStr | None = None
    AttributeAggregationFunction: QuickSightAttributeAggregationFunction | None = None
