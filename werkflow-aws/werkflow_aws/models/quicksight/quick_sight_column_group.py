from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_geo_spatial_column_group import QuickSightGeoSpatialColumnGroup


class QuickSightColumnGroup(BaseModel):
    GeoSpatialColumnGroup: QuickSightGeoSpatialColumnGroup | None = None
