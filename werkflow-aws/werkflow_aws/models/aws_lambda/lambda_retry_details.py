from __future__ import annotations
from pydantic import BaseModel, StrictInt


class LambdaRetryDetails(BaseModel):
    CurrentAttempt: StrictInt | None = None
    NextAttemptDelaySeconds: StrictInt | None = None
