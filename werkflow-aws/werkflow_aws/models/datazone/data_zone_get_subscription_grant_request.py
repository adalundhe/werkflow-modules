from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneGetSubscriptionGrantRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
