from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSDeleteEventSubscriptionRequest(BaseModel):
    SubscriptionName: StrictStr
