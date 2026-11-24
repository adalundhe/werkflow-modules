from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_conditional_formatting_custom_icon_condition import QuickSightConditionalFormattingCustomIconCondition
from .quick_sight_conditional_formatting_icon_set import QuickSightConditionalFormattingIconSet


class QuickSightConditionalFormattingIcon(BaseModel):
    IconSet: QuickSightConditionalFormattingIconSet | None = None
    CustomCondition: QuickSightConditionalFormattingCustomIconCondition | None = None
