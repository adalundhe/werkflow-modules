from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_geospatial_line_symbol_style import QuickSightGeospatialLineSymbolStyle


class QuickSightGeospatialLineStyle(BaseModel):
    LineSymbolStyle: QuickSightGeospatialLineSymbolStyle | None = None
