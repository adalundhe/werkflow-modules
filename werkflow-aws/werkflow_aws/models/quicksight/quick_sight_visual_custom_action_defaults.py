from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_visual_highlight_operation import QuickSightVisualHighlightOperation


class QuickSightVisualCustomActionDefaults(BaseModel):
    highlightOperation: QuickSightVisualHighlightOperation | None = None
