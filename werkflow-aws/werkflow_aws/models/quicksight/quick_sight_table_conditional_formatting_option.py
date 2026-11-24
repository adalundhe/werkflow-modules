from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_table_cell_conditional_formatting import QuickSightTableCellConditionalFormatting
from .quick_sight_table_row_conditional_formatting import QuickSightTableRowConditionalFormatting


class QuickSightTableConditionalFormattingOption(BaseModel):
    Cell: QuickSightTableCellConditionalFormatting | None = None
    Row: QuickSightTableRowConditionalFormatting | None = None
