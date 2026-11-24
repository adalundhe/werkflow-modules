from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyDisassociateMembersRequest(BaseModel):
    DetectorId: StrictStr
    AccountIds: list[StrictStr]
