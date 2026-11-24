from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ManagedBlockchainVoteSummary(BaseModel):
    Vote: StrictStr | None = None
    MemberName: StrictStr | None = None
    MemberId: StrictStr | None = None
