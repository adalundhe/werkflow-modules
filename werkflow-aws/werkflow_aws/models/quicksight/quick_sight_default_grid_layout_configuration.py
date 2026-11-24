from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_grid_layout_canvas_size_options import QuickSightGridLayoutCanvasSizeOptions


class QuickSightDefaultGridLayoutConfiguration(BaseModel):
    CanvasSizeOptions: QuickSightGridLayoutCanvasSizeOptions | None = None
