from __future__ import annotations
from pydantic import BaseModel, StrictInt


class FirehoseRetryOptions(BaseModel):
    DurationInSeconds: StrictInt | None = None
