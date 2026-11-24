from __future__ import annotations
from pydantic import BaseModel, StrictInt


class KinesisAnalyticsInputParallelism(BaseModel):
    Count: StrictInt | None = None
