from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_plugin_visual_field_well import QuickSightPluginVisualFieldWell
from .quick_sight_plugin_visual_options import QuickSightPluginVisualOptions
from .quick_sight_plugin_visual_sort_configuration import QuickSightPluginVisualSortConfiguration


class QuickSightPluginVisualConfiguration(BaseModel):
    FieldWells: list[QuickSightPluginVisualFieldWell] | None = None
    VisualOptions: QuickSightPluginVisualOptions | None = None
    SortConfiguration: QuickSightPluginVisualSortConfiguration | None = None
