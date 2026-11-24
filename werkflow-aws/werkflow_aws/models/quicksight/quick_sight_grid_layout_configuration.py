from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_grid_layout_canvas_size_options import QuickSightGridLayoutCanvasSizeOptions
from .quick_sight_grid_layout_element import QuickSightGridLayoutElement


class QuickSightGridLayoutConfiguration(BaseModel):
    Elements: list[QuickSightGridLayoutElement] | None = None
    CanvasSizeOptions: QuickSightGridLayoutCanvasSizeOptions | None = None
