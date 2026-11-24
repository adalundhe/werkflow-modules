from __future__ import annotations
from pydantic import BaseModel, StrictInt


class LambdaCallbackOptions(BaseModel):
    TimeoutSeconds: StrictInt | None = None
    HeartbeatTimeoutSeconds: StrictInt | None = None
