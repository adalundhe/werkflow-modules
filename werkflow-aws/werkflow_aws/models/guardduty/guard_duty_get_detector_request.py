from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyGetDetectorRequest(BaseModel):
    DetectorId: StrictStr
