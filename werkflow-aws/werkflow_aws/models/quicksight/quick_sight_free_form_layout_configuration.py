from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_free_form_layout_canvas_size_options import QuickSightFreeFormLayoutCanvasSizeOptions
from .quick_sight_free_form_layout_element import QuickSightFreeFormLayoutElement
from .quick_sight_sheet_layout_group import QuickSightSheetLayoutGroup


class QuickSightFreeFormLayoutConfiguration(BaseModel):
    Elements: list[QuickSightFreeFormLayoutElement] | None = None
    CanvasSizeOptions: QuickSightFreeFormLayoutCanvasSizeOptions | None = None
    Groups: list[QuickSightSheetLayoutGroup] | None = None
