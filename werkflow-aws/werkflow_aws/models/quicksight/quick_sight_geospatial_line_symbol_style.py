from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_geospatial_color import QuickSightGeospatialColor
from .quick_sight_geospatial_line_width import QuickSightGeospatialLineWidth


class QuickSightGeospatialLineSymbolStyle(BaseModel):
    FillColor: QuickSightGeospatialColor | None = None
    LineWidth: QuickSightGeospatialLineWidth | None = None
