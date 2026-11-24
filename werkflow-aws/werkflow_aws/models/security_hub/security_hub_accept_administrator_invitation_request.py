from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAcceptAdministratorInvitationRequest(BaseModel):
    AdministratorId: StrictStr
    InvitationId: StrictStr
