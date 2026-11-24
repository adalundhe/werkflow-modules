from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_gradient_color import QuickSightGradientColor


class QuickSightConditionalFormattingGradientColor(BaseModel):
    Expression: StrictStr | None = None
    Color: QuickSightGradientColor | None = None
