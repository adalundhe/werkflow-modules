from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_filled_map_shape_conditional_formatting import QuickSightFilledMapShapeConditionalFormatting


class QuickSightFilledMapConditionalFormattingOption(BaseModel):
    Shape: QuickSightFilledMapShapeConditionalFormatting | None = None
