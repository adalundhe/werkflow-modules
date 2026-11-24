from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_row_alternate_color_options import QuickSightRowAlternateColorOptions
from .quick_sight_table_cell_style import QuickSightTableCellStyle


class QuickSightTableOptions(BaseModel):
    Orientation: StrictStr | None = None
    HeaderStyle: QuickSightTableCellStyle | None = None
    CellStyle: QuickSightTableCellStyle | None = None
    RowAlternateColorOptions: QuickSightRowAlternateColorOptions | None = None
