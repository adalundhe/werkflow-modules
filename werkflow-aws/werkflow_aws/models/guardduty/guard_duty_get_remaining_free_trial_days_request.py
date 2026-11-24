from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyGetRemainingFreeTrialDaysRequest(BaseModel):
    DetectorId: StrictStr
    AccountIds: list[StrictStr]
