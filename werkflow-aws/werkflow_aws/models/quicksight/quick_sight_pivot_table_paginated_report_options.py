from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightPivotTablePaginatedReportOptions(BaseModel):
    VerticalOverflowVisibility: StrictStr | None = None
    OverflowColumnHeaderVisibility: StrictStr | None = None
