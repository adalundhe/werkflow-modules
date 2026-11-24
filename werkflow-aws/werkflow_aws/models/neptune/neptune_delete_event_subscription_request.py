from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NeptuneDeleteEventSubscriptionRequest(BaseModel):
    SubscriptionName: StrictStr
