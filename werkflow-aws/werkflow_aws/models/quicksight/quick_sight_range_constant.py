from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightRangeConstant(BaseModel):
    Minimum: StrictStr | None = None
    Maximum: StrictStr | None = None
