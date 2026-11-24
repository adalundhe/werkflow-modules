from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2CreateSpotDatafeedSubscriptionRequest(BaseModel):
    Bucket: StrictStr
    DryRun: StrictBool | None = None
    Prefix: StrictStr | None = None
