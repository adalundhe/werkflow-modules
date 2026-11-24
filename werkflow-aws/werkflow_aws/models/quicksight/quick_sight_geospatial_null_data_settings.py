from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_geospatial_null_symbol_style import QuickSightGeospatialNullSymbolStyle


class QuickSightGeospatialNullDataSettings(BaseModel):
    SymbolStyle: QuickSightGeospatialNullSymbolStyle | None = None
