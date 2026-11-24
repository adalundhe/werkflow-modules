from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_control_title_font_configuration import QuickSightControlTitleFontConfiguration
from .quick_sight_font import QuickSightFont
from .quick_sight_font_configuration import QuickSightFontConfiguration
from .quick_sight_visual_subtitle_font_configuration import QuickSightVisualSubtitleFontConfiguration
from .quick_sight_visual_title_font_configuration import QuickSightVisualTitleFontConfiguration


class QuickSightTypography(BaseModel):
    FontFamilies: list[QuickSightFont] | None = None
    AxisTitleFontConfiguration: QuickSightFontConfiguration | None = None
    AxisLabelFontConfiguration: QuickSightFontConfiguration | None = None
    LegendTitleFontConfiguration: QuickSightFontConfiguration | None = None
    LegendValueFontConfiguration: QuickSightFontConfiguration | None = None
    DataLabelFontConfiguration: QuickSightFontConfiguration | None = None
    VisualTitleFontConfiguration: QuickSightVisualTitleFontConfiguration | None = None
    VisualSubtitleFontConfiguration: QuickSightVisualSubtitleFontConfiguration | None = None
    ControlTitleFontConfiguration: QuickSightControlTitleFontConfiguration | None = None
