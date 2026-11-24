from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightCastColumnTypeOperation(BaseModel):
    ColumnName: StrictStr | None = None
    NewColumnType: StrictStr | None = None
    SubType: StrictStr | None = None
    Format: StrictStr | None = None
