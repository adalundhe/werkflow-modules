from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESTopicPreference(BaseModel):
    TopicName: StrictStr | None = None
    SubscriptionStatus: StrictStr | None = None
