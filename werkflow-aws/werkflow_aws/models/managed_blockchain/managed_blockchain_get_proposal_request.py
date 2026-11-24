from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ManagedBlockchainGetProposalRequest(BaseModel):
    NetworkId: StrictStr
    ProposalId: StrictStr
