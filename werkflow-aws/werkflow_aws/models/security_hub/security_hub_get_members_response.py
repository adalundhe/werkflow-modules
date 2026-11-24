from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .security_hub_member import SecurityHubMember
from .security_hub_result import SecurityHubResult


class SecurityHubGetMembersResponse(BaseModel):
    Members: list[SecurityHubMember] | None = None
    UnprocessedAccounts: list[SecurityHubResult] | None = None
    ResponseMetadata: dict[str, Any] | None = None
