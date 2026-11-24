from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EventBridgeRetryPolicy(BaseModel):
    MaximumRetryAttempts: StrictInt | None = None
    MaximumEventAgeInSeconds: StrictInt | None = None
