from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_appended_column import QuickSightAppendedColumn
from .quick_sight_transform_operation_source import QuickSightTransformOperationSource


class QuickSightAppendOperation(BaseModel):
    Alias: StrictStr | None = None
    FirstSource: QuickSightTransformOperationSource | None = None
    SecondSource: QuickSightTransformOperationSource | None = None
    AppendedColumns: list[QuickSightAppendedColumn] | None = None
