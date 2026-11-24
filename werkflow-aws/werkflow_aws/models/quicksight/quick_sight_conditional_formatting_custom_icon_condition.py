from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_conditional_formatting_custom_icon_options import QuickSightConditionalFormattingCustomIconOptions
from .quick_sight_conditional_formatting_icon_display_configuration import QuickSightConditionalFormattingIconDisplayConfiguration


class QuickSightConditionalFormattingCustomIconCondition(BaseModel):
    Expression: StrictStr | None = None
    IconOptions: QuickSightConditionalFormattingCustomIconOptions | None = None
    Color: StrictStr | None = None
    DisplayConfiguration: QuickSightConditionalFormattingIconDisplayConfiguration | None = None
