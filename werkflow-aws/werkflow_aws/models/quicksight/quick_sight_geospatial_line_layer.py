from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_geospatial_line_style import QuickSightGeospatialLineStyle


class QuickSightGeospatialLineLayer(BaseModel):
    Style: QuickSightGeospatialLineStyle | None = None
