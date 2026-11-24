from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_data_path_value import QuickSightDataPathValue


class QuickSightDataPathSort(BaseModel):
    Direction: StrictStr | None = None
    SortPaths: list[QuickSightDataPathValue] | None = None
