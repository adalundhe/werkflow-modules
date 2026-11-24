from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GuardDutyUpdateIPSetRequest(BaseModel):
    DetectorId: StrictStr
    IpSetId: StrictStr
    Name: StrictStr | None = None
    Location: StrictStr | None = None
    Activate: StrictBool | None = None
    ExpectedBucketOwner: StrictStr | None = None
