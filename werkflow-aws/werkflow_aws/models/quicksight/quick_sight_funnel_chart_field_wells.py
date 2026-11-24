from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_funnel_chart_aggregated_field_wells import QuickSightFunnelChartAggregatedFieldWells


class QuickSightFunnelChartFieldWells(BaseModel):
    FunnelChartAggregatedFieldWells: QuickSightFunnelChartAggregatedFieldWells | None = None
