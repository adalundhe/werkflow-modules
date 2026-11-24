from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubDeleteInvitationsRequest(BaseModel):
    AccountIds: list[StrictStr]
