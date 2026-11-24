from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ManagedBlockchainRejectInvitationRequest(BaseModel):
    InvitationId: StrictStr
