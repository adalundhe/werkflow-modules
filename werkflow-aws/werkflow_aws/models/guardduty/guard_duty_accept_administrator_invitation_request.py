from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyAcceptAdministratorInvitationRequest(BaseModel):
    DetectorId: StrictStr
    AdministratorId: StrictStr
    InvitationId: StrictStr
