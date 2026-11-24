from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_aggregation import QuickSightAggregation
from .quick_sight_transform_operation_source import QuickSightTransformOperationSource


class QuickSightAggregateOperation(BaseModel):
    Alias: StrictStr | None = None
    Source: QuickSightTransformOperationSource | None = None
    GroupByColumnNames: list[StrictStr] | None = None
    Aggregations: list[QuickSightAggregation] | None = None
