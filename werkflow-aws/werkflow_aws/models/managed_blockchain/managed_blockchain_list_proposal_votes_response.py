from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .managed_blockchain_vote_summary import ManagedBlockchainVoteSummary


class ManagedBlockchainListProposalVotesResponse(BaseModel):
    ProposalVotes: list[ManagedBlockchainVoteSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
