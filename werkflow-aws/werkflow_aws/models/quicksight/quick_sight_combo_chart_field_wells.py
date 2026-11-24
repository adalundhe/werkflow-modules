from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_combo_chart_aggregated_field_wells import QuickSightComboChartAggregatedFieldWells


class QuickSightComboChartFieldWells(BaseModel):
    ComboChartAggregatedFieldWells: QuickSightComboChartAggregatedFieldWells | None = None
