from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_filter_operation import QuickSightFilterOperation
from .quick_sight_transform_operation_source import QuickSightTransformOperationSource


class QuickSightFiltersOperation(BaseModel):
    Alias: StrictStr | None = None
    Source: QuickSightTransformOperationSource | None = None
    FilterOperations: list[QuickSightFilterOperation] | None = None
