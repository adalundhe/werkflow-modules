from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_field_sort_options import QuickSightFieldSortOptions
from .quick_sight_items_limit_configuration import QuickSightItemsLimitConfiguration


class QuickSightTreeMapSortConfiguration(BaseModel):
    TreeMapSort: list[QuickSightFieldSortOptions] | None = None
    TreeMapGroupItemsLimitConfiguration: QuickSightItemsLimitConfiguration | None = None
