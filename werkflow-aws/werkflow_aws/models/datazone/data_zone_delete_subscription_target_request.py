from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneDeleteSubscriptionTargetRequest(BaseModel):
    domainIdentifier: StrictStr
    environmentIdentifier: StrictStr
    identifier: StrictStr
