from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyDeleteTrustedEntitySetRequest(BaseModel):
    DetectorId: StrictStr
    TrustedEntitySetId: StrictStr
