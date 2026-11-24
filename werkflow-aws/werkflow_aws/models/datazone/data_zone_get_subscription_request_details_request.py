from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneGetSubscriptionRequestDetailsRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
