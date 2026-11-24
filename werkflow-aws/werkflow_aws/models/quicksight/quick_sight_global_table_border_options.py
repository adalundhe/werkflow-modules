from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_table_border_options import QuickSightTableBorderOptions
from .quick_sight_table_side_border_options import QuickSightTableSideBorderOptions


class QuickSightGlobalTableBorderOptions(BaseModel):
    UniformBorder: QuickSightTableBorderOptions | None = None
    SideSpecificBorder: QuickSightTableSideBorderOptions | None = None
