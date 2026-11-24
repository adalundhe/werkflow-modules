from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightFieldSort(BaseModel):
    FieldId: StrictStr | None = None
    Direction: StrictStr | None = None
