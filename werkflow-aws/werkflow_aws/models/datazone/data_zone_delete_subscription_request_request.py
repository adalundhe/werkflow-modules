from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneDeleteSubscriptionRequestRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
