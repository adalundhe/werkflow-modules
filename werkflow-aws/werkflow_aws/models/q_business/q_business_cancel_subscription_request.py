from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessCancelSubscriptionRequest(BaseModel):
    applicationId: StrictStr
    subscriptionId: StrictStr
