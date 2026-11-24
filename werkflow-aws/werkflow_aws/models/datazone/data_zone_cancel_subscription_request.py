from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneCancelSubscriptionRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
