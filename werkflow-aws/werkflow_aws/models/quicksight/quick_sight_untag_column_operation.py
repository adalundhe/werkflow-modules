from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightUntagColumnOperation(BaseModel):
    ColumnName: StrictStr | None = None
    TagNames: list[StrictStr] | None = None
