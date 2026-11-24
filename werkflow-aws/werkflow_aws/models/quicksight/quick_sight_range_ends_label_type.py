from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightRangeEndsLabelType(BaseModel):
    Visibility: StrictStr | None = None
