from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightPivotTableFieldOption(BaseModel):
    FieldId: StrictStr | None = None
    CustomLabel: StrictStr | None = None
    Visibility: StrictStr | None = None
