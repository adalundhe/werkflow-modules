from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DocumentDBRemoveSourceIdentifierFromSubscriptionRequest(BaseModel):
    SubscriptionName: StrictStr
    SourceIdentifier: StrictStr
