from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ManagedBlockchainVoteOnProposalRequest(BaseModel):
    NetworkId: StrictStr
    ProposalId: StrictStr
    VoterMemberId: StrictStr
    Vote: Literal['YES', 'NO']
