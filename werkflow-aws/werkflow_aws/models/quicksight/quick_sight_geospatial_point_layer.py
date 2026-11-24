from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_geospatial_point_style import QuickSightGeospatialPointStyle


class QuickSightGeospatialPointLayer(BaseModel):
    Style: QuickSightGeospatialPointStyle | None = None
