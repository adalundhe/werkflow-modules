from __future__ import annotations
from pydantic import BaseModel, StrictInt


class FirehoseSnowflakeBufferingHints(BaseModel):
    SizeInMBs: StrictInt | None = None
    IntervalInSeconds: StrictInt | None = None
