from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_free_form_layout_canvas_size_options import QuickSightFreeFormLayoutCanvasSizeOptions


class QuickSightDefaultFreeFormLayoutConfiguration(BaseModel):
    CanvasSizeOptions: QuickSightFreeFormLayoutCanvasSizeOptions | None = None
