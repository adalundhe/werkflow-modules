from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyDestinationProperties(BaseModel):
    DestinationArn: StrictStr | None = None
    KmsKeyArn: StrictStr | None = None
    ExpectedBucketOwner: StrictStr | None = None
