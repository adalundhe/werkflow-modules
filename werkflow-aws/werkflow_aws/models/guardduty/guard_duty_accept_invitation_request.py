from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyAcceptInvitationRequest(BaseModel):
    DetectorId: StrictStr
    MasterId: StrictStr
    InvitationId: StrictStr
