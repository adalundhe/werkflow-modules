from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SNSSubscription(BaseModel):
    SubscriptionArn: StrictStr | None = None
    Owner: StrictStr | None = None
    Protocol: StrictStr | None = None
    Endpoint: StrictStr | None = None
    TopicArn: StrictStr | None = None
