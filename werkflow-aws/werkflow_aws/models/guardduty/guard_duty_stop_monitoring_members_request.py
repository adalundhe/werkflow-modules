from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyStopMonitoringMembersRequest(BaseModel):
    DetectorId: StrictStr
    AccountIds: list[StrictStr]
