from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SchedulerRetryPolicy(BaseModel):
    MaximumEventAgeInSeconds: StrictInt | None = None
    MaximumRetryAttempts: StrictInt | None = None
