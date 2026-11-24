from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_plugin_visual_table_query_sort import QuickSightPluginVisualTableQuerySort


class QuickSightPluginVisualSortConfiguration(BaseModel):
    PluginVisualTableQuerySort: QuickSightPluginVisualTableQuerySort | None = None
