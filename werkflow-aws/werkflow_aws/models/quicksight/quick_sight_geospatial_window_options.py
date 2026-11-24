from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_geospatial_coordinate_bounds import QuickSightGeospatialCoordinateBounds


class QuickSightGeospatialWindowOptions(BaseModel):
    Bounds: QuickSightGeospatialCoordinateBounds | None = None
    MapZoomMode: StrictStr | None = None
