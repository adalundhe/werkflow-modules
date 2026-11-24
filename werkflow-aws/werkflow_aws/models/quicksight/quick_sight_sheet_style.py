from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_sheet_background_style import QuickSightSheetBackgroundStyle
from .quick_sight_tile_layout_style import QuickSightTileLayoutStyle
from .quick_sight_tile_style import QuickSightTileStyle


class QuickSightSheetStyle(BaseModel):
    Tile: QuickSightTileStyle | None = None
    TileLayout: QuickSightTileLayoutStyle | None = None
    Background: QuickSightSheetBackgroundStyle | None = None
