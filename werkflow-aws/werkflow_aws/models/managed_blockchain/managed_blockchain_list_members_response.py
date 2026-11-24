from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .managed_blockchain_member_summary import ManagedBlockchainMemberSummary


class ManagedBlockchainListMembersResponse(BaseModel):
    Members: list[ManagedBlockchainMemberSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
