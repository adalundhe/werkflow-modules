from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightUniqueKey(BaseModel):
    ColumnNames: list[StrictStr] | None = None
