from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .macie_invitation import MacieInvitation


class MacieListInvitationsResponse(BaseModel):
    invitations: list[MacieInvitation] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
