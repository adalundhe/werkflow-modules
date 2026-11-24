from __future__ import annotations
from pydantic import BaseModel, StrictInt


class FirehoseSnowflakeRetryOptions(BaseModel):
    DurationInSeconds: StrictInt | None = None
