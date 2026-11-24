from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_pivot_table_aggregated_field_wells import QuickSightPivotTableAggregatedFieldWells


class QuickSightPivotTableFieldWells(BaseModel):
    PivotTableAggregatedFieldWells: QuickSightPivotTableAggregatedFieldWells | None = None
