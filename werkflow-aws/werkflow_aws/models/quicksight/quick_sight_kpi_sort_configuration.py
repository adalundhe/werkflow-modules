from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_field_sort_options import QuickSightFieldSortOptions


class QuickSightKPISortConfiguration(BaseModel):
    TrendGroupSort: list[QuickSightFieldSortOptions] | None = None
