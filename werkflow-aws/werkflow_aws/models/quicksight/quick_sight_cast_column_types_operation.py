from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_cast_column_type_operation import QuickSightCastColumnTypeOperation
from .quick_sight_transform_operation_source import QuickSightTransformOperationSource


class QuickSightCastColumnTypesOperation(BaseModel):
    Alias: StrictStr | None = None
    Source: QuickSightTransformOperationSource | None = None
    CastColumnTypeOperations: list[QuickSightCastColumnTypeOperation] | None = None
