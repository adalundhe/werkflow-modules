from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneDeleteSubscriptionGrantRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
