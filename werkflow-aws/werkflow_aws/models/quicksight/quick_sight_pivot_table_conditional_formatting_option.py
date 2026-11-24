from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_pivot_table_cell_conditional_formatting import QuickSightPivotTableCellConditionalFormatting


class QuickSightPivotTableConditionalFormattingOption(BaseModel):
    Cell: QuickSightPivotTableCellConditionalFormatting | None = None
