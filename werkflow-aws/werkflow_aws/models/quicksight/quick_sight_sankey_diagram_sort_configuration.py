from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_field_sort_options import QuickSightFieldSortOptions
from .quick_sight_items_limit_configuration import QuickSightItemsLimitConfiguration


class QuickSightSankeyDiagramSortConfiguration(BaseModel):
    WeightSort: list[QuickSightFieldSortOptions] | None = None
    SourceItemsLimit: QuickSightItemsLimitConfiguration | None = None
    DestinationItemsLimit: QuickSightItemsLimitConfiguration | None = None
