from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_column_sort import QuickSightColumnSort
from .quick_sight_field_sort import QuickSightFieldSort


class QuickSightFieldSortOptions(BaseModel):
    FieldSort: QuickSightFieldSort | None = None
    ColumnSort: QuickSightColumnSort | None = None
