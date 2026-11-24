from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_conditional_formatting_gradient_color import QuickSightConditionalFormattingGradientColor
from .quick_sight_conditional_formatting_solid_color import QuickSightConditionalFormattingSolidColor


class QuickSightConditionalFormattingColor(BaseModel):
    Solid: QuickSightConditionalFormattingSolidColor | None = None
    Gradient: QuickSightConditionalFormattingGradientColor | None = None
