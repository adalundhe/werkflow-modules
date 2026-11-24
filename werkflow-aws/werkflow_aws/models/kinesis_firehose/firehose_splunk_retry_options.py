from __future__ import annotations
from pydantic import BaseModel, StrictInt


class FirehoseSplunkRetryOptions(BaseModel):
    DurationInSeconds: StrictInt | None = None
