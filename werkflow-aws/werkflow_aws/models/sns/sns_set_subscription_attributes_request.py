from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SNSSetSubscriptionAttributesRequest(BaseModel):
    SubscriptionArn: StrictStr
    AttributeName: StrictStr
    AttributeValue: StrictStr | None = None
