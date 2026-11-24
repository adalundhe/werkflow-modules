from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .managed_blockchain_proposal_summary import ManagedBlockchainProposalSummary


class ManagedBlockchainListProposalsResponse(BaseModel):
    Proposals: list[ManagedBlockchainProposalSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
