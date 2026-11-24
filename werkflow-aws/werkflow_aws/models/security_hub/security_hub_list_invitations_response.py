from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_hub_invitation import SecurityHubInvitation


class SecurityHubListInvitationsResponse(BaseModel):
    Invitations: list[SecurityHubInvitation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
