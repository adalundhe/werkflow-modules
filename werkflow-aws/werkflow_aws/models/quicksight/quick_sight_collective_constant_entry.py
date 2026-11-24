from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightCollectiveConstantEntry(BaseModel):
    ConstantType: StrictStr | None = None
    Value: StrictStr | None = None
