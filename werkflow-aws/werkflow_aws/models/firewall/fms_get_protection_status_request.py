from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class FMSGetProtectionStatusRequest(BaseModel):
    PolicyId: StrictStr
    MemberAccountId: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
