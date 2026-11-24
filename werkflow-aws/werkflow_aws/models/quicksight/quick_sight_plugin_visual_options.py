from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_plugin_visual_property import QuickSightPluginVisualProperty


class QuickSightPluginVisualOptions(BaseModel):
    VisualProperties: list[QuickSightPluginVisualProperty] | None = None
