from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_field_sort_options import QuickSightFieldSortOptions
from .quick_sight_items_limit_configuration import QuickSightItemsLimitConfiguration


class QuickSightLineChartSortConfiguration(BaseModel):
    CategorySort: list[QuickSightFieldSortOptions] | None = None
    CategoryItemsLimitConfiguration: QuickSightItemsLimitConfiguration | None = None
    ColorItemsLimitConfiguration: QuickSightItemsLimitConfiguration | None = None
    SmallMultiplesSort: list[QuickSightFieldSortOptions] | None = None
    SmallMultiplesLimitConfiguration: QuickSightItemsLimitConfiguration | None = None
