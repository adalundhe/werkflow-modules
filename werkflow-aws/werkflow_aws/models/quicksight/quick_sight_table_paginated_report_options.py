from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightTablePaginatedReportOptions(BaseModel):
    VerticalOverflowVisibility: StrictStr | None = None
    OverflowColumnHeaderVisibility: StrictStr | None = None
