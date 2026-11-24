from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_filled_map_aggregated_field_wells import QuickSightFilledMapAggregatedFieldWells


class QuickSightFilledMapFieldWells(BaseModel):
    FilledMapAggregatedFieldWells: QuickSightFilledMapAggregatedFieldWells | None = None
