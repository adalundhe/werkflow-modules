from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightCalculatedColumn(BaseModel):
    ColumnName: StrictStr | None = None
    ColumnId: StrictStr | None = None
    Expression: StrictStr | None = None
