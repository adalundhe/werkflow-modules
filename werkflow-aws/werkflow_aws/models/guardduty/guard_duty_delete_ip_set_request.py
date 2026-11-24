from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyDeleteIPSetRequest(BaseModel):
    DetectorId: StrictStr
    IpSetId: StrictStr
