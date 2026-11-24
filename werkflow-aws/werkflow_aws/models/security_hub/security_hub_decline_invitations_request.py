from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubDeclineInvitationsRequest(BaseModel):
    AccountIds: list[StrictStr]
