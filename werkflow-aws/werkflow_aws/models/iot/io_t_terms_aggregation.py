from __future__ import annotations
from pydantic import BaseModel, StrictInt


class IoTTermsAggregation(BaseModel):
    maxBuckets: StrictInt | None = None
