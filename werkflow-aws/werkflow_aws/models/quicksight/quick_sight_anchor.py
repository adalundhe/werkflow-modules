from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightAnchor(BaseModel):
    AnchorType: StrictStr | None = None
    TimeGranularity: StrictStr | None = None
    Offset: StrictInt | None = None
