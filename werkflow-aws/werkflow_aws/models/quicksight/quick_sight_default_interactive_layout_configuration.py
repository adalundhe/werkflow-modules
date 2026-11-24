from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_default_free_form_layout_configuration import QuickSightDefaultFreeFormLayoutConfiguration
from .quick_sight_default_grid_layout_configuration import QuickSightDefaultGridLayoutConfiguration


class QuickSightDefaultInteractiveLayoutConfiguration(BaseModel):
    Grid: QuickSightDefaultGridLayoutConfiguration | None = None
    FreeForm: QuickSightDefaultFreeFormLayoutConfiguration | None = None
