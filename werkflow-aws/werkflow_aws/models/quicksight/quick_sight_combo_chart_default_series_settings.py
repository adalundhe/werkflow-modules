from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_border_settings import QuickSightBorderSettings
from .quick_sight_decal_settings import QuickSightDecalSettings
from .quick_sight_line_chart_line_style_settings import QuickSightLineChartLineStyleSettings
from .quick_sight_line_chart_marker_style_settings import QuickSightLineChartMarkerStyleSettings


class QuickSightComboChartDefaultSeriesSettings(BaseModel):
    LineStyleSettings: QuickSightLineChartLineStyleSettings | None = None
    MarkerStyleSettings: QuickSightLineChartMarkerStyleSettings | None = None
    DecalSettings: QuickSightDecalSettings | None = None
    BorderSettings: QuickSightBorderSettings | None = None
