from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_pie_chart_aggregated_field_wells import QuickSightPieChartAggregatedFieldWells


class QuickSightPieChartFieldWells(BaseModel):
    PieChartAggregatedFieldWells: QuickSightPieChartAggregatedFieldWells | None = None
