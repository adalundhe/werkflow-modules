from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieAcceptInvitationRequest(BaseModel):
    invitationId: StrictStr
    administratorAccountId: StrictStr | None = None
    masterAccount: StrictStr | None = None
