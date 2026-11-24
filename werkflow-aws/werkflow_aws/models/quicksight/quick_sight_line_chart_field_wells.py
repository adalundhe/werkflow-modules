from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_line_chart_aggregated_field_wells import QuickSightLineChartAggregatedFieldWells


class QuickSightLineChartFieldWells(BaseModel):
    LineChartAggregatedFieldWells: QuickSightLineChartAggregatedFieldWells | None = None
