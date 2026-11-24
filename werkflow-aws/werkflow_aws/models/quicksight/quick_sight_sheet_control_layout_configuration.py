from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_grid_layout_configuration import QuickSightGridLayoutConfiguration


class QuickSightSheetControlLayoutConfiguration(BaseModel):
    GridLayout: QuickSightGridLayoutConfiguration | None = None
