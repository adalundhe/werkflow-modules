from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_table_conditional_formatting import QuickSightTableConditionalFormatting
from .quick_sight_table_configuration import QuickSightTableConfiguration
from .quick_sight_visual_custom_action import QuickSightVisualCustomAction
from .quick_sight_visual_subtitle_label_options import QuickSightVisualSubtitleLabelOptions
from .quick_sight_visual_title_label_options import QuickSightVisualTitleLabelOptions


class QuickSightTableVisual(BaseModel):
    VisualId: StrictStr | None = None
    Title: QuickSightVisualTitleLabelOptions | None = None
    Subtitle: QuickSightVisualSubtitleLabelOptions | None = None
    ChartConfiguration: QuickSightTableConfiguration | None = None
    ConditionalFormatting: QuickSightTableConditionalFormatting | None = None
    Actions: list[QuickSightVisualCustomAction] | None = None
    VisualContentAltText: StrictStr | None = None
