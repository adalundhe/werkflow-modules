from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneUpdateSubscriptionRequestRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
    requestReason: StrictStr
