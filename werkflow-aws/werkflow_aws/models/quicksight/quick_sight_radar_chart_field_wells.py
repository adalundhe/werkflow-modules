from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_radar_chart_aggregated_field_wells import QuickSightRadarChartAggregatedFieldWells


class QuickSightRadarChartFieldWells(BaseModel):
    RadarChartAggregatedFieldWells: QuickSightRadarChartAggregatedFieldWells | None = None
