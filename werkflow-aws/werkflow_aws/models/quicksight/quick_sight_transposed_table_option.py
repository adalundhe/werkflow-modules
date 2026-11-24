from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightTransposedTableOption(BaseModel):
    ColumnIndex: StrictInt | None = None
    ColumnWidth: StrictStr | None = None
    ColumnType: StrictStr | None = None
