from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .managed_blockchain_invitation import ManagedBlockchainInvitation


class ManagedBlockchainListInvitationsResponse(BaseModel):
    Invitations: list[ManagedBlockchainInvitation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
