from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NeptuneAddSourceIdentifierToSubscriptionRequest(BaseModel):
    SubscriptionName: StrictStr
    SourceIdentifier: StrictStr
