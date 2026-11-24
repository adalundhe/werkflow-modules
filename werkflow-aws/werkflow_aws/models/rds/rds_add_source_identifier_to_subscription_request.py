from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSAddSourceIdentifierToSubscriptionRequest(BaseModel):
    SubscriptionName: StrictStr
    SourceIdentifier: StrictStr
