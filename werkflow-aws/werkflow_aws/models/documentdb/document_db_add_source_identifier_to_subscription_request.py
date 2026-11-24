from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DocumentDBAddSourceIdentifierToSubscriptionRequest(BaseModel):
    SubscriptionName: StrictStr
    SourceIdentifier: StrictStr
