from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_geospatial_map_aggregated_field_wells import QuickSightGeospatialMapAggregatedFieldWells


class QuickSightGeospatialMapFieldWells(BaseModel):
    GeospatialMapAggregatedFieldWells: QuickSightGeospatialMapAggregatedFieldWells | None = None
