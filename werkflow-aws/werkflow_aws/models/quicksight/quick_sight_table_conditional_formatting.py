from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_table_conditional_formatting_option import QuickSightTableConditionalFormattingOption


class QuickSightTableConditionalFormatting(BaseModel):
    ConditionalFormattingOptions: list[QuickSightTableConditionalFormattingOption] | None = None
