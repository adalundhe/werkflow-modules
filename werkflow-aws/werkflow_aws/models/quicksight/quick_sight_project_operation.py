from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_transform_operation_source import QuickSightTransformOperationSource


class QuickSightProjectOperation(BaseModel):
    Alias: StrictStr | None = None
    Source: QuickSightTransformOperationSource | None = None
    ProjectedColumns: list[StrictStr] | None = None
