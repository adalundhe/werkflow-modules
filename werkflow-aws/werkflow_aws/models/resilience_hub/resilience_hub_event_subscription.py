from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubEventSubscription(BaseModel):
    eventType: StrictStr | None = None
    name: StrictStr | None = None
    snsTopicArn: StrictStr | None = None
