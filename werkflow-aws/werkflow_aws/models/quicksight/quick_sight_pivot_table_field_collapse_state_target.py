from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_data_path_value import QuickSightDataPathValue


class QuickSightPivotTableFieldCollapseStateTarget(BaseModel):
    FieldId: StrictStr | None = None
    FieldDataPathValues: list[QuickSightDataPathValue] | None = None
