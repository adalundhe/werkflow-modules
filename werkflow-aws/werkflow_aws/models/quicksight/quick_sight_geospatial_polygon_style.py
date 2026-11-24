from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_geospatial_polygon_symbol_style import QuickSightGeospatialPolygonSymbolStyle


class QuickSightGeospatialPolygonStyle(BaseModel):
    PolygonSymbolStyle: QuickSightGeospatialPolygonSymbolStyle | None = None
