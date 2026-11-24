from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GuardDutyUpdateTrustedEntitySetRequest(BaseModel):
    DetectorId: StrictStr
    TrustedEntitySetId: StrictStr
    Name: StrictStr | None = None
    Location: StrictStr | None = None
    ExpectedBucketOwner: StrictStr | None = None
    Activate: StrictBool | None = None
