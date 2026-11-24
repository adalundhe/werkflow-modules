from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightUnmaterializedCalculatedColumn(BaseModel):
    ColumnId: StrictStr | None = None
    ColumnName: StrictStr | None = None
    Expression: StrictStr | None = None
    Type: StrictStr | None = None
    SubType: StrictStr | None = None
