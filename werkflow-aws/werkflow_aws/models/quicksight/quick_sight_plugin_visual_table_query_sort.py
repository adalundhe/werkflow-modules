from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_field_sort_options import QuickSightFieldSortOptions
from .quick_sight_plugin_visual_items_limit_configuration import QuickSightPluginVisualItemsLimitConfiguration


class QuickSightPluginVisualTableQuerySort(BaseModel):
    RowSort: list[QuickSightFieldSortOptions] | None = None
    ItemsLimitConfiguration: QuickSightPluginVisualItemsLimitConfiguration | None = None
