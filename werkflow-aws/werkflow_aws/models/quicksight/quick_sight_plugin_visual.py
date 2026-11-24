from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_plugin_visual_configuration import QuickSightPluginVisualConfiguration
from .quick_sight_visual_custom_action import QuickSightVisualCustomAction
from .quick_sight_visual_subtitle_label_options import QuickSightVisualSubtitleLabelOptions
from .quick_sight_visual_title_label_options import QuickSightVisualTitleLabelOptions


class QuickSightPluginVisual(BaseModel):
    VisualId: StrictStr | None = None
    PluginArn: StrictStr | None = None
    Title: QuickSightVisualTitleLabelOptions | None = None
    Subtitle: QuickSightVisualSubtitleLabelOptions | None = None
    ChartConfiguration: QuickSightPluginVisualConfiguration | None = None
    Actions: list[QuickSightVisualCustomAction] | None = None
    VisualContentAltText: StrictStr | None = None
