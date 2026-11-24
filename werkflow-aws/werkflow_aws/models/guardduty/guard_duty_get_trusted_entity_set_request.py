from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyGetTrustedEntitySetRequest(BaseModel):
    DetectorId: StrictStr
    TrustedEntitySetId: StrictStr
