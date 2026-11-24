from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyGetMembersRequest(BaseModel):
    DetectorId: StrictStr
    AccountIds: list[StrictStr]
