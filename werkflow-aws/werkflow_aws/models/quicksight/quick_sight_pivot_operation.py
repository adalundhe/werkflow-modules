from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_pivot_configuration import QuickSightPivotConfiguration
from .quick_sight_transform_operation_source import QuickSightTransformOperationSource
from .quick_sight_value_column_configuration import QuickSightValueColumnConfiguration


class QuickSightPivotOperation(BaseModel):
    Alias: StrictStr | None = None
    Source: QuickSightTransformOperationSource | None = None
    GroupByColumnNames: list[StrictStr] | None = None
    ValueColumnConfiguration: QuickSightValueColumnConfiguration | None = None
    PivotConfiguration: QuickSightPivotConfiguration | None = None
