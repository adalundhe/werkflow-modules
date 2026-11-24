from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_geospatial_polygon_style import QuickSightGeospatialPolygonStyle


class QuickSightGeospatialPolygonLayer(BaseModel):
    Style: QuickSightGeospatialPolygonStyle | None = None
