from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightAppendedColumn(BaseModel):
    ColumnName: StrictStr | None = None
    NewColumnId: StrictStr | None = None
