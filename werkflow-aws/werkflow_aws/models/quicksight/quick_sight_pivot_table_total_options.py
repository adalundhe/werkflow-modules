from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_pivot_total_options import QuickSightPivotTotalOptions
from .quick_sight_subtotal_options import QuickSightSubtotalOptions


class QuickSightPivotTableTotalOptions(BaseModel):
    RowSubtotalOptions: QuickSightSubtotalOptions | None = None
    ColumnSubtotalOptions: QuickSightSubtotalOptions | None = None
    RowTotalOptions: QuickSightPivotTotalOptions | None = None
    ColumnTotalOptions: QuickSightPivotTotalOptions | None = None
