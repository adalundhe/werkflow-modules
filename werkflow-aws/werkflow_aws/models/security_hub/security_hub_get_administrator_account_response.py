from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .security_hub_invitation import SecurityHubInvitation


class SecurityHubGetAdministratorAccountResponse(BaseModel):
    Administrator: SecurityHubInvitation | None = None
    ResponseMetadata: dict[str, Any] | None = None
