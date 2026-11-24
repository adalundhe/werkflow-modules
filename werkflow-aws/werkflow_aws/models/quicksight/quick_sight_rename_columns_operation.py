from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_rename_column_operation import QuickSightRenameColumnOperation
from .quick_sight_transform_operation_source import QuickSightTransformOperationSource


class QuickSightRenameColumnsOperation(BaseModel):
    Alias: StrictStr | None = None
    Source: QuickSightTransformOperationSource | None = None
    RenameColumnOperations: list[QuickSightRenameColumnOperation] | None = None
