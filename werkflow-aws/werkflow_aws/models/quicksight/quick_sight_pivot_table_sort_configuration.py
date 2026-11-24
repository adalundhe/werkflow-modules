from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_pivot_field_sort_options import QuickSightPivotFieldSortOptions


class QuickSightPivotTableSortConfiguration(BaseModel):
    FieldSortOptions: list[QuickSightPivotFieldSortOptions] | None = None
