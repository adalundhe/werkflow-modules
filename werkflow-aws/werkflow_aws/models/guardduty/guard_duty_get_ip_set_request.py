from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyGetIPSetRequest(BaseModel):
    DetectorId: StrictStr
    IpSetId: StrictStr
