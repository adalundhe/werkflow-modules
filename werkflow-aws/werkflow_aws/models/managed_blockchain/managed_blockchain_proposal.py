from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .managed_blockchain_proposal_actions import ManagedBlockchainProposalActions


class ManagedBlockchainProposal(BaseModel):
    ProposalId: StrictStr | None = None
    NetworkId: StrictStr | None = None
    Description: StrictStr | None = None
    Actions: ManagedBlockchainProposalActions | None = None
    ProposedByMemberId: StrictStr | None = None
    ProposedByMemberName: StrictStr | None = None
    Status: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    ExpirationDate: datetime.datetime | StrictStr | None = None
    YesVoteCount: StrictInt | None = None
    NoVoteCount: StrictInt | None = None
    OutstandingVoteCount: StrictInt | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    Arn: StrictStr | None = None
