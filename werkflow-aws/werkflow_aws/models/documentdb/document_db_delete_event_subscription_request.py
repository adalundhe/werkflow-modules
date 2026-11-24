from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DocumentDBDeleteEventSubscriptionRequest(BaseModel):
    SubscriptionName: StrictStr
