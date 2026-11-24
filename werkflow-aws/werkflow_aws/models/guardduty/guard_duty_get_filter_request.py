from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyGetFilterRequest(BaseModel):
    DetectorId: StrictStr
    FilterName: StrictStr
