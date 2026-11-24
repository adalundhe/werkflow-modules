from __future__ import annotations
from pydantic import BaseModel, StrictInt


class FirehoseRedshiftRetryOptions(BaseModel):
    DurationInSeconds: StrictInt | None = None
