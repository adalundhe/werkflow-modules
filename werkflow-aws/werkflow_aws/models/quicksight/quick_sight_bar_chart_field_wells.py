from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_bar_chart_aggregated_field_wells import QuickSightBarChartAggregatedFieldWells


class QuickSightBarChartFieldWells(BaseModel):
    BarChartAggregatedFieldWells: QuickSightBarChartAggregatedFieldWells | None = None
