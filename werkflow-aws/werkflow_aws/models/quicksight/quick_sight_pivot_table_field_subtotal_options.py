from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightPivotTableFieldSubtotalOptions(BaseModel):
    FieldId: StrictStr | None = None
