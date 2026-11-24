from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ManagedBlockchainProposalSummary(BaseModel):
    ProposalId: StrictStr | None = None
    Description: StrictStr | None = None
    ProposedByMemberId: StrictStr | None = None
    ProposedByMemberName: StrictStr | None = None
    Status: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    ExpirationDate: datetime.datetime | StrictStr | None = None
    Arn: StrictStr | None = None
