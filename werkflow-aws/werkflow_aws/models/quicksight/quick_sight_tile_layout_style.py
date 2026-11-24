from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_gutter_style import QuickSightGutterStyle
from .quick_sight_margin_style import QuickSightMarginStyle


class QuickSightTileLayoutStyle(BaseModel):
    Gutter: QuickSightGutterStyle | None = None
    Margin: QuickSightMarginStyle | None = None
