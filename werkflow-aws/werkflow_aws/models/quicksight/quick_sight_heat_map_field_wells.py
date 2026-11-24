from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_heat_map_aggregated_field_wells import QuickSightHeatMapAggregatedFieldWells


class QuickSightHeatMapFieldWells(BaseModel):
    HeatMapAggregatedFieldWells: QuickSightHeatMapAggregatedFieldWells | None = None
