from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyDeleteFilterRequest(BaseModel):
    DetectorId: StrictStr
    FilterName: StrictStr
