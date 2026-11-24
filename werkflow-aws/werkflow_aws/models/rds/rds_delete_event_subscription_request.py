from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSDeleteEventSubscriptionRequest(BaseModel):
    SubscriptionName: StrictStr
