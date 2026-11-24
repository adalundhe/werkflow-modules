from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDataPathType(BaseModel):
    PivotTableDataPathType: StrictStr | None = None
