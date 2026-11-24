from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .managed_blockchain_member import ManagedBlockchainMember


class ManagedBlockchainGetMemberResponse(BaseModel):
    Member: ManagedBlockchainMember | None = None
    ResponseMetadata: dict[str, Any] | None = None
