from __future__ import annotations
from pydantic import BaseModel, StrictInt


class KinesisAnalyticsInputParallelismUpdate(BaseModel):
    CountUpdate: StrictInt
