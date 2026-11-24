from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_table_aggregated_field_wells import QuickSightTableAggregatedFieldWells
from .quick_sight_table_unaggregated_field_wells import QuickSightTableUnaggregatedFieldWells


class QuickSightTableFieldWells(BaseModel):
    TableAggregatedFieldWells: QuickSightTableAggregatedFieldWells | None = None
    TableUnaggregatedFieldWells: QuickSightTableUnaggregatedFieldWells | None = None
