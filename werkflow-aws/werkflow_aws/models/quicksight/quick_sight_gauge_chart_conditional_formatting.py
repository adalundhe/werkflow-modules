from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_gauge_chart_conditional_formatting_option import QuickSightGaugeChartConditionalFormattingOption


class QuickSightGaugeChartConditionalFormatting(BaseModel):
    ConditionalFormattingOptions: list[QuickSightGaugeChartConditionalFormattingOption] | None = None
