from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyGetMemberDetectorsRequest(BaseModel):
    DetectorId: StrictStr
    AccountIds: list[StrictStr]
