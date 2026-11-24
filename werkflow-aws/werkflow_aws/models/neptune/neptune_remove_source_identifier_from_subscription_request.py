from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NeptuneRemoveSourceIdentifierFromSubscriptionRequest(BaseModel):
    SubscriptionName: StrictStr
    SourceIdentifier: StrictStr
