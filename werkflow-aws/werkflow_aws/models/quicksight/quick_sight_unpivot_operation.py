from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_column_to_unpivot import QuickSightColumnToUnpivot
from .quick_sight_transform_operation_source import QuickSightTransformOperationSource


class QuickSightUnpivotOperation(BaseModel):
    Alias: StrictStr | None = None
    Source: QuickSightTransformOperationSource | None = None
    ColumnsToUnpivot: list[QuickSightColumnToUnpivot] | None = None
    UnpivotedLabelColumnName: StrictStr | None = None
    UnpivotedLabelColumnId: StrictStr | None = None
    UnpivotedValueColumnName: StrictStr | None = None
    UnpivotedValueColumnId: StrictStr | None = None
