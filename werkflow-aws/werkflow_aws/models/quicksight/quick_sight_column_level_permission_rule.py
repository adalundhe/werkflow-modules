from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightColumnLevelPermissionRule(BaseModel):
    Principals: list[StrictStr] | None = None
    ColumnNames: list[StrictStr] | None = None
