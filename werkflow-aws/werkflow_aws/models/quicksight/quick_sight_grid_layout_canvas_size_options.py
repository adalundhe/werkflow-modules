from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_grid_layout_screen_canvas_size_options import QuickSightGridLayoutScreenCanvasSizeOptions


class QuickSightGridLayoutCanvasSizeOptions(BaseModel):
    ScreenCanvasSizeOptions: QuickSightGridLayoutScreenCanvasSizeOptions | None = None
