from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneGetSubscriptionRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
