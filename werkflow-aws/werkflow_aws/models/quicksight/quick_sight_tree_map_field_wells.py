from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_tree_map_aggregated_field_wells import QuickSightTreeMapAggregatedFieldWells


class QuickSightTreeMapFieldWells(BaseModel):
    TreeMapAggregatedFieldWells: QuickSightTreeMapAggregatedFieldWells | None = None
