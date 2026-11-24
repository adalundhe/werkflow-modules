from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_pivot_table_sort_by import QuickSightPivotTableSortBy


class QuickSightPivotFieldSortOptions(BaseModel):
    FieldId: StrictStr | None = None
    SortBy: QuickSightPivotTableSortBy | None = None
