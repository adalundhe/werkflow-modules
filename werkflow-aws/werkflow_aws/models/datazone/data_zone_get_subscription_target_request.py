from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneGetSubscriptionTargetRequest(BaseModel):
    domainIdentifier: StrictStr
    environmentIdentifier: StrictStr
    identifier: StrictStr
