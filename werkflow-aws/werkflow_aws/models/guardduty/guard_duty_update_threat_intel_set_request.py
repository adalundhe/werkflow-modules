from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GuardDutyUpdateThreatIntelSetRequest(BaseModel):
    DetectorId: StrictStr
    ThreatIntelSetId: StrictStr
    Name: StrictStr | None = None
    Location: StrictStr | None = None
    Activate: StrictBool | None = None
    ExpectedBucketOwner: StrictStr | None = None
