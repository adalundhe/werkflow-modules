from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_filled_map_conditional_formatting_option import QuickSightFilledMapConditionalFormattingOption


class QuickSightFilledMapConditionalFormatting(BaseModel):
    ConditionalFormattingOptions: list[QuickSightFilledMapConditionalFormattingOption] | None = None
