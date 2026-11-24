from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_table_border_options import QuickSightTableBorderOptions


class QuickSightTableSideBorderOptions(BaseModel):
    InnerVertical: QuickSightTableBorderOptions | None = None
    InnerHorizontal: QuickSightTableBorderOptions | None = None
    Left: QuickSightTableBorderOptions | None = None
    Right: QuickSightTableBorderOptions | None = None
    Top: QuickSightTableBorderOptions | None = None
    Bottom: QuickSightTableBorderOptions | None = None
