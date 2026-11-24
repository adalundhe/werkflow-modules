from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_geospatial_circle_symbol_style import QuickSightGeospatialCircleSymbolStyle


class QuickSightGeospatialPointStyle(BaseModel):
    CircleSymbolStyle: QuickSightGeospatialCircleSymbolStyle | None = None
