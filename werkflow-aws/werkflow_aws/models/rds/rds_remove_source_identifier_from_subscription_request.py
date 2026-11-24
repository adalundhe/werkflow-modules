from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSRemoveSourceIdentifierFromSubscriptionRequest(BaseModel):
    SubscriptionName: StrictStr
    SourceIdentifier: StrictStr
