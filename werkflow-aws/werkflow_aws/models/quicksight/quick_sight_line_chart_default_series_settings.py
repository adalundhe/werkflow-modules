from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_decal_settings import QuickSightDecalSettings
from .quick_sight_line_chart_line_style_settings import QuickSightLineChartLineStyleSettings
from .quick_sight_line_chart_marker_style_settings import QuickSightLineChartMarkerStyleSettings


class QuickSightLineChartDefaultSeriesSettings(BaseModel):
    AxisBinding: StrictStr | None = None
    LineStyleSettings: QuickSightLineChartLineStyleSettings | None = None
    MarkerStyleSettings: QuickSightLineChartMarkerStyleSettings | None = None
    DecalSettings: QuickSightDecalSettings | None = None
