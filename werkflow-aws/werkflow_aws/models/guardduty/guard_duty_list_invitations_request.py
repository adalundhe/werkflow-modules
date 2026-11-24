from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GuardDutyListInvitationsRequest(BaseModel):
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
