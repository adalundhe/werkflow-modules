from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightPivotTableConditionalFormattingScope(BaseModel):
    Role: StrictStr | None = None
