from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_field_sort_options import QuickSightFieldSortOptions
from .quick_sight_items_limit_configuration import QuickSightItemsLimitConfiguration


class QuickSightWordCloudSortConfiguration(BaseModel):
    CategoryItemsLimit: QuickSightItemsLimitConfiguration | None = None
    CategorySort: list[QuickSightFieldSortOptions] | None = None
