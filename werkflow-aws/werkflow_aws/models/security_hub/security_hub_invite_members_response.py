from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .security_hub_result import SecurityHubResult


class SecurityHubInviteMembersResponse(BaseModel):
    UnprocessedAccounts: list[SecurityHubResult] | None = None
    ResponseMetadata: dict[str, Any] | None = None
