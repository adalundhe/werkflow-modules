from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_kpi_conditional_formatting_option import QuickSightKPIConditionalFormattingOption


class QuickSightKPIConditionalFormatting(BaseModel):
    ConditionalFormattingOptions: list[QuickSightKPIConditionalFormattingOption] | None = None
