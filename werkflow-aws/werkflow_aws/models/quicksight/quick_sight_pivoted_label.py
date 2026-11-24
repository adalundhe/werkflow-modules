from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightPivotedLabel(BaseModel):
    LabelName: StrictStr | None = None
    NewColumnName: StrictStr | None = None
    NewColumnId: StrictStr | None = None
