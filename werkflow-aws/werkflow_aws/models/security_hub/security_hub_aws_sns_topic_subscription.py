from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsSnsTopicSubscription(BaseModel):
    Endpoint: StrictStr | None = None
    Protocol: StrictStr | None = None
