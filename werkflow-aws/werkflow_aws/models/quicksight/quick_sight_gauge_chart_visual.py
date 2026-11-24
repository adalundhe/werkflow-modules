from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_gauge_chart_conditional_formatting import QuickSightGaugeChartConditionalFormatting
from .quick_sight_gauge_chart_configuration import QuickSightGaugeChartConfiguration
from .quick_sight_visual_custom_action import QuickSightVisualCustomAction
from .quick_sight_visual_subtitle_label_options import QuickSightVisualSubtitleLabelOptions
from .quick_sight_visual_title_label_options import QuickSightVisualTitleLabelOptions


class QuickSightGaugeChartVisual(BaseModel):
    VisualId: StrictStr | None = None
    Title: QuickSightVisualTitleLabelOptions | None = None
    Subtitle: QuickSightVisualSubtitleLabelOptions | None = None
    ChartConfiguration: QuickSightGaugeChartConfiguration | None = None
    ConditionalFormatting: QuickSightGaugeChartConditionalFormatting | None = None
    Actions: list[QuickSightVisualCustomAction] | None = None
    VisualContentAltText: StrictStr | None = None
