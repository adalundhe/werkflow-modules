from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_calculated_column import QuickSightCalculatedColumn
from .quick_sight_transform_operation_source import QuickSightTransformOperationSource


class QuickSightCreateColumnsOperation(BaseModel):
    Alias: StrictStr | None = None
    Source: QuickSightTransformOperationSource | None = None
    Columns: list[QuickSightCalculatedColumn] | None = None
