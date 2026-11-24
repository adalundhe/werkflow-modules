from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_field_sort_options import QuickSightFieldSortOptions
from .quick_sight_items_limit_configuration import QuickSightItemsLimitConfiguration


class QuickSightHeatMapSortConfiguration(BaseModel):
    HeatMapRowSort: list[QuickSightFieldSortOptions] | None = None
    HeatMapColumnSort: list[QuickSightFieldSortOptions] | None = None
    HeatMapRowItemsLimitConfiguration: QuickSightItemsLimitConfiguration | None = None
    HeatMapColumnItemsLimitConfiguration: QuickSightItemsLimitConfiguration | None = None
