from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_pivot_table_conditional_formatting_option import QuickSightPivotTableConditionalFormattingOption


class QuickSightPivotTableConditionalFormatting(BaseModel):
    ConditionalFormattingOptions: list[QuickSightPivotTableConditionalFormattingOption] | None = None
