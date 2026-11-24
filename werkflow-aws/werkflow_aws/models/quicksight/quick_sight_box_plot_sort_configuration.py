from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_field_sort_options import QuickSightFieldSortOptions
from .quick_sight_pagination_configuration import QuickSightPaginationConfiguration


class QuickSightBoxPlotSortConfiguration(BaseModel):
    CategorySort: list[QuickSightFieldSortOptions] | None = None
    PaginationConfiguration: QuickSightPaginationConfiguration | None = None
