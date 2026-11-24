from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAcceptInvitationRequest(BaseModel):
    MasterId: StrictStr
    InvitationId: StrictStr
