from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_field_sort_options import QuickSightFieldSortOptions
from .quick_sight_items_limit_configuration import QuickSightItemsLimitConfiguration


class QuickSightWaterfallChartSortConfiguration(BaseModel):
    CategorySort: list[QuickSightFieldSortOptions] | None = None
    BreakdownItemsLimit: QuickSightItemsLimitConfiguration | None = None
