from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_data_path_value import QuickSightDataPathValue


class QuickSightPivotTableDataPathOption(BaseModel):
    DataPathList: list[QuickSightDataPathValue] | None = None
    Width: StrictStr | None = None
