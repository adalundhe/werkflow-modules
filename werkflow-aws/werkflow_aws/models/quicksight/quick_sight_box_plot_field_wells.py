from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_box_plot_aggregated_field_wells import QuickSightBoxPlotAggregatedFieldWells


class QuickSightBoxPlotFieldWells(BaseModel):
    BoxPlotAggregatedFieldWells: QuickSightBoxPlotAggregatedFieldWells | None = None
