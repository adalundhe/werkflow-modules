from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ManagedBlockchainListProposalVotesRequest(BaseModel):
    NetworkId: StrictStr
    ProposalId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
