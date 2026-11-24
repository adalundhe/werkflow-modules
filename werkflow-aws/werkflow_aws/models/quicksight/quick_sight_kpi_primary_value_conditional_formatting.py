from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_conditional_formatting_color import QuickSightConditionalFormattingColor
from .quick_sight_conditional_formatting_icon import QuickSightConditionalFormattingIcon


class QuickSightKPIPrimaryValueConditionalFormatting(BaseModel):
    TextColor: QuickSightConditionalFormattingColor | None = None
    Icon: QuickSightConditionalFormattingIcon | None = None
