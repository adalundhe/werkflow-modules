from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .managed_blockchain_proposal_actions import ManagedBlockchainProposalActions


class ManagedBlockchainCreateProposalRequest(BaseModel):
    ClientRequestToken: StrictStr
    NetworkId: StrictStr
    MemberId: StrictStr
    Actions: ManagedBlockchainProposalActions
    Description: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
