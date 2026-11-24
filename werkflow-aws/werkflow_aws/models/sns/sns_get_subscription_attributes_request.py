from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SNSGetSubscriptionAttributesRequest(BaseModel):
    SubscriptionArn: StrictStr
