from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_sheet_image_tooltip_text import QuickSightSheetImageTooltipText


class QuickSightSheetImageTooltipConfiguration(BaseModel):
    TooltipText: QuickSightSheetImageTooltipText | None = None
    Visibility: StrictStr | None = None
