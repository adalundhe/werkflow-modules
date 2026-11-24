from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_geospatial_coordinate_bounds import QuickSightGeospatialCoordinateBounds


class QuickSightGeospatialMapState(BaseModel):
    Bounds: QuickSightGeospatialCoordinateBounds | None = None
    MapNavigation: StrictStr | None = None
