from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightPivotTableRowsLabelOptions(BaseModel):
    Visibility: StrictStr | None = None
    CustomLabel: StrictStr | None = None
