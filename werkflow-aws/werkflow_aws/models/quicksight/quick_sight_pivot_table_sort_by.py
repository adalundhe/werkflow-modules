from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_column_sort import QuickSightColumnSort
from .quick_sight_data_path_sort import QuickSightDataPathSort
from .quick_sight_field_sort import QuickSightFieldSort


class QuickSightPivotTableSortBy(BaseModel):
    Field: QuickSightFieldSort | None = None
    Column: QuickSightColumnSort | None = None
    DataPath: QuickSightDataPathSort | None = None
