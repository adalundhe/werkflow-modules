from __future__ import annotations
from pydantic import BaseModel, StrictInt


class FirehoseHttpEndpointRetryOptions(BaseModel):
    DurationInSeconds: StrictInt | None = None
