from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightColumnToUnpivot(BaseModel):
    ColumnName: StrictStr | None = None
    NewValue: StrictStr | None = None
