from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GuardDutyListMembersRequest(BaseModel):
    DetectorId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    OnlyAssociated: StrictStr | None = None
