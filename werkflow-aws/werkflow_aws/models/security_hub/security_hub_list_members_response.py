from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_hub_member import SecurityHubMember


class SecurityHubListMembersResponse(BaseModel):
    Members: list[SecurityHubMember] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
