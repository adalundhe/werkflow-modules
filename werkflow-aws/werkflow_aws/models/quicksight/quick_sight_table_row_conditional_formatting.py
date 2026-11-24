from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_conditional_formatting_color import QuickSightConditionalFormattingColor


class QuickSightTableRowConditionalFormatting(BaseModel):
    BackgroundColor: QuickSightConditionalFormattingColor | None = None
    TextColor: QuickSightConditionalFormattingColor | None = None
