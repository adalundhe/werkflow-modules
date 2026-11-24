from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightSelectableValuesSort(BaseModel):
    Direction: StrictStr | None = None
