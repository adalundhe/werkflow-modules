from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_geospatial_color import QuickSightGeospatialColor
from .quick_sight_geospatial_line_width import QuickSightGeospatialLineWidth


class QuickSightGeospatialPolygonSymbolStyle(BaseModel):
    FillColor: QuickSightGeospatialColor | None = None
    StrokeColor: QuickSightGeospatialColor | None = None
    StrokeWidth: QuickSightGeospatialLineWidth | None = None
