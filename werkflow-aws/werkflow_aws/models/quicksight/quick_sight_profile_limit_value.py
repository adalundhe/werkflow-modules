from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightProfileLimitValue(BaseModel):
    maxValue: StrictInt | None = None
    unit: StrictStr | None = None
