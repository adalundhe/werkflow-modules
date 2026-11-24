from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_radar_chart_area_style_settings import QuickSightRadarChartAreaStyleSettings


class QuickSightRadarChartSeriesSettings(BaseModel):
    AreaStyleSettings: QuickSightRadarChartAreaStyleSettings | None = None
