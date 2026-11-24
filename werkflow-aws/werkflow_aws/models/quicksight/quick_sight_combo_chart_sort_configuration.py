from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_field_sort_options import QuickSightFieldSortOptions
from .quick_sight_items_limit_configuration import QuickSightItemsLimitConfiguration


class QuickSightComboChartSortConfiguration(BaseModel):
    CategorySort: list[QuickSightFieldSortOptions] | None = None
    CategoryItemsLimit: QuickSightItemsLimitConfiguration | None = None
    ColorSort: list[QuickSightFieldSortOptions] | None = None
    ColorItemsLimit: QuickSightItemsLimitConfiguration | None = None
