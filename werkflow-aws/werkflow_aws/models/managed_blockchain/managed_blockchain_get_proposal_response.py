from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .managed_blockchain_proposal import ManagedBlockchainProposal


class ManagedBlockchainGetProposalResponse(BaseModel):
    Proposal: ManagedBlockchainProposal | None = None
    ResponseMetadata: dict[str, Any] | None = None
